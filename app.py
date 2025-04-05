
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    reply = f"You said: {user_input} (response from Prince AI)"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
