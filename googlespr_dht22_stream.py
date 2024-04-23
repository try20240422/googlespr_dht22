import streamlit as st
import pandas as pd
from datetime import datetime

# 日時のフォーマットを解析するための関数
def custom_date_parser(x):
    return datetime.strptime(x, '%Y/%m/%d %H:%M:%S')

# CSVファイルからデータを読み込む関数
def load_data(csv_url):
    # CSVデータを読み込む際に、適切な列名を設定
    df = pd.read_csv(
        csv_url, 
        parse_dates=['Timestamp'],
        date_parser=custom_date_parser,
        names=['Timestamp', 'Temperature', 'Humidity'],  # 列名を明示的に指定
        header=None  # ファイルにヘッダー行がないことを示す
    )
    return df

# スプレッドシートからCSVデータを取得する公開URL
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRTcX9UAeqPd9hIBMGuI7chkhKHZq9gUUGH7JyIusMhW_VIGynUFAYiD5LJby_FtAYttTPidSi9stVU/pub?gid=0&single=true&output=csv"

# Streamlitアプリのレイアウト設定
st.title("Temperature and Humidity Monitoring")

# データの読み込み
data = load_data(csv_url)

# データを表示
if not data.empty:
    st.write("Latest data snapshot:")
    st.write(data.tail())

# 温度と湿度のグラフ表示
st.subheader("Temperature and Humidity over Time")
if not data.empty:
    st.line_chart(data.set_index('Timestamp')[['Temperature', 'Humidity']])
