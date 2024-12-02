import sqlite3
import csv

def csv_to_sqlite(csv_file, table_name, db_file):
    """
    CSVファイルをSQLiteデータベースにインポートする関数

    Args:
        csv_file (str): インポートするCSVファイルのパス
        table_name (str): 作成するテーブル名
        db_file (str): SQLiteデータベースファイルのパス
    """

    # データベースに接続
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # CSVファイルを開いて読み込む
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # ヘッダー行を取得し、カラム名とする
        header = next(reader)
        # SQLのINSERT文を作成するためのプレースホルダを作成
        placeholders = ', '.join(['?'] * len(header))
        # INSERT文を作成
        sql = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ({placeholders})"
        # データを挿入
        cursor.executemany(sql, reader)

    # 変更をデータベースに反映
    conn.commit()
    # 接続を閉じる
    conn.close()

# 使用例
csv_file = 'accountbook_data.csv'
table_name = 'accountbook_data'
db_file = 'account.db'

csv_to_sqlite(csv_file, table_name, db_file)