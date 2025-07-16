#!/usr/bin/env python3
"""
Self-Learning AI System - Production Version
Continuous learning system with two AI personalities
"""

import time
import signal
import sys
from agent_alpha import alpha_talk
from logger import log_event
from nn_brain import get_brain_stats, load_brain
from shared_memory import load_memory

class SelfLearningAI:
    def __init__(self):
        self.question_queue = []
        self.processed_count = 0
        self.running = True
        self.max_queue_size = 50  # Prevent infinite queue growth
        self.learning_session_count = 0

        # Setup signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, _sig, _frame):
        """Handle Ctrl+C gracefully"""
        print("\n\n🛑 Graceful shutdown initiated...")
        self.running = False
        self.show_session_summary()
        sys.exit(0)

    def show_startup_info(self):
        """Display system startup information"""
        print("🤖 Self-Learning AI System - Production Mode")
        print("=" * 60)

        # Load existing brain
        load_brain()

        # Show brain statistics
        stats = get_brain_stats()
        print(f"🧠 Brain Status:")
        print(f"   - Knowledge Points: {stats['total_knowledge']}")
        print(f"   - Unique Answers: {stats['unique_answers']}")
        print(f"   - Model Trained: {'✅' if stats['is_trained'] else '❌'}")
        print(f"   - Model File Exists: {'✅' if stats['model_exists'] else '❌'}")

        # Show memory contents
        memory = load_memory()
        print(f"\n📚 Current Knowledge Base: {len(memory['topics'])} topics")

        print("\n🎯 System Features:")
        print("   - Real T5 model for question generation")
        print("   - Multi-source web search (DuckDuckGo, Wikipedia, Google)")
        print("   - Advanced neural network with similarity matching")
        print("   - Persistent learning and memory")
        print("   - Continuous self-improvement")

        print("\n💡 Commands:")
        print("   - Type 'quit' or 'exit' to stop")
        print("   - Type 'stats' to see current statistics")
        print("   - Type 'memory' to see knowledge base")
        print("   - Press Ctrl+C for graceful shutdown")
        print("=" * 60)

    def show_session_summary(self):
        """Show summary of the learning session"""
        print("\n📊 Learning Session Summary")
        print("-" * 40)
        print(f"Questions Processed: {self.processed_count}")
        print(f"Learning Sessions: {self.learning_session_count}")

        stats = get_brain_stats()
        print(f"Final Knowledge Points: {stats['total_knowledge']}")
        print(f"Brain Training Status: {'✅ Trained' if stats['is_trained'] else '❌ Not Trained'}")

        memory = load_memory()
        print(f"Total Topics in Memory: {len(memory['topics'])}")
        print("\n🎉 Thank you for using Self-Learning AI!")

    def handle_special_commands(self, user_input):
        """Handle special user commands"""
        command = user_input.lower().strip()

        if command in ['quit', 'exit']:
            self.running = False
            return True

        elif command == 'stats':
            stats = get_brain_stats()
            print(f"\n📊 Current Statistics:")
            print(f"   - Processed Questions: {self.processed_count}")
            print(f"   - Queue Size: {len(self.question_queue)}")
            print(f"   - Knowledge Points: {stats['total_knowledge']}")
            print(f"   - Brain Trained: {'Yes' if stats['is_trained'] else 'No'}")
            return True

        elif command == 'memory':
            memory = load_memory()
            print(f"\n📚 Knowledge Base ({len(memory['topics'])} topics):")
            for i, (q, a) in enumerate(memory['topics'].items(), 1):
                print(f"   {i}. Q: {q}")
                print(f"      A: {a[:100]}{'...' if len(a) > 100 else ''}")
            return True

        return False

    def process_question(self, question):
        """Process a single question through the AI system"""
        try:
            self.processed_count += 1
            print(f"\n🔄 Processing Question #{self.processed_count}: {question}")
            print("-" * 50)

            log_event("System", "Processing", f"Question #{self.processed_count}: {question}")

            # Get answer and follow-up questions from Alpha agent
            answer, follow_ups = alpha_talk(question)

            print(f"💡 Answer: {answer}")

            if follow_ups:
                print(f"❓ Generated {len(follow_ups)} follow-up questions:")
                for i, follow_up in enumerate(follow_ups, 1):
                    print(f"   {i}. {follow_up}")

                    # Add to queue if not too full
                    if len(self.question_queue) < self.max_queue_size:
                        self.question_queue.append(follow_up)
                        log_event("System", "Queued", follow_up)

            self.learning_session_count += 1

        except Exception as e:
            print(f"❌ Error processing question: {e}")
            log_event("System", "Error", f"Failed to process: {question} - {e}")

    def run(self):
        """Main execution loop"""
        self.show_startup_info()

        # Get initial question from user
        while self.running:
            try:
                user_input = input("\n🧠 Ask a question (or 'quit' to exit):\n> ").strip()

                if not user_input:
                    continue

                # Handle special commands
                if self.handle_special_commands(user_input):
                    continue

                # Add user question to queue
                self.question_queue.append(user_input)
                break

            except (EOFError, KeyboardInterrupt):
                self.running = False
                break

        # Process questions from queue
        while self.running and self.question_queue:
            try:
                current_question = self.question_queue.pop(0)
                self.process_question(current_question)

                # Show queue status
                if self.question_queue:
                    print(f"\n📋 Queue Status: {len(self.question_queue)} questions remaining")

                    # Ask user if they want to continue with auto-processing
                    if self.processed_count == 1:  # First question processed
                        choice = input("\n🤔 Continue auto-processing queue? (y/n/manual): ").lower().strip()
                        if choice == 'n':
                            break
                        elif choice == 'manual':
                            # Manual mode - ask before each question
                            while self.question_queue and self.running:
                                next_q = self.question_queue[0]
                                choice = input(f"\n➡️ Process next question: '{next_q}'? (y/n/quit): ").lower().strip()
                                if choice == 'y':
                                    self.question_queue.pop(0)
                                    self.process_question(next_q)
                                elif choice == 'quit':
                                    self.running = False
                                    break
                                else:
                                    break
                            break

                    # Small delay between auto-processing
                    time.sleep(1)
                else:
                    print("\n✅ All questions processed!")

                    # Ask if user wants to add more questions
                    while self.running:
                        user_input = input("\n🧠 Ask another question (or 'quit' to exit):\n> ").strip()

                        if not user_input:
                            continue

                        if self.handle_special_commands(user_input):
                            break

                        self.question_queue.append(user_input)
                        break

            except (EOFError, KeyboardInterrupt):
                self.running = False
                break

        if self.running:
            self.show_session_summary()

def main():
    """Main entry point"""
    ai_system = SelfLearningAI()
    ai_system.run()

if __name__ == "__main__":
    main()
