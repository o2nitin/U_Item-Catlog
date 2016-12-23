from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def showItemss():
    # return "This page will show all home page"
        categories = session.query(Category).all()
        return render_template('index.html',categories=categories)

@app.route('/addnewcat', methods=['GET', 'POST'])
def newCat():
    if request.method == 'POST':
        newCat = Category(name=request.form['name'],url=request.form['url'])
        session.add(newCat)
        session.commit()
        return redirect(url_for('showItemss'))
    else:
        return render_template('addcat.html')


@app.route('/catalog/<int:id>/items')
def showAllItemss(id):
    category = session.query(Category).filter_by(id=id).one()
    items = session.query(Item).filter_by(
        category_id=id).all()
    return render_template('items.html', items=items, category=category)
    # return "This page will show all home page"

@app.route('/catalog/<int:id>/newitem', methods=['GET', 'POST'])
def addNewItem(id):
     category = session.query(Category).filter_by(id=id).one()
     if request.method == 'POST':
         newItem = Item(name=request.form['name'],img_url=request.form['img_url'],
                            description=request.form['description'],category_id=id)
         session.add(newItem)
         session.commit()
         return redirect(url_for('showAllItemss',id=id))
     else:
         return render_template('newitem.html',category=category)
    # return "This page will show all home page"
    

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
    app.run(host='0.0.0.0', port=5000)