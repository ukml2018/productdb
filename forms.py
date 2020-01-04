from wtforms import Form, StringField, SelectField

class ProductSearchForm(Form):
    choices = [('SKU', 'SKU')]
    select = SelectField('Search for Price:', choices=choices)
    search = StringField('')
class PriceForm(Form):
    item_number = StringField('Sku')
    #catalogue_category = StringField('Category')
    #list_price = StringField('Price')
    price_effective_date = StringField('Price Effective Date')
    #media_type = SelectField('Media', choices=media_types)