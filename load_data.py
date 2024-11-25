from langchain_community.document_loaders import PyPDFLoader


def get_text():
    loader = PyPDFLoader("data/C&W Supporting Document.pdf")
    pages = loader.load()
    
    text = ""
    for page in pages:
        text += page.page_content
        
    return text