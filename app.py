from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils import load_data, create_index, ask_question
from config import OPENAI_API_KEY
import os

app = Flask(__name__)
CORS(app)

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize documents and index
documents = load_data("documents/")
index = create_index(documents) if documents else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def handle_question():
    if not index:
        return jsonify({"error": "Document index not initialized"}), 500
    
    question = request.json.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    response = ask_question(index, question)
    return jsonify({'answer': response.response})

if __name__ == '__main__':
    app.run(port=5001, debug=True) 