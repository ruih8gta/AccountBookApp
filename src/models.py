from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment
import os

# create the app
app = Flask(__name__)
app.jinja_env.filters['format_money'] = lambda value: f"{value:,}円"
base_dir = os.path.dirname(__file__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(base_dir,"account.db")
# initialize the app with the extension
db = SQLAlchemy(app)

class SavingsData(db.Model):
    __tablename__ = 'savings_data'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    yucho_asset = db.Column(db.Integer)
    rakuten_asset = db.Column(db.Integer)
    jre_asset = db.Column(db.Integer)
    bank_total = db.Column(db.Integer)
    investment_asset = db.Column(db.Integer)
    profit_loss = db.Column(db.Integer)
    total_money = db.Column(db.Integer)
    def __init__(self,year,month,yucho_asset,rakuten_asset,jre_asset, investment_asset,profit_loss):
            self.year = year
            self.month = month
            self.yucho_asset = yucho_asset
            self.rakuten_asset = rakuten_asset
            self.jre_asset = jre_asset
            bank_total = int(self.yucho_asset) + int(self.rakuten_asset) + int(self.jre_asset)
            self.bank_total = bank_total
            self.investment_asset = investment_asset
            self.profit_loss = profit_loss
            self.total_money = int(self.bank_total) + int(self.investment_asset)
    def __repr__(self):
        return f'<SavingsData {self.id}>'

with app.app_context():
    db.create_all()
