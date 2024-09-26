import json
import random
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model

class Chatbot:
    def __init__(self, model_path, intents_file):
        self.model = load_model(model_path)
        self.intents = json.load(open(intents_file))
        self.le = LabelEncoder()

    def respond(self, user_input):
        # TODO: Preprocess input and predict class
        response = random.choice(self.intents['responses'])
        return response
