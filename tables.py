from flask_table import Table, Col, LinkCol

class Results(Table):
    price_id = Col('Price', show=False)
    item_number = Col('Item Number')
    #item_description = Col('Description')
    #cataloque_category = Col('Catalogue Category')
    list_price = Col('Price')
    price_effective_date = Col('Price effective date')
    #publisher = Col('Publisher')
    #media_type = Col('Media')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='item_number'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='item_number'))