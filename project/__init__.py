from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/', methods=['GET'])
def hello_word():
    return jsonify({
        'status': 'success',
        'message': 'Hello World'
    })