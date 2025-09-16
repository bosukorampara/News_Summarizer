from flask import Flask, render_template, request
from summarization.extractive import summarize_extractive
from summarization.abstractive import summarize_abstractive

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('extractive.html')

@app.route('/extractive', methods=['GET', 'POST'])
def extractive():
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize_extractive(text)
        return render_template('extractive.html', summary=summary)
    return render_template('extractive.html')

@app.route('/abstractive', methods=['GET', 'POST'])
def abstractive():
    summary = ''
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize_abstractive(text)
    return render_template('abstractive.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)