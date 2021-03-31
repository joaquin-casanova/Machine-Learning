import os
from flask import Flask, jsonify

app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/', methods=['GET'])
def hello_word():
    return jsonify({
        'status': 'success',
        'message': 'Hello World'
    })