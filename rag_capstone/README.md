# RAG Capstone Project

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using Gemini, Sentence Transformers, and ChromaDB. The system retrieves the most relevant documents from a knowledge base using semantic search and then uses Google's Gemini model to generate accurate answers based on the retrieved context.

---

## Features

- Load multiple text documents
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Perform semantic similarity search
- Generate answers using Gemini
- Interactive chatbot using terminal input

---

## Technologies Used

- Python
- Google Gemini API
- Sentence Transformers
- ChromaDB
- python-dotenv

---

## Project Structure

```
rag_capstone/
│── Data/
│   ├── AuraHealth_Dietary_Standards.txt
│   ├── AuraHealth_Employee_Handbook_2026.txt
│   ├── ...
│
│── app.py
│── config.py
│── .env
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/kalpanadinodiya/45-day-training-codetrade.git
```

Go to the project folder

```bash
cd rag_capstone
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key.

```
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Project

```bash
python app.py
```

---

## Workflow

1. Load documents from the Data folder.
2. Generate embeddings using Sentence Transformers.
3. Store embeddings in ChromaDB.
4. Accept a user query.
5. Retrieve the most relevant documents.
6. Send the retrieved context to Gemini.
7. Display the generated answer.

---

## Sample Output

```
Ask your question:
Who is the Head of OmniHeal?

Answer:
Dr. Elena Rostova has officially taken the helm as the Chief Director of the OmniHeal Initiative.
```

---

## Future Improvements

- Web interface using Streamlit
- Persistent vector database
- PDF document support
- Conversation history
- Multiple LLM support

---

## Author

**Kalpana Dinodiya**

B.Tech Computer Science