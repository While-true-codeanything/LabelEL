import streamlit as st

st.subheader('Новости')

text = st.text_area('Текст новости')
news_tags = {
    'support': [],
    'hack': [],
    'accelerator': [],
    'grant': [],
    'market': [],
    'market_news': [],
    'market_review': [],
    'market_expert_opinion': [],
    'product': []
}

st.subheader('Тип новости')
support_col, market_col, product_col = st.columns(3)

with support_col:
    support = st.checkbox('Мера поддержки', key='support')
    if support:
        news_tags['support'] = [1]
        news_tags['hack'] = [int(st.checkbox('Хакатон'))]
        news_tags['accelerator'] = [int(st.checkbox('Акселератор'))]
        news_tags['grant'] = [int(st.checkbox('Грант'))]

with market_col:
    market = st.checkbox('Рынок', key='market')
    if market:
        news_tags['market'] = [1]
        news_tags['market_news'] = [int(st.checkbox('Новости рынка'))]
        news_tags['market_review'] = [int(st.checkbox('Обзор рынка'))]
        news_tags['market_expert_opinion'] = [int(st.checkbox('Мнение эксперта'))]
with product_col:
    product = st.checkbox('Продукт', key='product')

st.subheader('Релевантность')

