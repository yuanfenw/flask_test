from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Main Page'

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
