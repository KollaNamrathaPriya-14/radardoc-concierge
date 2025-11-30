import time
import uuid

class MemoryBank:
    def __init__(self):
        # Simple in-memory store: session_id -> list of documents
        self.store = {}

    def save_document(self, session_id, doc_meta):
        entry = {
            "id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "doc": doc_meta
        }
        self.store.setdefault(session_id, []).append(entry)
        return entry["id"]

    def retrieve_recent(self, session_id, n=3):
        return self.store.get(session_id, [])[-n:]

    def list_documents(self, session_id):
        return self.store.get(session_id, [])
