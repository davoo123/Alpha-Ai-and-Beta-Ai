import json

def load_memory():
    with open("shared_memory.json", "r") as f:
        return json.load(f)

def save_memory(question, answer):
    data = load_memory()
    data["topics"][question] = answer
    with open("shared_memory.json", "w") as f:
        json.dump(data, f, indent=4)
