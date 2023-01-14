from urllib.parse import unquote

from flask import Flask, jsonify, request

from utils import get_summary

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'welcome to the youtube summary api'


@app.route('/get_summary/<path:url>', methods=['GET'])
def process_text(url):   
    # Run a function with the text as an argument
    url = unquote(url)
    summary = get_summary(url)
    
    # Return the result as a JSON object
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
