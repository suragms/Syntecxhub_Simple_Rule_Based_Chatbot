# Simple Rule-Based Chatbot

## Syntecxhub Artificial Intelligence Internship (Project 1)

## Overview

The **Simple Rule-Based Chatbot** is a lightweight, offline conversational agent developed in Python as part of Project 1 for the **Syntecxhub Artificial Intelligence Internship**. The chatbot uses regular expression pattern matching for intent recognition, a JSON-based domain knowledge base for answering AI and computer science questions, a timestamped conversation logger, and an interactive terminal interface.

The application operates completely offline using the Python standard library without requiring external LLM APIs, paid dependencies, or cloud services.

---

## Features

- **Rule-Based Intent Recognition:** Regex pattern matching engine identifying user intents (greetings, help, small talk, gratitude, farewells).
- **Domain Knowledge Base:** Answers queries covering 12 core AI topics (Artificial Intelligence, Machine Learning, Deep Learning, NLP, Computer Vision, Supervised Learning, Unsupervised Learning, Reinforcement Learning, Chatbot, Python, Neural Networks, Generative AI).
- **Conversation Logging:** Automatically records user queries and bot responses with timestamps in `logs/conversation_history.txt`.
- **Interactive Console UI:** Formatted terminal interface with colored/styled text banners and built-in CLI commands (`help`, `history`, `exit`).
- **Offline & Lightweight:** Built using 100% Python Standard Library.
- **Robust Error & Input Handling:** Case-insensitive, punctuation-resilient, whitespace-stripped processing with graceful handling of missing files and keyboard interrupts (`Ctrl+C`).
- **Comprehensive Unit Testing:** Includes standard `unittest` test suite covering all modules and edge cases.

---

## Technologies Used

- **Python 3.10+**
- **Regular Expressions (`re`):** Pattern matching and intent classification.
- **JSON (`json`):** Domain knowledge storage and retrieval.
- **Path handling (`pathlib`):** Directory and file management.
- **Timestamps (`datetime`):** Conversation log timestamping.
- **Testing (`unittest`):** Automated test discovery and assertion suite.

---

## Project Structure

```
Syntecxhub_Simple_Rule_Based_Chatbot/
│
├── main.py                    # Entry point & interactive CLI loop
├── chatbot.py                 # RuleBasedChatbot class orchestrating intents, KB & logging
├── intents.py                 # Intent regex patterns, responses & detect_intent()
├── knowledge_base.py          # Knowledge base loader & query search engine
├── logger.py                  # Conversation history logger
│
├── data/
│   └── knowledge_base.json    # JSON storage for domain Q&A concepts
│
├── logs/
│   └── conversation_history.txt # Auto-generated conversation log file
│
├── tests/
│   └── test_chatbot.py        # Comprehensive unittest suite
│
├── requirements.txt           # Dependency declaration (Python standard library)
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
└── README.md                  # Internship documentation & guide
```

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/suragms/Syntecxhub_Simple_Rule_Based_Chatbot.git
   cd Syntecxhub_Simple_Rule_Based_Chatbot
   ```

2. **Create and Activate a Virtual Environment (Optional):**
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The project uses the Python Standard Library exclusively, so no external package installations are required.)*

---

## Running the Project

To launch the interactive chatbot terminal interface, run:

```bash
python main.py
```

---

## Running Tests

To run the automated unit test suite, execute:

```bash
python -m unittest discover tests
```

---

## Example Conversation

```text
==================================================
       SYNTECXHUB AI INTERNSHIP PROJECT
          SIMPLE RULE-BASED CHATBOT
==================================================
Bot: Hello! I'm SyntecxBot.
Bot: You can ask me about Artificial Intelligence.
Bot: Type 'help' to see available commands.
Bot: Type 'history' to view recent log entries.
Bot: Type 'exit' or 'quit' to close the chatbot.
==================================================

You: Hello

Bot: Hello! How can I help you today?

You: What is machine learning?

Bot: Machine Learning (ML) is a subset of AI that focuses on building applications that learn from data and improve their performance over time without being explicitly programmed.

You: Tell me about NLP

Bot: Natural Language Processing (NLP) is a field of AI focused on enabling computers to understand, interpret, manipulate, and generate human language in a valuable and contextually accurate way.

You: exit

Bot: Goodbye! Thanks for chatting with me.
Conversation saved successfully.
```

---

## Supported Intents

1. **Greeting:** Recognized words like `hi`, `hello`, `hey`, `good morning`, `greetings`.
2. **Help:** Commands like `help`, `what can you do`, `commands`, `features`.
3. **Small Talk:** Questions like `who are you`, `what is your name`, `who created you`, `how are you`.
4. **Gratitude:** Phrases like `thank you`, `thanks`, `much appreciated`.
5. **Domain Knowledge:** Questions matching topics stored in `data/knowledge_base.json`.
6. **Goodbye:** Exit triggers like `bye`, `goodbye`, `exit`, `quit`.
7. **Fallback:** Friendly default response when input is unknown or unmatched.

---

## Knowledge Base

Domain questions and answers are stored cleanly in [`data/knowledge_base.json`](data/knowledge_base.json). Topics included:
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Deep Learning (DL)
- Natural Language Processing (NLP)
- Computer Vision
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
- Chatbot
- Python
- Neural Networks
- Generative AI

---

## Conversation Logging

All conversation turns are automatically appended to [`logs/conversation_history.txt`](logs/conversation_history.txt) in the following format:

```text
[2026-10-07 20:10:15]
User: What is machine learning?
Bot: Machine Learning (ML) is a subset of AI that focuses on...
```

The `logs/` directory is created automatically on first run if it does not already exist.

---

## Future Improvements

- **Graphical User Interface (GUI):** Build a Tkinter or PyQt interface.
- **Voice Recognition:** Integrate speech-to-text and text-to-speech engines.
- **Expanded Knowledge Base:** Support dynamic online data sources or larger JSON schemas.
- **NLP / ML Intent Classification:** Upgrade regex matching to TF-IDF or vector embeddings.
- **Database Storage:** Replace flat file log storage with SQLite or PostgreSQL.

---

## Internship Information

- **Project:** Simple Rule-Based Chatbot (Project 1)
- **Domain:** Artificial Intelligence
- **Organization:** Syntecxhub

---

## Author

- **Name:** Surag Sunil
- **Role:** Artificial Intelligence Intern at Syntecxhub

---

## License

Distributed under the [MIT License](LICENSE).
