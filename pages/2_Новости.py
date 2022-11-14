
from reactions import *
import streamlit as st

st.subheader('Новости')
text = st.text_area('Текст', key='news_text')

news_tags = NEWS_DATA_DEFAULT
news_tags['text'] = [text]
FILE_NAME = 'news'
st.markdown(f"**На данный момент в датасете {check_col(FILE_NAME)} строк", unsafe_allow_html=False)

st.subheader('Тип')
support_col, market_col, product_col = st.columns(3)

with support_col:
    news_tags['support'] = [int(st.checkbox('МЕРА ПОДДЕРЖКИ', key='check_support'))]
    news_tags['hack'] = [int(st.checkbox('Хакатон', key='check_hack'))]
    news_tags['accelerator'] = [int(st.checkbox('Акселератор', key='check_accel'))]
    news_tags['grant'] = [int(st.checkbox('Грант', key='check_grant'))]

with market_col:
    news_tags['market'] = [int(st.checkbox('РЫНОК', key='check_market'))]
    news_tags['market_news'] = [int(st.checkbox('Новости рынка', key='check_market_news'))]
    news_tags['market_review'] = [int(st.checkbox('Обзор рынка', key='check_market_review'))]
    news_tags['market_expert_opinion'] = [int(st.checkbox('Мнение эксперта', key='check_market_expert_opinion'))]
with product_col:
    news_tags['product'] = [int(st.checkbox('Продукт', key='check_product'))]

st.subheader('Релевантность')
social_col, medicine_col, science_col, engineer_col, applied_col = st.columns(5)
with social_col:
    news_tags['social'] = [int(st.checkbox('Социальные', key='check_social'))]
with medicine_col:
    news_tags['medicine'] = [int(st.checkbox('Медицина', key='check_medicine'))]
with science_col:
    news_tags['science'] = [int(st.checkbox('Наука', key='check_science'))]
with engineer_col:
    news_tags['engineer'] = [int(st.checkbox('Инженерные', key='check_eng'))]
with applied_col:
    news_tags['applied'] = [int(st.checkbox('ПРИКЛАДНЫЕ', key='check_apply'))]
    news_tags['web3'] = [int(st.checkbox('Web 3', key='check_web3'))]
    news_tags['utilities'] = [int(st.checkbox('Утилиты', key='check_util'))]
    news_tags['ai'] = [int(st.checkbox('ИИ', key='check_ai'))]


st.title('')
clear_col, delete_col, next_col, export_col = st.columns(4)
with clear_col:
    if st.button('Clear', on_click=clear_news_checks):
        news_tags = NEWS_DATA_DEFAULT

with delete_col:
    if st.button('Delete last'):
        delete_prev(FILE_NAME)
with next_col:
    if st.button('Next ->', on_click=clear_news_checks, args=[news_tags, FILE_NAME]):
        news_tags = NEWS_DATA_DEFAULT

with export_col:
    if os.path.isfile(f'{FILE_NAME}.csv'):
        st.download_button('Export',
                           data=convert_df(pd.read_csv(f'{FILE_NAME}.csv', sep=';')),
                           file_name=f'{FILE_NAME}.csv')
