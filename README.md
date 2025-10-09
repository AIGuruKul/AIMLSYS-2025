# AIMLSYS-2025

# Document QA Application with Gemini Pro & Web Search

## 🎯 About This Project

This intelligent Document QA application was built during the **AIML System 2025 Conference Tutorial** using **Vibe Coding** methodology in just **1 hour**! 

### 📚 Conference Details
- **Event**: AIML System 2025 Conference
- **Session Type**: Tutorial - Vibe Coding
- **Duration**: 1 Hour
- **Session Instructor**: [Anupam Purwar](https://github.com/anupampurwar)
- **Volunteer**: [Chitranshu Harbola](https://github.com/chitranshu)

## 🚀 What This Application Does

This powerful application combines document processing with AI-powered question answering and real-time web search to provide comprehensive answers about your documents.

### Key Functionalities

1. **Multi-Format Document Processing**
   - PDF files (.pdf)
   - Word Documents (.docx)
   - Text files (.txt)
   - Images with OCR (.png, .jpg, .jpeg, .tiff, .bmp)

2. **AI-Powered Q&A**
   - Uses Google's Gemini 2.5-Flash model
   - Fallback to Gemini Pro for reliability
   - Context-aware responses

3. **Web Search Integration**
   - Real-time web search using Serper API
   - Combines document content with current web information
   - Provides enriched, up-to-date answers

4. **Dual Interface Options**
   - **Web Interface**: Beautiful Streamlit-based UI
   - **Command Line Interface**: For programmatic use

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key
- Serper API key (for web search)
- Tesseract OCR (for image processing)

### Installation Steps

1. **Clone the repository**:
```bash
git clone https://github.com/AIGuruKul/AIMLSYS-2025.git
cd AIMLSYS-2025
```

2. **Create a virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Install Tesseract OCR** (for image processing):
```bash
# macOS
brew install tesseract

# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```

5. **Set up API keys**:
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## 🎮 Usage

### Web Interface (Recommended)

Launch the Streamlit web application:

```bash
streamlit run src/app.py
```

Features:
- 📁 Drag & drop file upload
- 🔍 Interactive question-answering
- 📊 Document preview
- 📝 Q&A history tracking
- 🌐 Web search integration

### Command Line Interface

For programmatic or batch processing:

```bash
python src/main.py path/to/your/document.pdf
```

## 🏗️ Architecture

```
AIMLSYS-2025/
├── src/
│   ├── app.py                 # Streamlit web interface
│   ├── document_processor.py  # Core processing logic
│   └── main.py               # CLI interface
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
└── README.md               # This file
```

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5-Flash
- **Web Search**: Serper API
- **OCR**: Tesseract
- **Document Processing**: PyPDF2, python-docx
- **Image Processing**: PIL (Pillow)

## 🎨 Vibe Coding Methodology

This project demonstrates the power of **Vibe Coding** - a rapid development methodology that emphasizes:
- ⚡ Quick prototyping
- 🎯 Focus on core functionality
- 🔄 Iterative development
- 🤖 AI-assisted coding
- 🚀 Rapid deployment

## 🌟 Advanced Features

- **Smart Fallback**: Automatically switches between Gemini models
- **Error Handling**: Comprehensive error management
- **Multi-modal**: Supports text and image inputs
- **Context Enrichment**: Combines document + web information
- **User-friendly**: Intuitive interfaces for all skill levels

## 🚀 Getting Started - Quick Demo

1. Start the application: `streamlit run src/app.py`
2. Upload a document (PDF, DOCX, TXT, or image)
3. Ask questions like:
   - "What is the main topic of this document?"
   - "Summarize the key points"
   - "What are the latest developments in [topic from document]?"

## 🤝 Contributing

This project was created as an educational demonstration. Feel free to:
- Fork the repository
- Submit pull requests
- Report issues
- Suggest improvements

## 📄 License

MIT License - Feel free to use this project for learning and development.

## 🙏 Acknowledgments

Special thanks to:
- **AIML System 2025 Conference** organizers
- **Anupam Purwar** for expert instruction
- **Chitranshu Harbola** for volunteer support
- The open-source community for the amazing tools and libraries

---

**Built with ❤️ during AIML System 2025 Conference using Vibe Coding methodology**
