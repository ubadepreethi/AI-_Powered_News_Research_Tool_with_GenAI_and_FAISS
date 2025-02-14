import os
import streamlit as st
import pickle
import time 
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceEmbeddings  
from dotenv import load_dotenv

# Load environment variables from env.txt
load_dotenv("env.txt")
# Retrieve Google API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Missing Google API Key. Make sure it's in env.txt.")

# Configure Google Gemini API
genai.configure(api_key=api_key)

# Streamlit UI
st.title("📢 News Research Tool with AI")
st.sidebar.title("🔗 Enter News URLs")

# Get user input URLs
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
urls = [url for url in urls if url]  # Remove empty inputs

process_url_clicked = st.sidebar.button("🚀 Process URLs")
file_path = "faiss_store_google.pkl"
main_placeholder = st.empty()

if process_url_clicked and urls:
    try:
        # Load data
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("📡 Loading data from URLs...")
        data = loader.load()

        # Split data
        text_splitter = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '.', ','], chunk_size=1000)
        main_placeholder.text("✂ Splitting text into chunks...")
        docs = text_splitter.split_documents(data)

        # Create embeddings and save to FAISS index
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore_google = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("🧠 Creating embeddings and storing them...✅")
        time.sleep(2)

        # Save FAISS index
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore_google, f)

        st.sidebar.success("✅ Data processed successfully!")

    except Exception as e:
        st.sidebar.error(f"❌ Error: {str(e)}")

# Question input and retrieval
query = st.text_input("💬 Ask a Question:")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)

        retriever = vectorstore.as_retriever()
        retrieved_docs = retriever.get_relevant_documents(query)

        # ✅ Fix: Convert retrieved_docs to plain text
        retrieved_text = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Generate response using Google Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Answer this based on the following context:\n\n{retrieved_text}")

        st.header("📝 Answer")
        st.write(response.text)
