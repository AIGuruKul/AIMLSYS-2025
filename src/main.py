from document_processor import DocumentProcessor
import sys

def main():
    # Initialize the document processor
    processor = DocumentProcessor()
    
    # Check if file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Please provide the document file path as a command line argument")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        # Read the document
        print(f"Reading document: {file_path}")
        document_content = processor.read_document(file_path)
        print("Document loaded successfully!")
        
        # Interactive question-answering loop
        while True:
            question = input("\nEnter your question (or 'quit' to exit): ")
            
            if question.lower() == 'quit':
                break
            
            try:
                answer = processor.ask_question(document_content, question)
                print("\nAnswer:", answer)
            except Exception as e:
                print(f"Error getting answer: {str(e)}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
