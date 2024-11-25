from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from models import app,db, SavingsData
import matplotlib.pyplot as plt
import random

#ページ遷移
@app.route('/')
def index():
    data = SavingsData.query.all()
    latest_money = [account.total_money for account in data][-1]
    #latest_money = SavingsData.query.order_by(SavingsData.total_money.desc()).first()

    #labels = ['Red', 'Blue', 'Yellow', 'Green']
    labels = ['総資産', 'マイホーム代']
    data = [latest_money,40000000]

    return render_template('index.html', labels=labels, data=data)

@app.route('/savings')
def savings():
    savings = SavingsData.query.all()
    labels, values = get_data()
    return render_template('savings.html', savings=savings, labels=labels, values=values)
@app.route('/budget')
def budget():
    return render_template('budget.html')

#機能
@app.route("/add_saving",methods=["POST"])
def add_saving():
    year = request.form["input-year"]
    month = request.form["input-month"]
    yucho_asset = request.form["input-yucho"]
    rakuten_asset = request.form["input-rakuten"]
    jre_asset = request.form["input-jre"]
    investment_asset = request.form["input-invest"]
    profit_loss = request.form["input-loss"]

    savings = SavingsData(year,month,yucho_asset,rakuten_asset,jre_asset, investment_asset,profit_loss)
    try:
        db.session.add(savings)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return render_template("error.html")
    savings = SavingsData.query.all()
    labels, values = get_data()
    return render_template("savings.html",savings=savings, labels=labels, values=values)

def get_data():
    data = SavingsData.query.all()
    labels = [account.id for account in data]
    values = [account.total_money for account in data]
    return labels, values


if __name__ == '__main__':
    app.run(debug=True)