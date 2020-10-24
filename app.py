# Author: Anantha Perumal
# Date: Oct 24, 2020
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Web app hosted</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7070,debug = True)
