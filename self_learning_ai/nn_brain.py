from sentence_transformers import SentenceTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import pickle
import os

# Initialize the sentence transformer model
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
clf = MLPClassifier(hidden_layer_sizes=(256, 128, 64), max_iter=1000, random_state=42)

# Cache for embeddings to speed up processing
embedding_cache = {}
model_file = "brain_model.pkl"

def load_training_data():
    """Load and prepare training data from shared memory"""
    with open("shared_memory.json") as f:
        data = json.load(f)

    X, y, questions = [], [], []
    for topic, answer in data["topics"].items():
        # Skip invalid entries
        if not topic or not answer or answer == "No result found.":
            continue

        # Use cached embedding if available
        if topic in embedding_cache:
            vec = embedding_cache[topic]
        else:
            vec = model.encode(topic)
            embedding_cache[topic] = vec

        X.append(vec)
        y.append(answer)
        questions.append(topic)

    return np.array(X), y, questions

def train_brain():
    """Train the neural network brain with current knowledge"""
    X, y, _ = load_training_data()

    if len(X) < 2:
        print("⚠️ Need at least 2 data points to train the brain.")
        return False

    try:
        # Train the classifier
        clf.fit(X, y)

        # Save the trained model
        with open(model_file, 'wb') as f:
            pickle.dump(clf, f)

        print(f"🧠 Neural brain trained with {len(X)} knowledge points.")
        return True

    except Exception as e:
        print(f"❌ Brain training failed: {e}")
        return False

def load_brain():
    """Load pre-trained brain model if available"""
    if os.path.exists(model_file):
        try:
            with open(model_file, 'rb') as f:
                global clf
                clf = pickle.load(f)
            print("🧠 Pre-trained brain model loaded.")
            return True
        except Exception as e:
            print(f"⚠️ Failed to load brain model: {e}")
    return False

def predict_answer(question):
    """Predict answer using neural network and similarity matching"""
    try:
        # Load brain if not already loaded
        if not hasattr(clf, 'classes_'):
            if not load_brain():
                raise Exception("Brain not trained yet")

        # Get question embedding
        question_vec = model.encode(question)

        # Try neural network prediction first
        try:
            predicted_answer = clf.predict([question_vec])[0]
            confidence = max(clf.predict_proba([question_vec])[0])

            # If confidence is high enough, return neural network prediction
            if confidence > 0.3:
                return predicted_answer
        except:
            pass

        # Fallback to similarity-based matching
        X, y, questions = load_training_data()
        if len(X) == 0:
            raise Exception("No training data available")

        # Calculate similarities
        similarities = cosine_similarity([question_vec], X)[0]
        best_match_idx = np.argmax(similarities)
        best_similarity = similarities[best_match_idx]

        # Return best match if similarity is high enough
        if best_similarity > 0.7:
            print(f"🎯 Found similar question: '{questions[best_match_idx]}' (similarity: {best_similarity:.2f})")
            return y[best_match_idx]

        # If no good match found, raise exception to trigger search
        raise Exception(f"No similar question found (best similarity: {best_similarity:.2f})")

    except Exception as e:
        print(f"🤔 Brain prediction failed: {e}")
        raise e

def get_brain_stats():
    """Get statistics about the brain's knowledge"""
    try:
        X, y, _ = load_training_data()
        return {
            "total_knowledge": len(X),
            "unique_answers": len(set(y)),
            "is_trained": hasattr(clf, 'classes_'),
            "model_exists": os.path.exists(model_file)
        }
    except:
        return {
            "total_knowledge": 0,
            "unique_answers": 0,
            "is_trained": False,
            "model_exists": False
        }
