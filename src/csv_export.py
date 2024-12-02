import sqlite3
import csv

def sqlite_to_csv(db_file, table_name, csv_file):
    """
    SQLiteデータベースのデータをCSVファイルにエクスポートする関数

    Args:
        db_file (str): SQLiteデータベースファイルのパス
        table_name (str): エクスポートするテーブル名
        csv_file (str): 出力するCSVファイルのパス
    """

    # データベースに接続
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # SQLクエリを実行してデータを取得
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()

    # カラム名を取得
    column_names = [description[0] for description in cursor.description]

    # CSVファイルを開いて書き込み
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # ヘッダー行を書き込む
        writer.writerow(column_names)
        # データ行を書き込む
        writer.writerows(data)

    # 接続を閉じる
    conn.close()

# 使用例
db_file = 'account.db'
table_name = 'accountbook_data'
csv_file = 'accountbook_data.csv'

sqlite_to_csv(db_file, table_name, csv_file)