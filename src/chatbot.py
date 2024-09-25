from nlp import NLPProcessor

class Chatbot:
    def __init__(self):
        self.nlp_processor = NLPProcessor()

    def get_response(self, user_input):
        return self.nlp_processor.get_intent(user_input)

# Usage: chatbot = Chatbot().get_response("Hi")
