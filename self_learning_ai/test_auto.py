#!/usr/bin/env python3
"""
Test the automatic learning system
"""

from auto_learning import AutoLearningSystem

def test_auto_learning():
    print("🧪 Testing Automatic Learning System")
    print("=" * 50)
    
    # Create the auto learning system
    auto_system = AutoLearningSystem()
    
    # Test with just 3 cycles to see it working
    print("🚀 Starting 3-cycle test...")
    auto_system.start_auto_learning(3)

if __name__ == "__main__":
    test_auto_learning()
