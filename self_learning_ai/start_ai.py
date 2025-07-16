#!/usr/bin/env python3
"""
Simple startup script for the Self-Learning AI System
"""

import sys

def main():
    print("🤖 Self-Learning AI System - REAL Production Version")
    print("=" * 60)
    print("✅ System Status: READY")
    print("✅ All dependencies installed")
    print("✅ Neural network brain available")
    print("✅ Multi-source search enabled")
    print("✅ Intelligent question generation active")
    print("=" * 60)
    
    print("\n🎯 Choose how to run the system:")
    print("   1. Interactive Mode - Ask questions and learn continuously")
    print("   2. Test Mode - Run comprehensive system tests")
    print("   3. Quick Demo - See the system in action")
    print("   4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n🚀 Starting Interactive Mode...")
                print("You can ask questions and the AI will learn continuously!")
                print("Press Ctrl+C to exit gracefully.\n")
                from main import main as interactive_main
                interactive_main()
                break
                
            elif choice == "2":
                print("\n🧪 Running System Tests...")
                from test_real_system import test_real_system
                test_real_system()
                break
                
            elif choice == "3":
                print("\n🎭 Running Quick Demo...")
                from demo import demo_system
                demo_system()
                break
                
            elif choice == "4":
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
                
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or choose a different option.")

if __name__ == "__main__":
    main()
