from flask import Flask, redirect, render_template

app = Flask(__name__)

url = "https://cytech-calendars.cellar-c2.services.clever-cloud.com/{0}"


@app.route('/')
def index():
    return render_template('index.html', linkA=url.format("ING3-CS-A.ics"), linkB=url.format("ING3-CS-B.ics"))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
