import streamlit as st
import xml.etree.ElementTree as et
import requests
response=requests.get("https://www.tcmb.gov.tr/kurlar/today.xml")
veri=response.text
root=et.fromstring(veri)
veri=requests.get("https://api.coinlore.net/api/tickers/").json()
coinler=[coin["symbol"] for coin in veri["data"]]
cost=st.number_input("Amount:",min_value=0.00)

option=st.selectbox("Çevrilecek Coin",coinler)
option2=st.selectbox("Hedef Coin",coinler)
kurlar={}
for kur in root:
    kurlar.update({kur.attrib['Kod']:float(kur[3].text)})

kurlar['TRY']=1
kur1=st.selectbox("Eldeki kur",list(kurlar.keys()))
kur2=st.selectbox("Hedef kur",list(kurlar.keys()))
#adet=st.number_input("Adet")

fiyat1=0
fiyat2=0
fiyat1=kurlar[kur1]
fiyat2=kurlar[kur2]

sonuc=fiyat1/fiyat2*cost


for coin in veri["data"]:
    if coin["symbol"]==option:
        fiyat1=float(coin["price_usd"])

    if coin["symbol"]==option2:
        fiyat2=float(coin["price_usd"])

if st.button("Exchange"):
    sonuc=cost*fiyat1/fiyat2
    st.success(f"{cost} {option}={sonuc:6f} {option2}")
st.write("Seçilen:",option,"=>",option2)
st.write(sonuc)
#st.write("Seçilen:",option,"=>",option2)

