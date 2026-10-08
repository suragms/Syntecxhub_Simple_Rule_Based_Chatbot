"""
Main CLI entry point for the Simple Rule-Based Chatbot.

This script launches the interactive console UI, manages the input loop,
handles CLI exit commands, and catches keyboard interrupts gracefully.
"""

import sys
import os
from chatbot import RuleBasedChatbot
from logger import read_conversation_history


def display_banner() -> None:
    """Print the welcome banner and introductory instructions to the console."""
    banner = """
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
"""
    print(banner)


def display_help() -> None:
    """Print detailed help commands and topic examples."""
    help_text = """
Available commands:
  - hello              : Start a conversation
  - help               : Show chatbot capabilities and help menu
  - history            : Display recent conversation log entries
  - exit / quit / bye  : Close the chatbot gracefully

Example questions you can ask:
  - What is Artificial Intelligence?
  - What is Machine Learning?
  - What is Deep Learning?
  - What is NLP?
  - What is Computer Vision?
  - What is Supervised Learning?
  - What is Unsupervised Learning?
  - What is Reinforcement Learning?
  - What is a Chatbot?
  - What is Python?
  - What is Neural Network?
  - What is Generative AI?
"""
    print(help_text)


def display_history() -> None:
    """Display recent logged conversation turns."""
    print("\n--- Recent Conversation History ---")
    lines = read_conversation_history(max_lines=30)
    for line in lines:
        print(line, end="")
    print("-----------------------------------\n")


def main() -> None:
    """Initialize chatbot instance and start main execution loop."""
    chatbot = RuleBasedChatbot()
    display_banner()

    while True:
        try:
            user_input = input("You: ").strip()

            # Handle empty input
            if not user_input:
                print("\nBot: Please type a message or question. Type 'help' for examples.\n")
                continue

            # Check CLI exit commands
            lower_input = user_input.lower()
            if lower_input in ["exit", "quit", "bye", "goodbye"]:
                print("\nBot: Goodbye! Thanks for chatting with me.")
                print("Conversation saved successfully.\n")
                break

            # Check special CLI commands
            if lower_input == "help":
                display_help()
                continue
            elif lower_input == "history":
                display_history()
                continue

            # Get response from chatbot orchestrator
            response = chatbot.get_response(user_input)
            print(f"\nBot: {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nBot: Goodbye! Thanks for chatting with me.")
            print("Session ended gracefully.\n")
            sys.exit(0)


if __name__ == "__main__":
    main()
