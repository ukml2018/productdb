# main.py
from app import app
from db_setup import init_db, db_session
from forms import ProductSearchForm, PriceForm
from flask import flash, render_template, request, redirect
from models import Price, SKU
from tables import Results
from db_creator import SKU, Price
import pdb

#pdb.set_trace()
init_db()
@app.route('/', methods=['GET', 'POST'])
def index():
    search = ProductSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'SKU':
            str1 = search_string
            print(str1)
            qry = db_session.query(Price, SKU).filter(
                  Price.item_number == SKU.item_number).filter(
                  SKU.item_number.contains(search_string))
            results = [item[0] for item in qry.all()]
            print(qry)
            #print(search_string)
            #print(Price.item_number.contains(search_string))
        #elif search.data['select'] == 'Price':
        #    qry = db_session.query(Price).filter(
        #        Price.item_number.contains(search_string))
        #    results = qry.all()
            #pdb.set_trace()
        #elif search.data['select'] == 'Category':
        #    qry = db_session.query(Style).filter(
        #        Style.catalogue_category.contains(search_string))
        #    results = qry.all()
        else:
            qry = db_session.query(Price)
            results = qry.all()
    else:
        qry = db_session.query(Price)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        redirect('/')
        table = Results(results)
        table.border = True
        #pdb.set_trace()
        return render_template('results.html', table=table)
@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new album
    """
    form = PriceForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the album
        price = Price()
        save_changes(price, form, new=True)
        flash('Price created successfully!')
        return redirect('/')
    return render_template('new_album.html', form=form)
def save_changes(price, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    SKU = SKU()
    SKU.item_number = form.SKU.data

    price.item_number = item_number
    price.list_price = form.list_price.data
    price.price_effective_date = form.price_effective_date.data
    #album.publisher = form.publisher.data
    #album.media_type = form.media_type.data

    if new:
        # Add the new album to the database
        db_session.add(album)

    # commit the data to the database
    db_session.commit()

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(item_number):
    qry = db_session.query(Price).filter(
        Price.item_number == item_number)
    price = qry.first()

    if price:
        form = PriceForm(formdata=request.form, obj=price)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(album, form)
            flash('Price updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{item_number}'.format(item_number=item_number)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(item_number):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Price).filter(
        Price.item_number == item_number)
    price = qry.first()

    if price:
        form = PriceForm(formdata=request.form, obj=price)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(price)
            db_session.commit()

            flash('Price deleted successfully!')
            return redirect('/')
        return render_template('delete_album.html', form=form)
    else:
        return 'Error deleting #{item_number}'.format(item_number=item_number)
if __name__ == '__main__':
    app.run()