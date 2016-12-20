from flask import Flask, render_template, request, redirect, jsonify, url_for

app = Flask(__name__)


@app.route('/')
def showItemss():
    # return "This page will show all home page"
        return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)