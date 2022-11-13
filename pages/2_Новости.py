import pandas as pd
import streamlit as st

from reactions import clear_news_text

st.subheader('Новости')

text = st.text_area('Текст', key='news_text')

news_tags = {
    'text': [text],
    'support': [0],
    'hack': [0],
    'accelerator': [0],
    'grant': [0],
    'market': [0],
    'market_news': [0],
    'market_review': [0],
    'market_expert_opinion': [0],
    'product': [0],
    'social': [0],
    'medicine': [0],
    'science': [0],
    'engineer': [0],
    'applied': [0],
    'web3': [0],
    'utilities': [0],
    'ai': [0]
}

st.subheader('Тип')
support_col, market_col, product_col = st.columns(3)

with support_col:
    support = int(st.checkbox('Мера поддержки', key='support'))
    news_tags['support'] = [support]
    if support:
        news_tags['hack'] = [int(st.checkbox('Хакатон'))]
        news_tags['accelerator'] = [int(st.checkbox('Акселератор'))]
        news_tags['grant'] = [int(st.checkbox('Грант'))]

with market_col:
    market = int(st.checkbox('Рынок', key='market'))
    news_tags['market'] = [market]
    if market:
        news_tags['market_news'] = [int(st.checkbox('Новости рынка'))]
        news_tags['market_review'] = [int(st.checkbox('Обзор рынка'))]
        news_tags['market_expert_opinion'] = [int(st.checkbox('Мнение эксперта'))]
with product_col:
    news_tags['product'] = st.checkbox('Продукт', key='product')

st.subheader('Релевантность')
social_col, medicine_col, science_col, engineer_col, applied_col = st.columns(5)
with social_col:
    news_tags['social'] = [int(st.checkbox('Социальные'))]
with medicine_col:
    news_tags['medicine'] = [int(st.checkbox('Медицина'))]
with science_col:
    news_tags['science'] = [int(st.checkbox('Наука'))]
with engineer_col:
    news_tags['engineer'] = [int(st.checkbox('Инженерные'))]
with applied_col:
    applied = int(st.checkbox('Прикладные'))
    news_tags['applied'] = [applied]
    if applied:
        news_tags['web3'] = [int(st.checkbox('Web 3'))]
        news_tags['utilities'] = [int(st.checkbox('Утилиты'))]
        news_tags['ai'] = [int(st.checkbox('ИИ'))]

st.title('')
clear_col, delete_col, next_col, export_col = st.columns(4)
with clear_col:
    if st.button('Clear', on_click=clear_news_text):

with delete_col:
    if st.button('Delete'):
        print(0)
with next_col:
    if st.button('Next ->'):
        print(0)
with export_col:
    if st.button('Export'):
        print(0)

# st.download_button('export', data=NEWS_DATA, file_name='valid.csv')
