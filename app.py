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


#adding new item in catogery
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
 
#for view a specific item
@app.route('/catalog/<int:id>/<int:item_id>/viewitem')
def viewItem(id,item_id):
     category = session.query(Category).filter_by(id=id).one()
     item = session.query(Item).filter_by(id=item_id).one()
     return render_template('item.html',item=item,category=category)
    # return "This page will show all home page"


# delete item from list
@app.route('/catalog/<int:id>/<int:item_id>/deleteitem', methods=['GET', 'POST'])
def deleteItem(id,item_id):
     itemToDelete = session.query(Item).filter_by(id=item_id).one()
     if request.method == 'POST':
         session.delete(itemToDelete)
         session.commit()
         return redirect(url_for('showAllItemss',id=id))
     else:
         return render_template('deleteitem.html')  

#  edit item
@app.route('/catalog/<int:id>/<int:item_id>/edititem', methods=['GET', 'POST'])
def editItem(id,item_id):
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        
        editedItem.name = request.form['name']
     
        editedItem.description = request.form['description']
       
        editedItem.img_url = request.form['img_url']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('viewItem',id=id,item_id=item_id))
    else:
         return render_template('edititem.html',item=editedItem)    
    

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