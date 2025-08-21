import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

PDF_PATH = r"C:\Users\Abdullah\OneDrive\Desktop\LangChain\manual.pdf"   
CHROMA_DIR = "chroma_ollama"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K = 4


EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama2"

loader = PyPDFLoader(PDF_PATH)
docs = loader.load()
print(f"[+] Loaded {len(docs)} pages.")

splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
chunks = splitter.split_documents(docs)
print(f"[+] Split into {len(chunks)} chunks.")

embeddings = OllamaEmbeddings(model=EMBED_MODEL)
print(f"[+] Using Ollama embeddings model: {EMBED_MODEL}")

vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_DIR)
vectordb.persist()
retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": TOP_K})
print("[+] Vectorstore ready.")

llm = ChatOllama(model=LLM_MODEL, temperature=0.2, max_tokens=512)
print(f"[+] Using Ollama LLM: {LLM_MODEL}")


prompt_template = """You are an assistant that answers questions using ONLY the provided context.
If answer is not in the context, reply "I don't know".
Context:
{context}

Question: {question}
Answer:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)

print("\n--- Internal Knowledgebase (Ollama RAG) ---")
while True:
    q = input("\n❓ Ask: ")
    if q.lower() in ("exit", "quit"):
        break
    resp = qa_chain.invoke(q)
    print("💡 Answer:", resp)
