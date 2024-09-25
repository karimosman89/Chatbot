from flask import Flask, request, jsonify
from chatbot import Chatbot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
chatbot = Chatbot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
