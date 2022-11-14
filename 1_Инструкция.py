import streamlit as st
with open("opis.txt", encoding="utf8") as file:
    lines = [line for line in file]
    opis = "".join(lines)
st.markdown(opis, unsafe_allow_html=False)
