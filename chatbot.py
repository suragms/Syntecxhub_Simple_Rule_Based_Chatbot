"""
Chatbot orchestrator module for the Simple Rule-Based Chatbot.

This module defines the main RuleBasedChatbot class which coordinates intent
detection, knowledge base queries, fallback handling, and conversation logging.
"""

import random
from pathlib import Path
from typing import Dict, Optional, Union

from intents import detect_intent
from knowledge_base import load_knowledge_base, search_knowledge_base
from logger import log_conversation


class RuleBasedChatbot:
    """
    Main rule-based chatbot class managing interaction logic, knowledge retrieval,
    and history logging.
    """

    FALLBACK_RESPONSES = [
        "Sorry, I don't understand that yet. Could you ask that in another way?",
        "I'm still learning. Try asking me about AI, Machine Learning, NLP, or Python!",
        "I'm not sure how to respond to that. Type 'help' to see what I can do."
    ]

    def __init__(
        self,
        kb_path: Union[str, Path] = "data/knowledge_base.json",
        log_dir: Union[str, Path] = "logs",
        log_file: str = "conversation_history.txt"
    ) -> None:
        """
        Initialize the chatbot instance, load the knowledge base, and configure logging.

        Args:
            kb_path (str | Path): Path to knowledge base JSON file.
            log_dir (str | Path): Path to log directory.
            log_file (str): Log filename.
        """
        self.kb_path = Path(kb_path)
        self.log_dir = Path(log_dir)
        self.log_file = log_file

        # Load knowledge base data dictionary
        self.knowledge_base: Dict[str, str] = load_knowledge_base(self.kb_path)

    def detect_intent(self, user_input: str) -> tuple[Optional[str], Optional[str]]:
        """
        Detect intent from user input using the regex intent engine.

        Args:
            user_input (str): Raw input message.

        Returns:
            tuple[Optional[str], Optional[str]]: Matched intent name and initial response.
        """
        return detect_intent(user_input)

    def handle_intent(self, intent: str, user_input: str) -> Optional[str]:
        """
        Process a detected intent and return the corresponding response.

        Args:
            intent (str): The intent identifier.
            user_input (str): Raw input message string.

        Returns:
            Optional[str]: Generated response string for the intent.
        """
        # detect_intent already handles response generation, but this method allows custom overrides
        intent_name, response = detect_intent(user_input)
        return response

    def get_response(self, user_input: str) -> str:
        """
        Generate a bot response for the given user input, handle fallbacks, and log the interaction.

        Args:
            user_input (str): Raw user message text.

        Returns:
            str: Generated chatbot response text.
        """
        stripped_input = user_input.strip() if user_input else ""

        # Handle empty input
        if not stripped_input:
            response = "Please type a message or ask me a question! Type 'help' for available topics."
            return response

        # 1. Intent Detection
        intent, response = self.detect_intent(stripped_input)

        # 2. Knowledge Base Search (if no intent matched or intent was general)
        if not response:
            kb_answer = search_knowledge_base(stripped_input, self.knowledge_base)
            if kb_answer:
                response = kb_answer

        # 3. Fallback Response (if neither intent nor KB produced a response)
        if not response:
            response = random.choice(self.FALLBACK_RESPONSES)

        # 4. Log interaction
        log_conversation(
            user_message=stripped_input,
            bot_response=response,
            log_dir=self.log_dir,
            log_file=self.log_file
        )

        return response
