# modules/database.py

import os
import faiss
import pickle
from langchain_community.vectorstores import FAISS

class VectorDB:
    def __init__(self, store_path="store/faiss_index"):
        self.store_path = store_path
        self.index = None
        self.store = None

    def save_vector_store(self, db):
        """Save the FAISS vector store to disk."""
        os.makedirs(self.store_path, exist_ok=True)
        db.save_local(self.store_path)

    def load_vector_store(self, embeddings, allow_dangerous_deserialization=False):
        """Load the FAISS vector store from disk."""
        if os.path.exists(self.store_path):
            self.store = FAISS.load_local(
                self.store_path,
                embeddings,
                allow_dangerous_deserialization=allow_dangerous_deserialization
            )
        else:
            raise FileNotFoundError("Vector store not found. Please generate it first.")
        return self.store

    def create_vector_store(self, docs, embeddings):
        """Create a FAISS vector store from documents."""
        self.store = FAISS.from_documents(docs, embeddings)
        self.save_vector_store(self.store)
        return self.store

    def search_similar(self, query, embeddings, k=3):
        """Search top K similar documents from vector store."""
        if not self.store:
            self.load_vector_store(embeddings)
        results = self.store.similarity_search(query, k=k)
        return results
