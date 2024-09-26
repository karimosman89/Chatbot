import json
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

def train_chatbot(intents_file):
    intents = json.load(open(intents_file))
    training_sentences = []
    training_labels = []
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            training_sentences.append(pattern)
            training_labels.append(intent['tag'])

    le = LabelEncoder()
    labels = le.fit_transform(training_labels)

    # TODO: Convert sentences to vectors
    # Create and train model
    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(len(training_sentences),)))
    model.add(Dense(len(le.classes_), activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, labels, epochs=200, verbose=1)

if __name__ == "__main__":
    train_chatbot('data/intents.json')
