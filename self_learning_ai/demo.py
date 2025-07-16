#!/usr/bin/env python3
"""
Demo script to showcase the self-learning AI system
"""

from agent_alpha import alpha_talk
from shared_memory import load_memory, save_memory
from logger import log_event
import json

def demo_system():
    print("🎭 Self-Learning AI System Demo")
    print("=" * 60)
    
    # Pre-populate some knowledge
    print("\n📚 Pre-populating knowledge base...")
    knowledge_base = {
        "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "What is machine learning?": "Machine learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed.",
        "What is neural network?": "A neural network is a computing system inspired by biological neural networks that can learn patterns in data.",
        "What is deep learning?": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to model complex patterns."
    }
    
    for question, answer in knowledge_base.items():
        save_memory(question, answer)
    
    memory = load_memory()
    print(f"✅ Knowledge base initialized with {len(memory['topics'])} topics")
    
    # Demo questions to process
    demo_questions = [
        "What is artificial intelligence?",
        "What is Python?",  # This should be predicted from memory
        "How does machine learning work?"
    ]
    
    print("\n🤖 Starting AI conversation simulation...")
    print("-" * 60)
    
    question_queue = demo_questions.copy()
    processed_count = 0
    max_questions = 8  # Limit to prevent infinite loop in demo
    
    while question_queue and processed_count < max_questions:
        current_question = question_queue.pop(0)
        processed_count += 1
        
        print(f"\n🔄 Processing Question #{processed_count}: {current_question}")
        print("-" * 40)
        
        try:
            answer, follow_ups = alpha_talk(current_question)
            
            print(f"💡 Answer: {answer}")
            print(f"❓ Generated {len(follow_ups)} follow-up questions:")
            
            for i, follow_up in enumerate(follow_ups, 1):
                print(f"   {i}. {follow_up}")
                # Add some follow-ups to queue (limit to prevent explosion)
                if len(question_queue) < 3:
                    question_queue.append(follow_up)
            
        except Exception as e:
            print(f"❌ Error processing question: {e}")
        
        print(f"\n📊 Queue status: {len(question_queue)} questions remaining")
    
    # Show final statistics
    print("\n" + "=" * 60)
    print("📈 Final System Statistics")
    print("=" * 60)
    
    final_memory = load_memory()
    print(f"🧠 Total knowledge stored: {len(final_memory['topics'])} topics")
    print(f"🔄 Questions processed: {processed_count}")
    
    print("\n📋 Knowledge Base Contents:")
    for i, (question, answer) in enumerate(final_memory['topics'].items(), 1):
        print(f"   {i}. Q: {question}")
        print(f"      A: {answer[:80]}{'...' if len(answer) > 80 else ''}")
    
    print(f"\n📁 Check these files for more details:")
    print(f"   - shared_memory.json (knowledge storage)")
    print(f"   - activity_log.txt (system activity log)")
    
    print("\n🎉 Demo completed! The system is ready for continuous learning.")

if __name__ == "__main__":
    demo_system()
