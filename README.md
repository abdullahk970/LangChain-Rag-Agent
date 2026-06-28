# 🧠 LangChain RAG + AI Agent System

> A dual-purpose **LangChain-based AI system** that combines:
>
> 1. 📄 PDF-based Retrieval-Augmented Generation (RAG)
> 2. 🤖 Tool-using AI Agent (Calendar + Email Assistant)

Built using **LangChain, Ollama, ChromaDB, and local LLMs**, this project demonstrates both **knowledge-based QA systems** and **functional AI agents with tools and memory**.

---

# 🚀 Overview

This project contains two intelligent AI systems:

### 1️⃣ PDF RAG System

An offline document QA system that:

* Loads PDF documents
* Splits them into chunks
* Stores embeddings in ChromaDB
* Uses LLaMA 2 (Ollama) for context-based answering

### 2️⃣ AI Personal Assistant Agent

A tool-using conversational agent that can:

* Manage calendar events
* Send and list emails
* Maintain conversation memory
* Use function-calling style tools via LangChain agents

---

# ✨ Features

## 📄 RAG System Features

* PDF document loading using `PyPDFLoader`
* Smart text chunking (Recursive splitter)
* Local vector database (ChromaDB)
* Semantic search using embeddings
* Context-only answering (no hallucination)
* Offline LLM via Ollama (LLaMA2)

## 🤖 AI Agent Features

* Calendar event management
* Email sending simulation system
* Tool-based function calling
* Conversation memory support
* Multi-tool orchestration
* Interactive CLI assistant

---

# 🧠 Architecture Overview

## 📄 RAG Pipeline

```text id="rag-flow"
PDF Document
     │
     ▼
Text Extraction (PyPDFLoader)
     │
     ▼
Chunking (Recursive Splitter)
     │
     ▼
Embeddings (Ollama: nomic-embed-text)
     │
     ▼
Chroma Vector DB
     │
     ▼
User Question
     │
     ▼
Retriever (MMR Search)
     │
     ▼
LLM (LLaMA 2 via Ollama)
     │
     ▼
Context-Based Answer
```

---

## 🤖 AI Agent Flow

```text id="agent-flow"
User Input
     │
     ▼
LangChain Agent
     │
     ├── Calendar Tool
     ├── Email Tool
     ├── List Events Tool
     └── List Emails Tool
     │
     ▼
Memory (Conversation Buffer)
     │
     ▼
LLM (Phi via Ollama)
     │
     ▼
Final Response
```

---

# 🏗️ Tech Stack

### 🧠 AI & LLMs

* Ollama
* LLaMA 2 (Chat Model)
* Phi Model

### 🔗 LangChain Components

* RetrievalQA
* Agents (OpenAI Functions Agent style)
* PromptTemplate & ChatPromptTemplate
* Memory (ConversationBufferMemory)

### 📄 Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

### 🗄️ Vector Database

* ChromaDB (Local Persistent Storage)

---

# 📂 Project Structure

```text id="langchain-structure"
langchain-project/
│
├── rag_system.py        # PDF RAG QA system
├── agent_system.py      # AI tools-based assistant
├── chroma_ollama/       # Vector database storage
├── manual.pdf           # Knowledge base document
└── README.md
```

---

# 📄 RAG SYSTEM (How It Works)

## Step-by-step Flow:

1. Load PDF document
2. Split into chunks (800 tokens)
3. Create embeddings using:

   * `nomic-embed-text`
4. Store vectors in ChromaDB
5. Retrieve top-K relevant chunks
6. Pass context to LLaMA 2
7. Generate grounded answer

---

## 🧠 Prompt Strategy

The system enforces strict grounding:

```text id="rag-prompt"
You are an assistant that answers questions using ONLY the provided context.
If answer is not in the context, reply "I don't know".
```

✔ Prevents hallucination
✔ Forces document-based reasoning

---

# 🤖 AI AGENT (Tools System)

## 🛠️ Available Tools

### 📅 Calendar Tools

* Add Event

```text
Format: YYYY-MM-DD|Event description
```

* List Events

---

### 📧 Email Tools

* Send Email

```text
Format: Recipient|Subject|Body
```

* List Emails

---

## 🧠 Memory System

* Uses `ConversationBufferMemory`
* Stores chat history
* Enables contextual conversations

---

## 🤖 Agent Configuration

* Model: `phi` (Ollama)
* Agent Type: Function-calling style agent
* Execution Mode: Tool-augmented reasoning

---

# ⚙️ Installation

## Clone Repository

```bash id="clone-langchain"
git clone https://github.com/yourusername/langchain-project.git

cd langchain-project
```

---

## Install Dependencies

```bash id="install-langchain"
pip install langchain langchain-community langchain-ollama chromadb pypdf
```

---

## Install & Run Ollama

```bash id="ollama-run"
ollama serve
```

Pull required models:

```bash id="ollama-models"
ollama pull llama2
ollama pull phi
ollama pull nomic-embed-text
```

---

# 🚀 Run Project

## 1️⃣ Run RAG System

```bash id="run-rag"
python rag_system.py
```

Ask questions like:

```text
What is explained in the document?
```

---

## 2️⃣ Run AI Agent

```bash id="run-agent"
python agent_system.py
```

Try commands:

```text
Add event 2025-06-01|Meeting with client
Send email John|Hello|Project update
List calendar events
```

---

# 📊 Key Highlights

* 🧠 Dual AI system (RAG + Agent)
* 📄 Offline document intelligence
* 🤖 Tool-using AI assistant
* 🗄️ Local vector database (ChromaDB)
* ⚡ Fully local (no cloud dependency)
* 🔐 Privacy-friendly AI system
* 🧩 Modular LangChain architecture

---

# 🔮 Future Improvements

* 🌐 Web UI (Streamlit / FastAPI)
* 📅 Real calendar API integration (Google Calendar)
* 📧 Real email sending (SMTP integration)
* 🧠 Multi-document RAG system
* 🔐 User authentication system
* 📊 Admin dashboard
* 🤖 Multi-model routing (GPT + Claude + Ollama)

---

# 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

# 👨‍💻 Author

**Muhammad Abdullah Khan**


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps improve visibility and supports future development.
