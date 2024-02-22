# app.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, Docker! my name is Vijay, This is a Flask app running in a Docker container.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
