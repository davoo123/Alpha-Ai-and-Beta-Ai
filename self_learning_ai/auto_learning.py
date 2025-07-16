#!/usr/bin/env python3
"""
Automatic Self-Learning System - Two AI agents train each other automatically
Command: "get info" - Starts automatic learning between Alpha and Beta
"""

import random
import time
import threading
from search_module import search_web
from shared_memory import save_memory, load_memory
from nn_brain import train_brain, get_brain_stats
from question_generator import generate_questions_from_text
from random_question_generator import get_random_question, get_random_questions
from logger import log_event

class AutoLearningSystem:
    def __init__(self):
        self.running = False
        self.learning_cycles = 0
        self.max_cycles = 50  # Prevent infinite running
        self.question_pool = []
        self.current_turn = "Alpha"  # Alpha starts first
        
        # Random question categories for diverse learning
        self.question_categories = [
            "science", "technology", "history", "geography", "biology",
            "physics", "chemistry", "mathematics", "psychology", "philosophy",
            "economics", "politics", "art", "music", "literature",
            "medicine", "engineering", "astronomy", "ecology", "sociology"
        ]
        
        # Question templates for generating diverse questions
        self.question_templates = [
            "What is {}?",
            "How does {} work?",
            "What are the benefits of {}?",
            "What is the history of {}?",
            "How is {} used in modern times?",
            "What are the types of {}?",
            "What are the challenges in {}?",
            "How has {} evolved?",
            "What is the future of {}?",
            "What are examples of {}?",
            "How do you learn {}?",
            "What tools are used for {}?",
            "What are the principles of {}?",
            "How does {} impact society?",
            "What research is being done on {}?"
        ]
    
    def generate_random_question(self):
        """Generate a random question using advanced question generator"""
        try:
            # Use the advanced random question generator
            question = get_random_question()
            log_event("System", "Generated", f"Random question: {question}")
            return question

        except Exception as e:
            log_event("System", "Error", f"Failed to generate random question: {e}")
            return "What is artificial intelligence?"
    
    def alpha_ask_question(self):
        """Alpha agent asks a question"""
        try:
            # Generate or pick a question
            if self.question_pool:
                question = self.question_pool.pop(0)
                log_event("Alpha", "Asking from pool", question)
            else:
                question = self.generate_random_question()
                log_event("Alpha", "Generated question", question)
            
            print(f"\n🔵 ALPHA ASKS: {question}")
            return question
            
        except Exception as e:
            log_event("Alpha", "Error", f"Failed to ask question: {e}")
            return self.generate_random_question()
    
    def beta_answer_question(self, question):
        """Beta agent answers the question by searching"""
        try:
            log_event("Beta", "Researching", question)
            print(f"🔴 BETA RESEARCHING: {question}")
            
            # Search for the answer
            answer = search_web(question)
            
            # Save to memory
            save_memory(question, answer)
            log_event("Beta", "Learned", f"Q: {question} | A: {answer[:100]}...")
            
            print(f"🔴 BETA FOUND: {answer[:200]}...")
            
            # Generate follow-up questions
            follow_ups = generate_questions_from_text(answer, 2)
            for follow_up in follow_ups:
                self.question_pool.append(follow_up)
                log_event("Beta", "Generated follow-up", follow_up)
            
            print(f"🔴 BETA GENERATED {len(follow_ups)} follow-up questions")
            
            return answer, follow_ups
            
        except Exception as e:
            log_event("Beta", "Error", f"Failed to answer question: {e}")
            return "Unable to find information", []
    
    def beta_ask_question(self):
        """Beta agent asks a question"""
        try:
            # Generate or pick a question
            if self.question_pool:
                question = self.question_pool.pop(0)
                log_event("Beta", "Asking from pool", question)
            else:
                question = self.generate_random_question()
                log_event("Beta", "Generated question", question)
            
            print(f"\n🔴 BETA ASKS: {question}")
            return question
            
        except Exception as e:
            log_event("Beta", "Error", f"Failed to ask question: {e}")
            return self.generate_random_question()
    
    def alpha_answer_question(self, question):
        """Alpha agent answers the question by searching"""
        try:
            log_event("Alpha", "Researching", question)
            print(f"🔵 ALPHA RESEARCHING: {question}")
            
            # Search for the answer
            answer = search_web(question)
            
            # Save to memory
            save_memory(question, answer)
            log_event("Alpha", "Learned", f"Q: {question} | A: {answer[:100]}...")
            
            print(f"🔵 ALPHA FOUND: {answer[:200]}...")
            
            # Generate follow-up questions
            follow_ups = generate_questions_from_text(answer, 2)
            for follow_up in follow_ups:
                self.question_pool.append(follow_up)
                log_event("Alpha", "Generated follow-up", follow_up)
            
            print(f"🔵 ALPHA GENERATED {len(follow_ups)} follow-up questions")
            
            return answer, follow_ups
            
        except Exception as e:
            log_event("Alpha", "Error", f"Failed to answer question: {e}")
            return "Unable to find information", []
    
    def learning_cycle(self):
        """One complete learning cycle between Alpha and Beta"""
        try:
            self.learning_cycles += 1
            print(f"\n{'='*60}")
            print(f"🔄 LEARNING CYCLE #{self.learning_cycles}")
            print(f"{'='*60}")
            
            if self.current_turn == "Alpha":
                # Alpha asks, Beta answers
                question = self.alpha_ask_question()
                time.sleep(1)  # Brief pause for readability
                answer, follow_ups = self.beta_answer_question(question)
                self.current_turn = "Beta"  # Switch turn
                
            else:
                # Beta asks, Alpha answers
                question = self.beta_ask_question()
                time.sleep(1)  # Brief pause for readability
                answer, follow_ups = self.alpha_answer_question(question)
                self.current_turn = "Alpha"  # Switch turn
            
            # Train the brain with new knowledge
            print(f"🧠 TRAINING BRAIN...")
            train_brain()
            
            # Show current statistics
            stats = get_brain_stats()
            memory = load_memory()
            print(f"📊 STATS: {len(memory['topics'])} topics | Brain: {'Trained' if stats['is_trained'] else 'Learning'}")
            print(f"📋 QUEUE: {len(self.question_pool)} questions waiting")
            
            time.sleep(2)  # Pause between cycles
            
        except Exception as e:
            log_event("System", "Error", f"Learning cycle failed: {e}")
            print(f"❌ Cycle error: {e}")
    
    def start_auto_learning(self, cycles=None):
        """Start the automatic learning process"""
        self.running = True
        target_cycles = cycles or self.max_cycles
        
        print("🚀 STARTING AUTOMATIC AI LEARNING")
        print("=" * 60)
        print("🔵 Agent Alpha: Asker & Researcher")
        print("🔴 Agent Beta: Researcher & Asker")
        print(f"🎯 Target: {target_cycles} learning cycles")
        print("🔄 Agents will switch roles automatically")
        print("=" * 60)
        
        # Initialize with diverse random questions
        print("🎲 Generating initial random questions...")
        initial_questions = get_random_questions(10)  # Get 10 diverse questions
        self.question_pool.extend(initial_questions)

        print(f"📋 Initial question pool:")
        for i, q in enumerate(initial_questions[:5], 1):
            print(f"   {i}. {q}")
        if len(initial_questions) > 5:
            print(f"   ... and {len(initial_questions) - 5} more questions")
        
        log_event("System", "Started", f"Auto-learning with {target_cycles} cycles")
        
        try:
            while self.running and self.learning_cycles < target_cycles:
                self.learning_cycle()
                
                # Check if we should continue
                if self.learning_cycles % 10 == 0:
                    print(f"\n⏸️ Completed {self.learning_cycles} cycles. Continue? (y/n/stop): ", end="")
                    # For automatic mode, just continue
                    print("y (auto-continuing)")
                    
        except KeyboardInterrupt:
            print("\n\n🛑 Learning interrupted by user")
            self.running = False
        except Exception as e:
            print(f"\n❌ Learning stopped due to error: {e}")
            self.running = False
        
        self.show_final_results()
    
    def show_final_results(self):
        """Show final learning results"""
        print("\n" + "=" * 60)
        print("🎉 AUTOMATIC LEARNING COMPLETED")
        print("=" * 60)
        
        memory = load_memory()
        stats = get_brain_stats()
        
        print(f"📊 Final Statistics:")
        print(f"   - Learning Cycles: {self.learning_cycles}")
        print(f"   - Total Knowledge: {len(memory['topics'])} topics")
        print(f"   - Brain Status: {'✅ Trained' if stats['is_trained'] else '❌ Not Trained'}")
        print(f"   - Questions in Queue: {len(self.question_pool)}")
        
        print(f"\n📚 Recent Knowledge Acquired:")
        recent_topics = list(memory['topics'].items())[-5:]
        for i, (q, a) in enumerate(recent_topics, 1):
            print(f"   {i}. Q: {q}")
            print(f"      A: {a[:100]}{'...' if len(a) > 100 else ''}")
        
        log_event("System", "Completed", f"Auto-learning finished with {self.learning_cycles} cycles")

def get_info(cycles=20):
    """Main command function - starts automatic learning"""
    print("🎯 COMMAND RECEIVED: GET INFO")
    print("🤖 Initializing automatic AI learning system...")
    
    auto_system = AutoLearningSystem()
    auto_system.start_auto_learning(cycles)

if __name__ == "__main__":
    # Command interface
    print("🤖 Automatic AI Learning System")
    print("Commands:")
    print("  'get info' - Start automatic learning")
    print("  'get info 30' - Start with 30 cycles")
    print("  'quit' - Exit")
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command == "get info":
                get_info(20)
            elif command.startswith("get info "):
                try:
                    cycles = int(command.split()[-1])
                    get_info(cycles)
                except:
                    print("❌ Invalid number. Using default 20 cycles.")
                    get_info(20)
            elif command in ["quit", "exit"]:
                print("👋 Goodbye!")
                break
            else:
                print("❌ Unknown command. Use 'get info' or 'quit'")
                
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            break
