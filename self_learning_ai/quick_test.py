#!/usr/bin/env python3
"""
Quick test to verify the system is working
"""

def quick_test():
    print("🔥 Quick System Test")
    print("=" * 40)
    
    # Test 1: Import all modules
    try:
        import torch
        import sklearn
        import sentence_transformers
        import bs4
        import requests
        import numpy
        print("✅ All dependencies imported successfully")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return
    
    # Test 2: Load our modules
    try:
        from nn_brain import get_brain_stats
        from search_module import search_web
        from question_generator import generate_questions_from_text
        from shared_memory import load_memory
        print("✅ All custom modules loaded successfully")
    except Exception as e:
        print(f"❌ Module loading error: {e}")
        return
    
    # Test 3: Check brain stats
    try:
        stats = get_brain_stats()
        print(f"✅ Brain stats: {stats}")
    except Exception as e:
        print(f"❌ Brain stats error: {e}")
    
    # Test 4: Check memory
    try:
        memory = load_memory()
        print(f"✅ Memory loaded: {len(memory['topics'])} topics")
    except Exception as e:
        print(f"❌ Memory error: {e}")
    
    # Test 5: Test question generation
    try:
        questions = generate_questions_from_text("Artificial intelligence is fascinating", 2)
        print(f"✅ Question generation: {questions}")
    except Exception as e:
        print(f"❌ Question generation error: {e}")
    
    print("\n🎉 System is ready!")
    print("\n🚀 To run the full system:")
    print("   python main.py")
    print("\n🧪 To run comprehensive tests:")
    print("   python test_real_system.py")

if __name__ == "__main__":
    quick_test()
