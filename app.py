from flask import Flask, request, jsonify, render_template
from model2 import myfunc1

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.form['input-text']
    summary = myfunc1(data)
    return render_template('index.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
