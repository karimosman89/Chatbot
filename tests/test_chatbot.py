import unittest
from chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_response(self):
        response = self.chatbot.get_response("Hi")
        self.assertIn(response, ["Hello!", "Hi there!", "Greetings!"])

if __name__ == '__main__':
    unittest.main()
