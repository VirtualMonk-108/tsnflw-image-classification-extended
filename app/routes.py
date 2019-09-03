from flask import render_template, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
 app.run(host='0.0.0.0',port=8001)
