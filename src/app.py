from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from models import app,db, SavingsData, AccountBookData
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
    accountbooks = AccountBookData.query.all()
    labels, values = get_data_account()
    return render_template('budget.html', accountbooks=accountbooks, labels=labels, values=values)

#予算管理機能
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

#家計簿機能
@app.route("/add_account",methods=["POST"])
def add_account():
    year = request.form["input-year"]
    month = request.form["input-month"]
    syokuhi = request.form["input-syokuhi"]
    gaisyoku = request.form["input-gaisyoku"]
    seikatsu = request.form["input-seikatsu"]
    yachin = request.form["input-yachin"]
    denki = request.form["input-denki"]
    gas = request.form["input-gas"]
    suido = request.form["input-suido"]
    net = request.form["input-net"]
    baby = request.form["input-baby"]
    other = request.form["input-other"]
    save_total = request.form["input-save"]
    in_total = request.form["input-in"]

    accountbook = AccountBookData(year,month,syokuhi,gaisyoku,seikatsu,yachin,denki,gas,suido,net,baby,other,save_total,in_total)
    try:
        db.session.add(accountbook)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return render_template("error.html")
    accountbooks = AccountBookData.query.all()
    return render_template("budget.html",accountbooks=accountbooks, labels=labels, values=values)
#直近12ヶ月のデータを取得し、棒グラフで表示するためのデータを取得
def get_data_account():
    data = AccountBookData.query.all()
    #直近１２件のデータを取得
    data = data[-12:]
    labels = [account.id for account in data]
    #    out_total　と　save_total　と in_totalの値を取得
    values1 = [account.out_total for account in data] 
    values2 = [account.save_total for account in data]
    values3 = [account.in_total for account in data]
    values = {
    "out_total": values1 if values1 is not None else [],
    "save_total": values2 if values2 is not None else [],
    "in_total": values3 if values3 is not None else []
    }
    """
    syokuhi
    gaisyoku 
    seikatsu 
    yachin 
    denki
    gas 
    suido 
    net 
    baby 
    other"""
    return labels, values
if __name__ == '__main__':
    app.run(debug=True)