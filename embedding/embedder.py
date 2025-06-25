# embedding/embedder.py

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.embeddings.base import Embeddings
from dotenv import load_dotenv
import os

# Load the API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Safety check
if not GOOGLE_API_KEY or not GOOGLE_API_KEY.startswith("AIza"):
    raise ValueError("Invalid or missing GOOGLE_API_KEY in .env")

# Gemini Embedding model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

def get_embeddings(text_list: list[str]) -> list[list[float]]:
    """Returns a list of embeddings for a list of documents/text chunks."""
    return embedding_model.embed_documents(text_list)
