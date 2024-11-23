from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# モデル定義 (例として貯金情報を定義)
class Saving(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    yucho = db.Column(db.Integer)
    rakuten = db.Column(db.Integer)
    jre = db.Column(db.Integer)
    investment = db.Column(db.Integer)
    profit_loss = db.Column(db.Integer)

# ルーティング
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/saving', methods=['GET', 'POST'])
def saving():
    if request.method == 'POST':
        # 貯金情報の保存処理
        saving = Saving(
            year=request.form['year'],
            month=request.form['month'],
            yucho=request.form['yucho'],
            # ...
        )
        db.session.add(saving)
        db.session.commit()
    # 貯金情報の取得処理
    savings = Saving.query.all()
    return render_template('savhomeing.html', savings=savings)

# ... その他のルーティング

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)