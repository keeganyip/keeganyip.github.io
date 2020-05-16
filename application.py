from flask import Flask, render_template, request, redirect, url_for, flash, session, Markup


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/shop')
def shop():
    return render_template('shopindex.html')

@app.route('/shopIndex')
def shopIndex():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

