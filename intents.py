"""
Intent recognition module for the Simple Rule-Based Chatbot.

This module defines intent regular expression patterns, predefined responses,
and functions for matching user input against rule-based intent patterns.
"""

import re
import random
from typing import Optional, Tuple, Dict, List

# Dictionary of regex patterns for intent classification
INTENT_PATTERNS: Dict[str, List[str]] = {
    "greeting": [
        r"\b(hi|hello|hey|greetings|howdy|sup)\b",
        r"\bgood\s+(morning|afternoon|evening|day)\b",
    ],
    "help": [
        r"\b(help|commands|capabilities|features|what\s+can\s+you\s+do|options|menu)\b",
        r"\bhow\s+can\s+you\s+help\b",
    ],
    "small_talk_name": [
        r"\b(what\s+is\s+your\s+name|who\s+are\s+you|your\s+name|call\s+you)\b",
    ],
    "small_talk_creator": [
        r"\b(who\s+created\s+you|who\s+made\s+you|who\s+built\s+you|author|developer)\b",
    ],
    "small_talk_how_are_you": [
        r"\b(how\s+are\s+you|how\'?s\s+it\s+going|how\s+do\s+you\s+do)\b",
    ],
    "small_talk_status": [
        r"\b(what\s+are\s+you\s+doing|what\'?s\s+up)\b",
    ],
    "small_talk_nicety": [
        r"\b(nice\s+to\s+meet\s+you|pleasure\s+to\s+meet\s+you)\b",
    ],
    "gratitude": [
        r"\b(thank\s+you|thanks|thank\s+you\s+so\s+much|much\s+appreciated|thx)\b",
    ],
    "goodbye": [
        r"\b(bye|goodbye|exit|quit|see\s+you|take\s+care|farewell|cya)\b",
    ]
}

# Predefined responses for each intent
INTENT_RESPONSES: Dict[str, List[str]] = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What would you like to know?",
        "Hey! Nice to talk with you. Ask me anything about AI!",
        "Greetings! How may I assist you today?"
    ],
    "help": [
        "Here are the available features and commands:\n"
        " - Greetings (e.g., 'hello', 'hi')\n"
        " - Ask about AI concepts (e.g., 'What is Machine Learning?', 'Explain NLP')\n"
        " - View conversation history ('history')\n"
        " - Display help ('help')\n"
        " - Exit chatbot ('exit' or 'quit')"
    ],
    "small_talk_name": [
        "I'm SyntecxBot, a rule-based AI assistant built for the Syntecxhub Internship Project."
    ],
    "small_talk_creator": [
        "I was created by Surag Sunil as part of the Syntecxhub Artificial Intelligence Internship."
    ],
    "small_talk_how_are_you": [
        "I'm doing great, thank you for asking! How can I assist you today?",
        "All systems operational! Ready to discuss Artificial Intelligence."
    ],
    "small_talk_status": [
        "I am waiting to answer your questions about AI, Python, and Machine Learning!"
    ],
    "small_talk_nicety": [
        "Nice to meet you too! How can I assist you today?"
    ],
    "gratitude": [
        "You're very welcome!",
        "Happy to help!",
        "Anytime! Let me know if you have more questions."
    ],
    "goodbye": [
        "Goodbye! Thanks for chatting with me.",
        "See you later! Have a great day!",
        "Bye! Feel free to return if you have more questions."
    ]
}


def clean_text(text: str) -> str:
    """
    Clean and normalize user input string.

    Args:
        text (str): Raw user input string.

    Returns:
        str: Normalized, lowercase, stripped string.
    """
    if not text:
        return ""
    # Convert to lowercase and strip whitespace
    cleaned = text.lower().strip()
    # Remove excessive whitespace
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def detect_intent(user_input: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Detect the user intent from cleaned input text using regular expressions.

    Args:
        user_input (str): Raw or cleaned user message string.

    Returns:
        Tuple[Optional[str], Optional[str]]: A tuple of (intent_name, response_text)
        or (None, None) if no intent is matched.
    """
    cleaned_input = clean_text(user_input)
    if not cleaned_input:
        return None, None

    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, cleaned_input, re.IGNORECASE):
                responses = INTENT_RESPONSES.get(intent, ["I understand."])
                # Return intent name and a deterministically chosen response or random choice
                response = responses[0] if len(responses) == 1 else random.choice(responses)
                return intent, response

    return None, None
