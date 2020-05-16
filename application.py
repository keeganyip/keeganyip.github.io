from flask import Flask, render_template, request, redirect, url_for, flash, session, Markup

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/shopindex')
def shop():
    return render_template('shopindex.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
