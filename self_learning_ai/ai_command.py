#!/usr/bin/env python3
"""
AI Command Interface - Simple command to start automatic learning
Usage: Just type "get info" and the two AI agents will start training each other
"""

import sys
from auto_learning import get_info

def main():
    print("🤖 AI Command Interface")
    print("=" * 40)
    print("💡 Available Commands:")
    print("   'get info' - Start automatic AI learning")
    print("   'get info 50' - Start with 50 learning cycles")
    print("   'quit' - Exit")
    print("=" * 40)
    
    while True:
        try:
            command = input("\n🎯 Enter command: ").strip().lower()
            
            if command == "get info":
                print("\n🚀 Starting automatic AI learning...")
                get_info(25)  # Default 25 cycles
                
            elif command.startswith("get info "):
                try:
                    parts = command.split()
                    if len(parts) >= 3 and parts[2].isdigit():
                        cycles = int(parts[2])
                        print(f"\n🚀 Starting automatic AI learning with {cycles} cycles...")
                        get_info(cycles)
                    else:
                        print("❌ Invalid format. Use: get info [number]")
                except:
                    print("❌ Invalid number. Using default 25 cycles.")
                    get_info(25)
                    
            elif command in ["quit", "exit", "stop"]:
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Unknown command. Use 'get info' or 'quit'")
                
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
