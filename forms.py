from wtforms import Form, StringField, SelectField

class ProductSearchForm(Form):
    choices = [('Style', 'Style'),
               ('Price', 'Price'),
               ('Category', 'Category')]
    select = SelectField('Search for Price:', choices=choices)
    search = StringField('')
class PriceForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    item_number = StringField('Style')
    catalogue_category = StringField('Category')
    list_price = StringField('Price')
    price_effective_date = StringField('Price Effective Date')
    #media_type = SelectField('Media', choices=media_types)