from flask import Flask,jsonify
from flask_cors import CORS
from script import get_trending_topics

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return jsonify(message="Welcome to the Trending Topics App")

@app.route('/run_script', methods=['POST'])
def run_script():
    result = get_trending_topics()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
