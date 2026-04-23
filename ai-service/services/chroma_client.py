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
    embeddings = model.encode(docs)

    for i, doc in enumerate(docs):
        collection.add(
            documents=[doc],
            embeddings=[embeddings[i].tolist()],
            ids=[str(i)]
        )


# 🔹 Query similar documents
def query_documents(query_text):
    query_embedding = model.encode([query_text])[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    return results["documents"]