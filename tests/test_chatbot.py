"""
Unit test suite for the Simple Rule-Based Chatbot project.

Tests intent detection, knowledge base retrieval, fallback logic, input normalization,
and conversation history logging using Python's standard unittest framework.
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

from chatbot import RuleBasedChatbot
from intents import clean_text, detect_intent
from knowledge_base import load_knowledge_base, search_knowledge_base
from logger import log_conversation, read_conversation_history


class TestIntents(unittest.TestCase):
    """Test cases for regular expression intent detection and text cleaning."""

    def test_clean_text(self):
        self.assertEqual(clean_text("  HELLO World!  "), "hello world!")
        self.assertEqual(clean_text("What   is   AI?"), "what is ai?")
        self.assertEqual(clean_text(""), "")

    def test_greeting_intent(self):
        intent, response = detect_intent("hello")
        self.assertEqual(intent, "greeting")
        self.assertIsNotNone(response)

        intent, response = detect_intent("hi there")
        self.assertEqual(intent, "greeting")

        intent, response = detect_intent("good morning")
        self.assertEqual(intent, "greeting")

    def test_help_intent(self):
        intent, response = detect_intent("help")
        self.assertEqual(intent, "help")

        intent, response = detect_intent("what can you do")
        self.assertEqual(intent, "help")

    def test_goodbye_intent(self):
        intent, response = detect_intent("bye")
        self.assertEqual(intent, "goodbye")

        intent, response = detect_intent("goodbye")
        self.assertEqual(intent, "goodbye")

    def test_small_talk_intent(self):
        intent, response = detect_intent("who are you")
        self.assertEqual(intent, "small_talk_name")

        intent, response = detect_intent("who created you")
        self.assertEqual(intent, "small_talk_creator")

    def test_gratitude_intent(self):
        intent, response = detect_intent("thank you")
        self.assertEqual(intent, "gratitude")


class TestKnowledgeBase(unittest.TestCase):
    """Test cases for loading and searching the knowledge base."""

    def setUp(self):
        self.kb_data = {
            "artificial intelligence": "AI is creating systems capable of human intelligence.",
            "machine learning": "ML is a subset of AI that learns from data.",
            "nlp": "NLP enables computers to understand human language.",
            "python": "Python is a high-level programming language."
        }

    def test_exact_and_phrase_matching(self):
        ans = search_knowledge_base("What is Machine Learning?", self.kb_data)
        self.assertEqual(ans, self.kb_data["machine learning"])

        ans = search_knowledge_base("tell me about artificial intelligence!", self.kb_data)
        self.assertEqual(ans, self.kb_data["artificial intelligence"])

        ans = search_knowledge_base("explain NLP please", self.kb_data)
        self.assertEqual(ans, self.kb_data["nlp"])

        ans = search_knowledge_base("what is python", self.kb_data)
        self.assertEqual(ans, self.kb_data["python"])

    def test_unmatched_query(self):
        ans = search_knowledge_base("What is quantum computing?", self.kb_data)
        self.assertIsNone(ans)

    def test_missing_kb_file(self):
        data = load_knowledge_base("non_existent_file.json")
        self.assertEqual(data, {})


class TestLogger(unittest.TestCase):
    """Test cases for conversation history logging."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.log_file = "test_history.txt"

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_log_conversation_creation(self):
        log_path = log_conversation(
            user_message="Hello",
            bot_response="Hi there!",
            log_dir=self.test_dir,
            log_file=self.log_file
        )

        self.assertTrue(log_path.exists())

        lines = read_conversation_history(log_dir=self.test_dir, log_file=self.log_file)
        content = "".join(lines)
        self.assertIn("User: Hello", content)
        self.assertIn("Bot: Hi there!", content)


class TestChatbotOrchestrator(unittest.TestCase):
    """Integration test cases for the RuleBasedChatbot class."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.bot = RuleBasedChatbot(
            kb_path="data/knowledge_base.json",
            log_dir=self.test_dir,
            log_file="test_log.txt"
        )

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_greeting_response(self):
        response = self.bot.get_response("Hello")
        self.assertTrue(any(word in response.lower() for word in ["hello", "hi", "hey", "greetings", "help"]))

    def test_kb_question_response(self):
        response = self.bot.get_response("What is deep learning?")
        self.assertIn("neural networks", response.lower())

    def test_fallback_response(self):
        response = self.bot.get_response("xyz123abc456 invalid question")
        self.assertTrue(any(res in response for res in RuleBasedChatbot.FALLBACK_RESPONSES))

    def test_empty_input(self):
        response = self.bot.get_response("   ")
        self.assertIn("Please type a message", response)

    def test_case_and_punctuation_insensitivity(self):
        resp1 = self.bot.get_response("WHAT IS PYTHON?")
        resp2 = self.bot.get_response("what is python")
        self.assertEqual(resp1, resp2)


if __name__ == "__main__":
    unittest.main()
