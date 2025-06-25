# modules/gemini_answer.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-flash")

def format_docs(docs):
    """Concatenate the page content of retrieved documents into a single context string."""
    return "\n\n".join(doc.page_content for doc in docs)

def ask_gemini_with_context(query, docs):
    """
    Sends the user query and the context (retrieved docs) to Gemini and returns its answer.
    """
    context = format_docs(docs)
    prompt = f"""You are a helpful assistant. Use the below context to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

    response = model.generate_content(prompt)
    return response.text
