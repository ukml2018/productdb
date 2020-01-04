# db_creator.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql+pymysql://xxuser:welcome1@129.146.85.135/sampledb', echo=True)
Base = declarative_base()

class SKU(Base):
    __tablename__ = "XXIBM_PRODUCT_SKU"

    item_number = Column(String, primary_key=True)
    catalogue_category = Column(String)

    def __repr__(self):
        return "{}".format(self.name)

class Price(Base):
    """"""
    __tablename__ = "XXIBM_PRODUCT_PRICING"
    price_id = Column(String, primary_key=True)
    item_number = Column(String, ForeignKey("XXIBM_PRODUCT_SKU.item_number"))
    list_price = Column(String)
    price_effective_date = Column(String)
    #media_type = Column(String)

    #item_number = Column(String, ForeignKey("XXIBM_PRODUCT_STYLE.item_number"))
    #item_number = relationship("Item_number", backref=backref(
    #    "XXIBM_PRODUCT_PRICING", order_by=price_id))
# create tables
#Base.metadata.create_all(engine)