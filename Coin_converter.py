import streamlit as st
import requests

veri=requests.get("https://api.coinlore.net/api/tickers/").json()
coinler=[coin["symbol"] for coin in veri["data"]]
cost=st.number_input("Amount:",min_value=0.00)

option=st.selectbox("Çevrilecek Coin",coinler)
option2=st.selectbox("Hedef Coin",coinler)

fiyat1=0
fiyat2=0

for coin in veri["data"]:
    if coin["symbol"]==option:
        fiyat1=float(coin["price_usd"])

    if coin["symbol"]==option2:
        fiyat2=float(coin["price_usd"])

if st.button("Exchange"):
    sonuc=cost*fiyat1/fiyat2
    st.success(f"{cost} {option}={sonuc:6f} {option2}")
st.write("Seçilen:",option,"=>",option2)

