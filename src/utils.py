import json
import random

def load_intents(file_path):
    """Load the chatbot intents from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def get_response(intents, user_input):
    """Get chatbot response based on user input."""
    for intent in intents['intents']:
        if user_input.lower() in intent['patterns']:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

