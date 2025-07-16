#!/usr/bin/env python3
"""
Fast startup version of the Self-Learning AI System
"""

import time
from agent_alpha import alpha_talk
from shared_memory import load_memory
from logger import log_event

def run_ai_now():
    print("🤖 Self-Learning AI System - RUNNING NOW!")
    print("=" * 50)
    
    # Show current knowledge
    memory = load_memory()
    print(f"📚 Current Knowledge: {len(memory['topics'])} topics")
    
    print("\n🎯 System Features:")
    print("   ✅ Multi-source web search")
    print("   ✅ Neural network learning")
    print("   ✅ Intelligent question generation")
    print("   ✅ Persistent memory")
    
    print("\n🚀 Ready to learn! Ask me anything...")
    print("(Type 'quit' to exit)")
    print("=" * 50)
    
    question_count = 0
    
    while True:
        try:
            # Get user question
            question = input(f"\n🧠 Question #{question_count + 1}: ").strip()
            
            if not question:
                continue
                
            if question.lower() in ['quit', 'exit', 'stop']:
                print("\n👋 Thanks for using the AI system!")
                break
            
            question_count += 1
            print(f"\n🔄 Processing: {question}")
            print("-" * 30)
            
            # Process the question
            start_time = time.time()
            answer, follow_ups = alpha_talk(question)
            process_time = time.time() - start_time
            
            print(f"💡 Answer: {answer}")
            print(f"⏱️ Processing time: {process_time:.2f} seconds")
            
            if follow_ups:
                print(f"\n❓ Generated {len(follow_ups)} follow-up questions:")
                for i, follow_up in enumerate(follow_ups, 1):
                    print(f"   {i}. {follow_up}")
            
            # Show updated knowledge count
            updated_memory = load_memory()
            if len(updated_memory['topics']) > len(memory['topics']):
                print(f"📚 Knowledge updated! Now have {len(updated_memory['topics'])} topics")
                memory = updated_memory
            
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down gracefully...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try another question.")
    
    print(f"\n📊 Session Summary:")
    print(f"   - Questions processed: {question_count}")
    print(f"   - Total knowledge: {len(load_memory()['topics'])} topics")
    print(f"   - Activity logged to: activity_log.txt")
    print("\n🎉 AI system session completed!")

if __name__ == "__main__":
    run_ai_now()
