import streamlit as st
from document_processor import DocumentProcessor
import tempfile
import os

st.set_page_config(
    page_title="Document QA with Gemini Pro",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title("📚 Document QA with Gemini Pro")
    st.write("Upload a document (PDF, DOCX, or TXT) and ask questions about its content!")

    # Initialize the document processor
    try:
        processor = DocumentProcessor()
    except ValueError as e:
        st.error("Error: Make sure you have set up your GOOGLE_API_KEY in the .env file")
        return

    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg', 'tiff', 'bmp'])
    
    if uploaded_file:
        # Create a temporary file to store the uploaded content
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{uploaded_file.name.split(".")[-1]}') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        try:
            # Read the document
            with st.spinner('Reading document...'):
                document_content = processor.read_document(tmp_file_path)
                st.success("Document loaded successfully!")

            # Delete the temporary file
            os.unlink(tmp_file_path)

            # Store document content in session state
            st.session_state['document_content'] = document_content

            # Display document preview
            with st.expander("Document Preview"):
                st.text_area("Content", document_content[:1000] + "...", height=200, disabled=True)

            # Question input
            question = st.text_input("Ask a question about the document:")
            
            if question:
                with st.spinner('Getting answer...'):
                    try:
                        answer = processor.ask_question(document_content, question)
                        
                        # Display the Q&A
                        st.write("### Answer:")
                        st.write(answer)
                        
                        # Store Q&A history in session state
                        if 'qa_history' not in st.session_state:
                            st.session_state['qa_history'] = []
                        
                        st.session_state['qa_history'].append({
                            'question': question,
                            'answer': answer
                        })

                    except Exception as e:
                        st.error(f"Error getting answer: {str(e)}")

            # Display Q&A history
            if 'qa_history' in st.session_state and st.session_state['qa_history']:
                st.write("### Previous Questions & Answers")
                for qa in reversed(st.session_state['qa_history']):
                    with st.expander(f"Q: {qa['question']}"):
                        st.write(qa['answer'])

        except Exception as e:
            st.error(f"Error processing document: {str(e)}")

if __name__ == "__main__":
    main()
