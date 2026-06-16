import streamlit as st

fiyat=st.text_input("Lütfen gelirinizi giriniz:")
fiyat=float(fiyat)
vergi=fiyat*0.15
vergi1= (190000 * 0.15) + ((fiyat- 190000) * 0.20)
vergi2=((190000 * 0.15)+ (210000 * 0.20)+ ((fiyat - 400000) * 0.27))
vergi3=((190000 * 0.15)+ (210000 * 0.20)+ (1100000 * 0.27)+ ((fiyat - 1500000) * 0.35))
vergi4=((190000 * 0.15)+ (210000 * 0.20)+ (1100000 * 0.27)+ (3800000 * 0.35)+ ((fiyat - 5300000) * 0.40))

if fiyat <=190000:
    st.write(vergi)
elif fiyat <=400000:
    st.write(vergi1)
elif fiyat <=1500000:
    st.write(vergi2)
elif fiyat <=5300000:
    st.write(vergi3)
else:
    st.write(vergi4)
