#!/usr/bin/env python3
"""
Advanced Random Question Generator for AI Training
Generates unique and diverse questions from various sources
"""

import random
import requests
from bs4 import BeautifulSoup
import time

class RandomQuestionGenerator:
    def __init__(self):
        # Comprehensive topic categories
        self.categories = {
            "science": ["physics", "chemistry", "biology", "astronomy", "geology", "meteorology"],
            "technology": ["artificial intelligence", "machine learning", "robotics", "quantum computing", "blockchain", "cybersecurity"],
            "medicine": ["anatomy", "pharmacology", "surgery", "genetics", "immunology", "neuroscience"],
            "history": ["ancient civilizations", "world wars", "renaissance", "industrial revolution", "cold war"],
            "geography": ["continents", "oceans", "mountains", "rivers", "countries", "capitals"],
            "arts": ["painting", "sculpture", "music", "literature", "theater", "cinema"],
            "sports": ["football", "basketball", "tennis", "swimming", "athletics", "gymnastics"],
            "nature": ["animals", "plants", "ecosystems", "climate", "evolution", "conservation"],
            "space": ["planets", "stars", "galaxies", "black holes", "space exploration", "satellites"],
            "culture": ["languages", "religions", "traditions", "festivals", "customs", "mythology"]
        }
        
        # Advanced question patterns
        self.question_patterns = [
            "What is the definition of {}?",
            "How does {} work?",
            "What are the main types of {}?",
            "What is the history behind {}?",
            "How is {} used in modern society?",
            "What are the benefits and drawbacks of {}?",
            "How has {} evolved over time?",
            "What are the key principles of {}?",
            "What role does {} play in {}?",
            "How do experts approach {}?",
            "What are common misconceptions about {}?",
            "What is the future of {}?",
            "How does {} compare to {}?",
            "What are the latest developments in {}?",
            "What skills are needed for {}?",
            "What tools are essential for {}?",
            "How does {} impact the environment?",
            "What are the ethical considerations of {}?",
            "How can someone learn {}?",
            "What are real-world applications of {}?"
        ]
        
        # Trending topics and current affairs
        self.trending_topics = [
            "climate change", "renewable energy", "electric vehicles", "space tourism",
            "gene therapy", "virtual reality", "augmented reality", "cryptocurrency",
            "sustainable development", "mental health", "remote work", "digital transformation",
            "5G technology", "Internet of Things", "smart cities", "precision medicine",
            "quantum internet", "brain-computer interfaces", "synthetic biology", "green technology"
        ]
        
        # Complex multi-part questions
        self.complex_patterns = [
            "How does {} relate to {} in the context of {}?",
            "What are the similarities and differences between {} and {}?",
            "How has {} influenced the development of {}?",
            "What would happen if {} was combined with {}?",
            "How do {} and {} work together to achieve {}?"
        ]
    
    def generate_simple_question(self):
        """Generate a simple random question"""
        category = random.choice(list(self.categories.keys()))
        topic = random.choice(self.categories[category])
        pattern = random.choice(self.question_patterns)
        return pattern.format(topic)
    
    def generate_trending_question(self):
        """Generate a question about trending topics"""
        topic = random.choice(self.trending_topics)
        pattern = random.choice(self.question_patterns)
        return pattern.format(topic)
    
    def generate_complex_question(self):
        """Generate a complex multi-part question"""
        try:
            pattern = random.choice(self.complex_patterns)
            
            # Get random topics from different categories
            cat1 = random.choice(list(self.categories.keys()))
            cat2 = random.choice(list(self.categories.keys()))
            
            topic1 = random.choice(self.categories[cat1])
            topic2 = random.choice(self.categories[cat2])
            
            if "{}" in pattern:
                placeholders = pattern.count("{}")
                if placeholders == 2:
                    return pattern.format(topic1, topic2)
                elif placeholders == 3:
                    topic3 = random.choice(self.trending_topics)
                    return pattern.format(topic1, topic2, topic3)
            
            return self.generate_simple_question()
            
        except:
            return self.generate_simple_question()
    
    def generate_wikipedia_random_question(self):
        """Generate a question based on Wikipedia's random article"""
        try:
            # Get a random Wikipedia article
            random_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
            headers = {"User-Agent": "RandomQuestionBot/1.0"}
            
            response = requests.get(random_url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                title = data.get('title', '')
                
                if title and len(title) > 2:
                    pattern = random.choice(self.question_patterns)
                    return pattern.format(title.lower())
            
        except Exception as e:
            print(f"Wikipedia random failed: {e}")
        
        return self.generate_simple_question()
    
    def generate_diverse_question(self):
        """Generate a diverse question using different methods"""
        methods = [
            self.generate_simple_question,
            self.generate_trending_question,
            self.generate_complex_question,
            self.generate_wikipedia_random_question
        ]
        
        # Weight the methods (simple questions more common)
        weights = [0.4, 0.3, 0.2, 0.1]
        method = random.choices(methods, weights=weights)[0]
        
        try:
            question = method()
            # Ensure question ends with ?
            if not question.endswith('?'):
                question += '?'
            return question.capitalize()
        except:
            return "What is artificial intelligence?"
    
    def generate_question_batch(self, count=5):
        """Generate a batch of diverse questions"""
        questions = []
        for _ in range(count):
            question = self.generate_diverse_question()
            if question not in questions:  # Avoid duplicates
                questions.append(question)
            time.sleep(0.1)  # Small delay to avoid rate limiting
        
        return questions
    
    def generate_educational_questions(self):
        """Generate educational questions across different difficulty levels"""
        levels = {
            "basic": [
                "What is {}?",
                "Where is {} located?",
                "When was {} invented?",
                "Who discovered {}?"
            ],
            "intermediate": [
                "How does {} function?",
                "What are the components of {}?",
                "How is {} measured?",
                "What causes {}?"
            ],
            "advanced": [
                "What are the theoretical implications of {}?",
                "How does {} challenge existing paradigms?",
                "What are the interdisciplinary connections of {}?",
                "How might {} evolve in the future?"
            ]
        }
        
        level = random.choice(list(levels.keys()))
        pattern = random.choice(levels[level])
        
        # Choose topic based on level
        if level == "basic":
            category = random.choice(list(self.categories.keys()))
            topic = random.choice(self.categories[category])
        else:
            topic = random.choice(self.trending_topics)
        
        return pattern.format(topic)

# Global instance for easy access
question_generator = RandomQuestionGenerator()

def get_random_question():
    """Get a single random question"""
    return question_generator.generate_diverse_question()

def get_random_questions(count=5):
    """Get multiple random questions"""
    return question_generator.generate_question_batch(count)

def get_educational_question():
    """Get an educational question"""
    return question_generator.generate_educational_questions()

if __name__ == "__main__":
    # Test the question generator
    print("🎲 Random Question Generator Test")
    print("=" * 40)
    
    for i in range(10):
        question = get_random_question()
        print(f"{i+1}. {question}")
        time.sleep(0.5)
