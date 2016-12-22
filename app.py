from flask import Flask, render_template, request, redirect, jsonify, url_for

app = Flask(__name__)


@app.route('/')
def showItemss():
    # return "This page will show all home page"
        return render_template('index.html')


@app.route('/catalog/Snowboarding/items')
def showAllItemss():
    # return "This page will show all home page"
        return render_template('items.html')

@app.route('/catalog/Snowboarding/Snowboard')
def showOneItemss():
    # return "This page will show all home page"
        return render_template('item.html')

@app.route('/catalog/Snowboard/edit')
def editItemss():
    # return "This page will show all home page"
        return render_template('edititem.html')

@app.route('/catalog/Snowboard/delete')
def deleteItemss():
    # return "This page will show all home page"
        return render_template('deleteitem.html')

@app.route('/catalog.json')
def showItemssApi():
    # return "This page will show all home page"
        return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5005)