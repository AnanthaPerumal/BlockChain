# Author: Anantha Perumal
# Date: Oct 24, 2020
from flask import Flask, render_template
from flask_mysqldb import MySQL
from sqlhelpers import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'crypto'
app.config['MYSQL_PASSWORD'] = 'crypto123'
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    #to create a table
    demo = Table("demo","name","email","username","password")
    #to insert some value inside a table
    demo.insert("AP","a@gmail.com","ap777","hash")
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(host='0.0.0.0',port=7070,debug = True)
