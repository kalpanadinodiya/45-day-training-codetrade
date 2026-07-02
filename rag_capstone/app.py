import os
import chromadb
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from config import GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel("gemini-2.5-flash")

folder = "Data"

documents = []

files = os.listdir(folder)

print("=" * 60)
print("READING DOCUMENTS")
print("=" * 60)

for file in files:

    path = os.path.join(folder, file)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    documents.append(text)

    print(f"{file}  -->  {len(text)} characters")

print("\n")
print("=" * 60)
print("SUMMARY")
print("=" * 60)

print("Total Documents:", len(documents))
print("Total Characters:", sum(len(doc) for doc in documents))

print("\n")
print("=" * 60)
print("CREATING EMBEDDINGS")
print("=" * 60)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents)

print("Embeddings created successfully!")
print("Number of embeddings:", len(embeddings))
print("Embedding dimension:", len(embeddings[0]))

print("\n")
print("=" * 60)
print("CREATING VECTOR DATABASE")
print("=" * 60)

# Create ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.get_or_create_collection(name="medical_documents")

# Store documents
for i in range(len(documents)):
    collection.add(
        documents=[documents[i]],
        embeddings=[embeddings[i].tolist()],
        ids=[str(i)]
    )

print("Vector Database Created Successfully!")
print("Documents Stored:", collection.count())

print("\n")
print("=" * 60)
print("SEMANTIC SEARCH")
print("=" * 60)

while True:

    query = input("Ask your question: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3
    )

    print("Question:")
    print(query)

    print("\nTop Matching Documents:\n")

    for i, doc in enumerate(results["documents"][0], start=1):
        print(f"Result {i}")
        print(doc[:500])
        print("-" * 60)
        print("\n")
    print("=" * 60)
    print("RAG ANSWER")
    print("=" * 60)

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY using the information provided in the context below.
    If the answer is not present in the context, reply:
    'I could not find the answer in the provided documents.'

    Context:
    {context}

    Question:
    {query}
    """

    response = gemini_model.generate_content(prompt)

    print(response.text)