from chromadb.config import Settings
import chromadb


class ChromaClient:
    def __init__(self):
        # ✅ Persistent DB (auto handled)
        self.client = chromadb.Client(
            Settings(
                persist_directory="chroma_db"
            )
        )

        # ✅ Create/Get collection
        self.collection = self.client.get_or_create_collection(
            name="fraud_collection"
        )

    # ✅ Add data
    def add_data(self, texts):
        for i, text in enumerate(texts):
            self.collection.add(
                documents=[text],
                ids=[str(i)]
            )

    # ✅ Query data
    def query(self, query_text):
        results = self.collection.query(
            query_texts=[query_text],
            n_results=2
        )

        return results["documents"]