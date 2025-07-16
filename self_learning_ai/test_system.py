#!/usr/bin/env python3
"""
Test script to demonstrate the self-learning AI system functionality
"""

import json
from shared_memory import load_memory, save_memory
from search_module import search_web
from nn_brain import train_brain, predict_answer
from question_generator import generate_questions_from_text
from logger import log_event
from agent_beta import beta_listen_and_reply

def test_system():
    print("🔬 Testing Self-Learning AI System")
    print("=" * 50)
    
    # Test 1: Memory system
    print("\n1. Testing Memory System...")
    save_memory("What is Python?", "Python is a high-level programming language")
    memory = load_memory()
    print(f"✅ Memory saved: {len(memory['topics'])} topics stored")
    
    # Test 2: Search module
    print("\n2. Testing Search Module...")
    try:
        result = search_web("Python programming language")
        print(f"✅ Search result: {result[:100]}...")
    except Exception as e:
        print(f"⚠️ Search test failed: {e}")
    
    # Test 3: Question generator
    print("\n3. Testing Question Generator...")
    questions = generate_questions_from_text("Python is a programming language", 2)
    print(f"✅ Generated questions: {questions}")
    
    # Test 4: Logger
    print("\n4. Testing Logger...")
    log_event("Test", "System Check", "All systems operational")
    print("✅ Logger working (check activity_log.txt)")
    
    # Test 5: Neural brain (after some data)
    print("\n5. Testing Neural Brain...")
    save_memory("What is AI?", "Artificial Intelligence is machine intelligence")
    save_memory("What is ML?", "Machine Learning is a subset of AI")
    try:
        train_brain()
        print("✅ Neural brain trained successfully")
    except Exception as e:
        print(f"⚠️ Neural brain needs more data: {e}")
    
    # Test 6: Agent Beta
    print("\n6. Testing Agent Beta...")
    try:
        answer, follow_ups = beta_listen_and_reply("What is machine learning?")
        print(f"✅ Agent Beta response: {answer[:100]}...")
        print(f"✅ Follow-up questions: {follow_ups}")
    except Exception as e:
        print(f"⚠️ Agent Beta test failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 System test completed!")
    print("📁 Check the following files:")
    print("   - shared_memory.json (for stored knowledge)")
    print("   - activity_log.txt (for system activity)")

if __name__ == "__main__":
    test_system()
