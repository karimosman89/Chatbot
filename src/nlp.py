import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

class NLPProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        with open('data/intents.json') as file:
            self.intents = json.load(file)

    def preprocess(self, sentence):
        words = nltk.word_tokenize(sentence)
        return [self.lemmatizer.lemmatize(word.lower()) for word in words]

    def get_intent(self, user_input):
        processed_input = self.preprocess(user_input)
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                if processed_input == self.preprocess(pattern):
                    return random.choice(intent['responses'])
        return "Sorry, I don't understand."
