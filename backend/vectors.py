import chromadb
from sentence_transformers import SentenceTransformer

# add embedding function using sentenace transformer later
class VectorEngine():
    def __init__(self):
        self.transformer = SentenceTransformer('all-MiniLM-L6-v2')
        self.db = chromadb.PersistentClient(path='./chroma_db')
        self.collection = self.client.get_or_create_collection('messages')

    def append(self, message, metadata, id):
        self.collection.add(
            documents=[message],
            metadatas=[metadata],
            ids=[str(id)]
        )

    def compare(self, comparison_text, limit=5):
        return self.collection.query(
            query_texts=[comparison_text],
            limit=5
        )