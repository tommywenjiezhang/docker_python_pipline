import os

from flask import Flask

app = Flask(__name__)

def add(num1, num2):
    return num1 + num2
    

@app.route('/')
def hello():
    return 'Hello Wenjie!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
