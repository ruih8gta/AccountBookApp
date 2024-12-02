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

class AccountBookData(db.Model):
    __tablename__ = 'accountbook_data'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    syokuhi = db.Column(db.Integer)
    gaisyoku = db.Column(db.Integer)
    seikatsu = db.Column(db.Integer)
    yachin = db.Column(db.Integer)
    denki = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    suido = db.Column(db.Integer)
    net = db.Column(db.Integer)
    baby = db.Column(db.Integer)
    other = db.Column(db.Integer)
    out_total = db.Column(db.Integer)
    save_total = db.Column(db.Integer)
    in_total = db.Column(db.Integer)
    diff = db.Column(db.Integer)
    def __init__(self,year,month,syokuhi,gaisyoku,seikatsu,yachin,denki,gas,suido,net,baby,other,save_total,in_total):
            self.year = year
            self.month = month
            self.syokuhi = syokuhi
            self.gaisyoku = gaisyoku
            self.seikatsu = seikatsu
            self.yachin = yachin
            self.denki = denki
            self.gas = gas
            self.suido = suido
            self.net = net
            self.baby =baby
            self.other = other
            self.out_total = int(self.syokuhi) + int(self.gaisyoku) + int(self.seikatsu) + \
             int(self.yachin) + int(self.denki) + int(self.gas) + int(self.suido) + int(self.net) + int(self.baby) + int(self.other)
            self.save_total = save_total
            self.in_total = in_total
            self.diff = int(self.in_total) - int(self.save_total) - int(self.out_total)
    def __repr__(self):
        return f'<AccountBookData {self.id}>'

with app.app_context():
    db.create_all()
