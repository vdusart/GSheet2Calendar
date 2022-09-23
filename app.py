from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', link="test")


@app.route('/', defaults={ 'path': '' })
@app.route('/<path:path>')
def catch_all(path):
    return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
