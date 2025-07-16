#!/usr/bin/env python3
"""
Demo showing the AI system working with sample questions
"""

import time
from agent_alpha import alpha_talk
from shared_memory import load_memory, save_memory
from search_module import search_web
from question_generator import generate_questions_from_text

def demo_ai_working():
    print("🤖 Self-Learning AI System - LIVE DEMO")
    print("=" * 50)
    
    print("🔄 Loading AI models... (this may take a moment)")
    
    # Pre-populate some knowledge for faster demo
    print("📚 Initializing knowledge base...")
    initial_knowledge = {
        "What is Python?": "Python is a high-level programming language known for its simplicity and readability.",
        "What is machine learning?": "Machine learning is a subset of AI that enables computers to learn from data.",
        "What is neural network?": "A neural network is a computing system inspired by biological neural networks."
    }
    
    for q, a in initial_knowledge.items():
        save_memory(q, a)
    
    memory = load_memory()
    print(f"✅ Knowledge base ready: {len(memory['topics'])} topics")
    
    # Demo questions to show the system working
    demo_questions = [
        "What is Python?",  # Should use brain prediction
        "What is quantum computing?",  # Should trigger web search
        "Tell me about machine learning"  # Should use brain prediction
    ]
    
    print("\n🚀 Starting AI demonstration...")
    print("=" * 50)
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n🔄 Demo Question #{i}: {question}")
        print("-" * 40)
        
        try:
            start_time = time.time()
            answer, follow_ups = alpha_talk(question)
            process_time = time.time() - start_time
            
            print(f"💡 Answer: {answer}")
            print(f"⏱️ Processing time: {process_time:.2f} seconds")
            
            if follow_ups:
                print(f"❓ Generated follow-ups:")
                for j, follow_up in enumerate(follow_ups[:2], 1):
                    print(f"   {j}. {follow_up}")
            
            # Show knowledge growth
            updated_memory = load_memory()
            print(f"📚 Knowledge count: {len(updated_memory['topics'])} topics")
            
            time.sleep(1)  # Brief pause between questions
            
        except Exception as e:
            print(f"❌ Error processing question: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Demo completed!")
    
    final_memory = load_memory()
    print(f"📊 Final Statistics:")
    print(f"   - Total knowledge: {len(final_memory['topics'])} topics")
    print(f"   - Questions processed: {len(demo_questions)}")
    
    print(f"\n📋 Current Knowledge Base:")
    for i, (q, a) in enumerate(final_memory['topics'].items(), 1):
        print(f"   {i}. Q: {q}")
        print(f"      A: {a[:80]}{'...' if len(a) > 80 else ''}")
    
    print(f"\n🚀 System is ready for interactive use!")
    print(f"   Run: python main.py")

if __name__ == "__main__":
    demo_ai_working()
