from sentence_transformers import SentenceTransformer
import chromadb

# 🔹 Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔹 Initialize DB
client = chromadb.Client()

# 🔹 Create collection
collection = client.get_or_create_collection(name="fraud_docs")


# 🔹 Add documents to DB
def add_documents(docs):
    all_chunks = []
    ids = []

    for i, doc in enumerate(docs):
        chunks = chunk_text(doc)
        for j, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            ids.append(f"{i}_{j}")

    if not all_chunks:
        return

    embeddings = model.encode(all_chunks)

    collection.add(
        documents=all_chunks,
        embeddings=[e.tolist() for e in embeddings],
        ids=ids
    )
    print("Total chunks created:", len(all_chunks))

# 🔹 Query similar documents
def query_documents(query_text):
    query_embedding = model.encode([query_text])[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    return results["documents"]

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks