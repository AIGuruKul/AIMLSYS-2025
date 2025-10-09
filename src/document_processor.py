import os
from typing import Dict, Any, List
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2
from docx import Document
import pytesseract
from PIL import Image
import requests
import json

class DocumentProcessor:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize Gemini API
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError("Please set GOOGLE_API_KEY in .env file")
        
        # Initialize Serper API
        self.serper_api_key = os.getenv("SERPER_API_KEY")
        if not self.serper_api_key:
            raise ValueError("Please set SERPER_API_KEY in .env file")
        
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        
    def search_web(self, query: str) -> List[Dict]:
        """Search the web using Serper API."""
        url = "https://google.serper.dev/search"
        headers = {
            "X-API-KEY": self.serper_api_key,
            "Content-Type": "application/json"
        }
        payload = json.dumps({"q": query})
        
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            results = response.json()
            
            web_data = []
            if "organic" in results:
                for result in results["organic"][:3]:
                    web_data.append({
                        "title": result.get("title", ""),
                        "snippet": result.get("snippet", ""),
                        "link": result.get("link", "")
                    })
            return web_data
        except Exception as e:
            print(f"Error in web search: {str(e)}")
            return []
    
    def read_pdf(self, file_path: str) -> str:
        """Read content from a PDF file."""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    
    def read_docx(self, file_path: str) -> str:
        """Read content from a DOCX file."""
        doc = Document(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    
    def read_txt(self, file_path: str) -> str:
        """Read content from a text file."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def read_image(self, file_path: str) -> str:
        """Extract text from an image using OCR."""
        try:
            image = Image.open(file_path)
            if image.mode != "RGB":
                image = image.convert("RGB")
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            raise ValueError(f"Error processing image: {str(e)}")
    
    def read_document(self, file_path: str) -> str:
        """Read content from a document based on its file extension."""
        file_extension = file_path.lower().split(".")[-1]
        
        if file_extension == "pdf":
            return self.read_pdf(file_path)
        elif file_extension == "docx":
            return self.read_docx(file_path)
        elif file_extension == "txt":
            return self.read_txt(file_path)
        elif file_extension in ["png", "jpg", "jpeg", "tiff", "bmp"]:
            return self.read_image(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
    
    def ask_question(self, document_content: str, question: str) -> str:
        """Ask a question about the document content using Gemini Flash."""
        web_results = self.search_web(question)
        web_context = ""
        if web_results:
            web_context = "\n\nRelevant web information:\n"
            for result in web_results:
                web_context += f"\n- {result['title']}\n  {result['snippet']}\n"
        
        try:
            prompt = f"Document content: {document_content}\n\n{web_context}\n\nQuestion: {question}\n\nPlease provide a clear and concise answer based on both the document content and any relevant web information above. If the web information provides additional context, incorporate it into your answer while primarily focusing on the document content."
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            try:
                self.model = genai.GenerativeModel("gemini-pro")
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e2:
                raise ValueError(f"Error generating response with fallback model: {str(e2)}")
