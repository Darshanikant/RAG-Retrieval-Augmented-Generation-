# RAG-Retrieval-Augmented-Generation-


# **RAG-Based Document Search & Q\&A System**

This project implements a **Retrieval-Augmented Generation (RAG)** model for intelligent document search and contextual question answering. The system allows users to query unstructured documents (PDF, DOCX, TXT), performs semantic search using vector databases, and generates meaningful responses via an LLM.

---

##  **Key Features**

*  Supports loading documents in **PDF, DOCX, and TXT** formats
*  Converts documents and queries to **embeddings** using:

  * `Google Generative AI embeddings (embedding-001)`
  * Alternative: `HuggingFace embeddings`
*  Stores vector embeddings in **FAISS (Facebook AI Similarity Search)** for efficient semantic search
*  Combines relevant document chunks + user query → passes to **LLM (e.g. Gemini)** for final response generation
*  Modular, scalable design


##  **How It Works**

### 1 **Document Loading**

* Load and parse documents:

  * **PDF** → `PyPDFLoader`
  * **DOCX** → `python-docx`
  * **TXT** → standard file read
* Output: List of document chunks

---

### 2️ **Embedding Generation**

* Generate embeddings for all document chunks
* Use:

  * `Google Generative AI embeddings (embedding-001)`
  * Optionally: `HuggingFace embedding models`

---

### 3️ **Vector Database Storage**

* Store the embeddings in **FAISS vector database**
* Enables fast similarity search during queries

---

### 4️ **User Query Embedding**

* Convert incoming user query to embedding
* Use the **same embedding model** (Google/HuggingFace) for consistency

---

### 5️ **Semantic Search**

* Perform similarity search:

  * Match query embedding against stored document embeddings
  * Retrieve top relevant document chunks

---

### 6️ **LLM-Based Answer Generation**

* Pass **user query + matched document chunks** to an LLM (e.g., Gemini)
* LLM generates a context-aware response
* Display the result to the user

---

##  **Tech Stack**

* **Python**
* **FAISS** (vector database)
* **LangChain**
* **Google Generative AI embeddings**
* **HuggingFace (optional)**
* **PyPDFLoader / python-docx**
* **LLM (e.g. Gemini)**

---

##  **Project Flow Diagram (Text Version)**

```
[ User uploads documents (PDF / DOCX / TXT) ]
            ↓
[ Document Parsing ]
            ↓
[ Embedding Generation ]
            ↓
[ Store in FAISS vector DB ]
            ↓
[ User submits query ]
            ↓
[ Query embedding generation ]
            ↓
[ Semantic search in vector DB ]
            ↓
[ Pass matched docs + query to LLM ]
            ↓
[ LLM generates answer ]
            ↓
[ Display to user ]
```

---

##  **How to Run**

1 Install required libraries

```bash
pip install faiss-cpu langchain google-generativeai transformers pypdf python-docx
```

2 Set up your **Google Generative AI API key** (or HuggingFace model)

3 Run your script or app (e.g., Streamlit or command line)

---

##  **Applications**

* Document intelligence assistants
* Knowledge base Q\&A systems
* AI-powered legal, healthcare, or enterprise search
* Chatbots with real document grounding

