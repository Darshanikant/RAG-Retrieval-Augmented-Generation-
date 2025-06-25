from embedding.embedder import embedding_model  
from modules.database import VectorDB
from modules.loader import load_documents
from modules.gemini_answer import ask_gemini_with_context

def main():
    print("\n🧠 Loading documents...")
    docs = load_documents("data")

    print("📄 Splitting documents into chunks...")  

    print("📐 Generating embeddings...")
    db = VectorDB()

    print("💾 Creating and storing Vector DB...")
    db.create_vector_store(docs, embedding_model)

    print("\n✅ Setup complete. Ready to take your query!")

    while True:
        query = input("\n🗣️ Enter your question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break

        print("\n🔍 Searching relevant documents...")
        
        # Pass allow_dangerous_deserialization=True when loading the vector store
        vectorstore = db.load_vector_store(embedding_model, allow_dangerous_deserialization=True)

        relevant_docs = db.search_similar(query, embedding_model)

        print("🤖 Asking Gemini with context...")
        answer = ask_gemini_with_context(query, relevant_docs)

        print("\n💡 Answer:")
        print(answer)

if __name__ == "__main__":
    main()
