#!/usr/bin/env python3
"""
Production Launcher for Self-Learning AI System
Run this script to start the real AI system
"""

import sys
import os

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_imports = [
        ('torch', 'torch'),
        ('transformers', 'transformers'),
        ('sentence_transformers', 'sentence_transformers'),
        ('sklearn', 'scikit-learn'),
        ('requests', 'requests'),
        ('bs4', 'beautifulsoup4'),
        ('numpy', 'numpy'),
        ('pickle', 'pickle'),
        ('json', 'json'),
        ('re', 're')
    ]

    missing_packages = []
    for import_name, package_name in required_imports:
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)

    if missing_packages:
        print("❌ Missing required packages:")
        for pkg in missing_packages:
            print(f"   - {pkg}")
        print("\n📦 Install missing packages with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False

    return True

def show_system_info():
    """Display system information and capabilities"""
    print("🤖 Self-Learning AI System - Production Version")
    print("=" * 70)
    print("🎯 REAL FEATURES:")
    print("   ✅ Multi-source web search (Wikipedia, DuckDuckGo, Google)")
    print("   ✅ Advanced neural network with similarity matching")
    print("   ✅ Intelligent question generation with context analysis")
    print("   ✅ Persistent memory and continuous learning")
    print("   ✅ Two AI personalities (Alpha: Asker, Beta: Researcher)")
    print("   ✅ Comprehensive activity logging")
    print("   ✅ Graceful shutdown and session management")
    print("   ✅ Real-time brain training and prediction")
    print()
    print("🚀 CAPABILITIES:")
    print("   - Learns from every interaction")
    print("   - Generates intelligent follow-up questions")
    print("   - Searches multiple sources for accurate information")
    print("   - Builds and trains neural network from conversations")
    print("   - Maintains persistent knowledge across sessions")
    print("   - Provides similarity-based answer matching")
    print()
    print("💡 USAGE MODES:")
    print("   1. Interactive Mode: Ask questions and get continuous learning")
    print("   2. Auto Mode: Let AI generate and process questions automatically")
    print("   3. Manual Mode: Control each step of the learning process")
    print("=" * 70)

def main():
    """Main launcher function"""
    print("🔥 Starting REAL Self-Learning AI System...")
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Cannot start: Missing dependencies")
        sys.exit(1)
    
    # Show system information
    show_system_info()
    
    # Ask user for mode selection
    print("\n🎮 Select Mode:")
    print("   1. Full Interactive Mode (Recommended)")
    print("   2. Quick Test Mode")
    print("   3. System Information Only")
    
    try:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n🚀 Launching Full Interactive Mode...")
            from main import main as run_main
            run_main()
            
        elif choice == "2":
            print("\n🧪 Running Quick Test...")
            from test_real_system import test_real_system
            test_real_system()
            
        elif choice == "3":
            print("\n📊 System Information Displayed Above")
            
            # Show current knowledge base
            try:
                from shared_memory import load_memory
                from nn_brain import get_brain_stats
                
                memory = load_memory()
                stats = get_brain_stats()
                
                print(f"\n📚 Current Knowledge Base: {len(memory['topics'])} topics")
                print(f"🧠 Brain Status: {stats}")
                
                if memory['topics']:
                    print("\n📋 Recent Knowledge:")
                    for i, (q, a) in enumerate(list(memory['topics'].items())[-3:], 1):
                        print(f"   {i}. Q: {q}")
                        print(f"      A: {a[:80]}{'...' if len(a) > 80 else ''}")
                        
            except Exception as e:
                print(f"⚠️ Could not load system status: {e}")
                
        else:
            print("❌ Invalid choice. Exiting.")
            
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 Goodbye!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check your installation and try again.")

if __name__ == "__main__":
    main()
