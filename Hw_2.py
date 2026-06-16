import streamlit as st

fiyat=int(st.text_input("Lütfen gelirinizi giriniz:"))
vergi=fiyat*0.15
vergi1=fiyat*0.20
vergi2=fiyat*0.27
vergi3=fiyat*0.35
vergi4=fiyat*40
if fiyat in range(0,190000):
  st.write(vergi)
elif fiyat in range(190001,400000):
  st.write(vergi1)
elif fiyat in range(400001,1500000):
  st.write(vergi2)
elif fiyat in range(1500001,5300000):
  st.write(vergi3)
elif fiyat>=5300001.00:
  st.write(vergi4)