import pickle
import os

class Memory:

    def __init__(self, path="memory_store/chat_history.pkl"):
        self.path = path

        if os.path.exists(self.path):
            self.load()
        else:
            self.data = {
                "chat_history": [],
                "city": None,
                "weather": None
            }
            self.save()

    # -------------------
    # SAVE / LOAD
    # -------------------

    def save(self):
        os.makedirs("memory_store", exist_ok=True)
        with open(self.path, "wb") as f:
            pickle.dump(self.data, f)

    def load(self):
        with open(self.path, "rb") as f:
            self.data = pickle.load(f)

    # -------------------
    # GET / SET
    # -------------------

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key):
        return self.data.get(key)

    # -------------------
    # CHAT HISTORY
    # -------------------

    def add_message(self, role, text):
        self.data["chat_history"].append({
            "role": role,
            "text": text
        })
        self.save()

    def get_history(self):
        return self.data["chat_history"]

    # -------------------
    # CLEAR
    # -------------------

    def clear(self):
        self.data = {
            "chat_history": [],
            "city": None,
            "weather": None
        }
        self.save()
