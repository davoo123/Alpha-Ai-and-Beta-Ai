# 🤖 Self-Learning AI System - PRODUCTION VERSION

A **REAL** Python-based self-learning AI system with advanced neural networks, multi-source web search, and intelligent question generation for continuous knowledge building.

## 🚀 REAL FEATURES (Not Demo!)

### 🔹 Two AI Personalities
- **Agent Alpha**: Asker personality (curious & logical)
- **Agent Beta**: Researcher personality (knowledge seeker & web searcher)

### 🔹 Advanced Core Components
- **Enhanced Neural Brain**: Sentence-transformers + MLPClassifier with similarity matching
- **Multi-Source Search**: Wikipedia API, DuckDuckGo, and Google fallback
- **Intelligent Question Generator**: Context-aware question generation with key term extraction
- **Persistent Memory**: JSON-based knowledge storage with caching
- **Advanced Logging**: Comprehensive activity tracking and session management
- **Production-Ready**: Graceful shutdown, error handling, and performance optimization

## 📁 Project Structure

```
self_learning_ai/
├── main.py                 # Main application with infinity loop
├── agent_alpha.py          # Asker personality agent
├── agent_beta.py           # Researcher personality agent
├── ai_communicator.py      # Communication handler between agents
├── shared_memory.json      # Knowledge storage (auto-generated)
├── shared_memory.py        # Memory management functions
├── nn_brain.py            # Neural network brain for predictions
├── search_module.py       # Web search functionality
├── question_generator.py  # Follow-up question generation
├── logger.py              # Activity logging system
├── activity_log.txt       # Activity log (auto-generated)
├── test_system.py         # System testing script
└── README.md              # This file
```

## 🚀 Installation

1. **Install Required Dependencies:**
```bash
pip install torch transformers sentence-transformers scikit-learn requests beautifulsoup4 tiktoken protobuf sentencepiece
```

2. **Navigate to the project directory:**
```bash
cd self_learning_ai
```

## 🎯 Usage

### 🔥 Quick Start (Recommended)
```bash
python run_ai.py
```

### 🎮 Alternative Launch Methods
```bash
# Full interactive mode
python main.py

# Test real system capabilities
python test_real_system.py

# Legacy demo (basic features)
python demo.py
```

## 🔄 How It Works

1. **User Input**: System starts with a user-provided question
2. **Agent Alpha**: Processes the question and forwards to AI Communicator
3. **Neural Brain**: Attempts to predict answer from stored knowledge
4. **Agent Beta**: If brain doesn't know, searches web for information
5. **Memory Update**: Stores new question-answer pairs in shared memory
6. **Brain Training**: Retrains neural network with new data
7. **Question Generation**: Creates follow-up questions from the answer
8. **Queue Management**: Adds new questions to processing queue
9. **Infinity Loop**: Continues processing until queue is empty

## 📊 System Components

### Agent Alpha (Asker)
- Curious and logical personality
- Processes incoming questions
- Logs all asking activities

### Agent Beta (Researcher)
- Knowledge-seeking personality
- Performs web searches
- Generates follow-up questions
- Updates shared memory

### Neural Network Brain
- Uses sentence-transformers for text encoding
- MLPClassifier for answer prediction
- Trains on accumulated knowledge
- Provides instant answers for known topics

### Shared Memory System
- JSON-based storage format
- Persistent knowledge retention
- Easy data access and updates

### Activity Logger
- Timestamps all activities
- Dual output (file + console)
- Comprehensive system monitoring

## 🔧 Customization

### Modify Search Behavior
Edit `search_module.py` to change search providers or parsing logic.

### Enhance Question Generation
Update `question_generator.py` to improve follow-up question quality.

### Adjust Neural Network
Modify `nn_brain.py` to change model architecture or training parameters.

### Extend Logging
Customize `logger.py` for additional logging features.

## 🎨 Future Enhancements

- Voice interface integration
- Web UI dashboard
- Cloud storage support
- Advanced NLP models
- Multi-language support
- Real-time learning visualization

## 📝 Example Output

```
🔁 AI Infinity Learning Started
🧠 Ask a starting question:
> What is artificial intelligence?

[2025-07-16 20:29:06] [Alpha] Asking: What is artificial intelligence?
[2025-07-16 20:29:06] [Beta] Searching: What is artificial intelligence?
🌐 Searching: What is artificial intelligence?
[2025-07-16 20:29:07] [Beta] Answer: Artificial intelligence (AI) is...
🧠 Neural brain trained.
[2025-07-16 20:29:07] [Beta] Generated Follow-Up: What more can you tell me about Artificial intelligence?
```

## 🛠️ Troubleshooting

- **Search Issues**: Google may block automated requests. This is normal behavior.
- **Model Downloads**: First run will download sentence-transformer models (~90MB).
- **Memory Errors**: Ensure sufficient RAM for neural network operations.

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for continuous AI learning and knowledge expansion!**
