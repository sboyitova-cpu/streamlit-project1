import streamlit as st
import sqlite3
import requests
from datetime import datetime

conn=sqlite3.connect("crypto.db")
c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS crypto(id INTEGER PRIMARY KEY AUTOINCREMENT,coin TEXT,date TEXT,price REAL)")
conn.commit()
st.title("Kripto para sistemi")
st.header("Bugünkü fiyat")
coins=st.text_input("Coin Adı(Bitcoin.Ethereum,Solana...):")
tarih = st.text_input("Tarih (GG-AA-YYYY)","10-07-2026")
if st.button("Kaydet"):
    today = datetime.now().strftime("%d-%m-%Y")
    url=f"https://api.coinlore.net/api/tickers/"
    response=requests.get(url)
    json_data=response.json()["data"]
    bulundu=True

    for item in json_data:
        if item["name"].lower()==coins.lower():
          price=float(item["price_usd"])
          c.execute("INSERT INTO crypto(coin,date,price) VALUES(?,?,?)",(coins.lower(),tarih,price))
          conn.commit()
          st.success(f"{coins} kaydedildi.")
          st.write("Fiyat:",price,"USD")

          bulundu=True
          break

        if not bulundu:
          st.error("Coin bulunamadı")

st.header("Geçmiş fiyatlar")
coins2=st.text_input("Coin Adı:")
tarih2=st.text_input("Tarih(DD-MM-YYYY)")
if st.button("Fiyat getir:"):
    c.execute("SELECT price FROM crypto WHERE LOWER(coin)=LOWER(?) AND date=?""",(coins2.lower(),tarih))
    sonuc=c.fetchone()

    if sonuc:
        st.success(f"{coins2}-{tarih2}")
        st.write("Fiyat:",sonuc[0],"USD")
    else:
        st.error("Bu tarihte bulunamadı.")









