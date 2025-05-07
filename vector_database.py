from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # using google genai
from langchain_community.vectorstores import FAISS
import os

# Step_1: Upload & Load raw PDF(s)
pdfs_directory = 'pdfs/'

def upload_pdf(file):
    os.makedirs(pdfs_directory, exist_ok=True)
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

file_path = 'universal_declaration_of_human_rights.pdf'
documents = load_pdf(file_path)

# Step_2: Create Chunks
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

text_chunks = create_chunks(documents)

# Step_3: Setup Embeddings Model
def get_embedding_model():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings

# Step_4: Index Documents
FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, get_embedding_model())
faiss_db.save_local(FAISS_DB_PATH)