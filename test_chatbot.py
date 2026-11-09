"""
Simple tests for the Basic Rule-Based Chatbot.

Run with:
    python -m unittest test_chatbot.py -v
"""

import unittest

from chatbot import get_response, is_exit_command


class TestGetResponse(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(get_response("hello"), "Hi! Welcome to my chatbot.")

    def test_how_are_you(self):
        self.assertEqual(get_response("how are you"),
                         "I'm fine, thanks! How can I help you?")

    def test_name(self):
        self.assertEqual(get_response("what is your name"),
                         "I am a Python Basic Chatbot.")

    def test_abilities(self):
        self.assertEqual(get_response("what can you do"),
                         "I can answer simple predefined questions.")

    def test_thanks(self):
        self.assertEqual(get_response("thank you"), "You're welcome!")

    def test_case_insensitive(self):
        self.assertEqual(get_response("HELLO"), "Hi! Welcome to my chatbot.")
        self.assertEqual(get_response("  How Are You  "),
                         "I'm fine, thanks! How can I help you?")

    def test_unknown_message(self):
        self.assertEqual(get_response("xyz"),
                         "Sorry, I don't understand that. Please try again.")


class TestExitCommand(unittest.TestCase):
    def test_exit_words(self):
        for word in ("bye", "exit", "quit", "BYE", "Quit"):
            self.assertTrue(is_exit_command(word))

    def test_non_exit_words(self):
        self.assertFalse(is_exit_command("hello"))


if __name__ == "__main__":
    unittest.main()
