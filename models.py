# models.py
from app import db

class Style(db.Model):
    __tablename__ = "XXIBM_PRODUCT_STYLE"

    item_number = db.Column(db.String, primary_key=True)
    #item_number = db.Column(db.String)
    catalogue_category = db.Column(db.String)

    def __repr__(self):
        return "<Style: {}>".format(self.name)

class Price(db.Model):
    """"""
    __tablename__ = "XXIBM_PRODUCT_PRICING"

    item_number = db.Column(db.String, db.ForeignKey("XXIBM_PRODUCT_STYLE.item_number"), primary_key=True)
    #item_number = db.Column(db.String)
    list_price = db.Column(db.String)
    price_effective_date = db.Column(db.String)
    #publisher = db.Column(db.String)
    #media_type = db.Column(db.String)

    #item_number = db.Column(db.String, db.ForeignKey("XXIBM_PRODUCT_PRICING.item_number"))
    #item_number = db.relationship("Item_number", backref=db.backref(
    #    "XXIBM_PRODUCT_PRICING", order_by=item_number), lazy=True)