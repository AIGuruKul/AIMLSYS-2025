# Document QA Application with Gemini Pro

This application allows you to load documents (PDF, DOCX, or TXT) and ask questions about their content using Google's Gemini Pro model.

## Setup

1. Create a `.env` file in the root directory with your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface (Recommended)

Run the Streamlit web application:

```bash
streamlit run src/app.py
```

This will:
1. Start a local web server
2. Open the application in your default web browser
3. Allow you to upload documents and ask questions through a user-friendly interface

### Command Line Interface

Alternatively, you can use the command-line version:

```bash
python src/main.py path/to/your/document.pdf
```

The CLI application will:
1. Load the document
2. Start an interactive session where you can ask questions about the document
3. Type 'quit' to exit the application

## Supported File Types
- PDF (.pdf)
- Word Documents (.docx)
- Text files (.txt)

## Features
- Document content extraction
- Interactive question-answering using Gemini Pro
- Support for multiple document formats
- Error handling and user-friendly interface
