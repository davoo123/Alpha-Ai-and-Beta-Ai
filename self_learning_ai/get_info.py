#!/usr/bin/env python3
"""
Simple "get info" command - Automatic AI Learning
Just run this script and the two AI agents will start learning automatically
"""

from auto_learning import AutoLearningSystem

def get_info():
    """The main 'get info' command - starts automatic learning"""
    print("🎯 COMMAND: GET INFO")
    print("🤖 Starting automatic AI learning...")
    
    # Create and start the automatic learning system
    auto_system = AutoLearningSystem()
    auto_system.start_auto_learning(20)  # 20 learning cycles

if __name__ == "__main__":
    get_info()
