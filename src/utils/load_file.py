import PyPDF2
import docx
import io

def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def load_file(file):
    # Check the file type
    if file.type == "application/pdf":
        # Read the PDF file using PyPDF2
        text = get_pdf_text(file)
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Read the DOCX file using docx
        doc = docx.Document(file)
        # Initialize an empty string for the text
        text = ""
        # Loop through the paragraphs of the DOCX file
        for paragraph in doc.paragraphs:
            # Extract the text from the paragraph
            paragraph_text = paragraph.text
            # Append the text to the string with a newline
            text += paragraph_text + "\n"
        # Return the text
        return text
    elif file.type == "text/plain":
        # Read the TXT file using io
        text = io.TextIOWrapper(file).read()
        # Return the text
        return text
    else:
        # Return an empty string if the file type is not supported
        return ""
