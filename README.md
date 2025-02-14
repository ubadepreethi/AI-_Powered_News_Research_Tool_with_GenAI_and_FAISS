# 📢 AI-Powered News Research Tool

## 🚀 Overview
This project is an **AI-powered news research tool** that allows users to extract, process, and retrieve key insights from online news articles. By leveraging **Google Gemini API, FAISS, and LangChain**, the tool provides **fast and accurate responses** to user queries based on extracted news content.

## 🛠 Tech Stack
- **Google Gemini API** – AI-powered content generation
- **FAISS (Facebook AI Similarity Search)** – Efficient similarity-based retrieval
- **LangChain** – Text processing & embeddings
- **Sentence-Transformers** – Contextual embeddings for better search
- **Streamlit** – Interactive web-based UI

## 🌟 Features
✅ Load article content via URLs or upload text files
✅ Extract key information using **LangChain's UnstructuredURLLoader**
✅ Generate embeddings using **Hugging Face Sentence-Transformers**
✅ Store and index embeddings using **FAISS** for quick retrieval
✅ Query a **Large Language Model (LLM)** to get answers from extracted content
✅ Display source URLs for transparency

## 🎯 Usage
1. Run the **Streamlit** application:
   ```sh
   streamlit run main.py
   ```
2. The web app will open in your browser.
3. Enter **news URLs** in the sidebar.
4. Click **"Process URLs"** to extract and store key insights.
5. Once processing is done, enter a **query** to retrieve insights from the articles.
6. View AI-generated responses along with **source links**.

## 🔗 Example URLs Used
For testing, the following articles were processed:
- [Tata Motors, Mahindra gain certificates for production-linked payouts](https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html)
- [Tata Motors launches Punch iCNG, price starts at Rs 7.1 lakh](https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html)
- [Buy Tata Motors, target of Rs 743: KR Choksey](https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html)

## 📁 Project Structure
```
📂 news-research-tool
├── 📜 main.py                 # Main Streamlit application
├── 📜 requirements.txt        # Python dependencies
├── 📜 .env                    # API Key configuration
├── 📜 faiss_store_google.pkl  # FAISS index storage
```

## 🎯 Future Enhancements
🚀 Add multi-language support for international news processing.
🚀 Improve AI summarization for better article insights.
🚀 Expand the dataset to support **more news sources**.

## 🙌 Special Thanks
A special thanks to **Omkar Sir** for guidance and support throughout this project! 🙏

## 📢 Connect
If you found this project useful, feel free to **like, share, and contribute**! 💡

