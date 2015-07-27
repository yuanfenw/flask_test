from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps

app = Flask(__name__)
GoogleMaps(app)

@app.route('/')
def show_map():
    return render_template('show_map.html')

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

