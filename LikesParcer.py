from flask import Flask, render_template, request,jsonify
import parcer

app = Flask(__name__)


@app.route('/')
def hello_world():
    users = parcer.parse_it_baby()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run()
