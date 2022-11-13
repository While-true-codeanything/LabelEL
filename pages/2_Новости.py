import copy
import os.path

from reactions import *

st.subheader('Новости')

text = st.text_area('Текст', key='news_text')
text_copy = copy.copy(text)

news_tags = NEWS_DATA_DEFAULT
FILE_NAME = 'news'

st.subheader('Тип')
support_col, market_col, product_col = st.columns(3)

with support_col:
    support = int(st.checkbox('Мера поддержки', key='check_support'))
    news_tags['support'] = [support]
    if support:
        news_tags['hack'] = [int(st.checkbox('Хакатон', key='check_hack'))]
        news_tags['accelerator'] = [int(st.checkbox('Акселератор', key='check_accel'))]
        news_tags['grant'] = [int(st.checkbox('Грант', key='check_grant'))]

with market_col:
    market = int(st.checkbox('Рынок', key='check_market'))
    news_tags['market'] = [market]
    if market:
        news_tags['market_news'] = [int(st.checkbox('Новости рынка', key='check_market_news'))]
        news_tags['market_review'] = [int(st.checkbox('Обзор рынка', key='check_market_review'))]
        news_tags['market_expert_opinion'] = [int(st.checkbox('Мнение эксперта', key='check_market_expert_opinion'))]
with product_col:
    news_tags['product'] = int(st.checkbox('Продукт', key='check_product'))

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
    applied = int(st.checkbox('Прикладные', key='check_apply'))
    news_tags['applied'] = [applied]
    if applied:
        news_tags['web3'] = [int(st.checkbox('Web 3', key='check_web3'))]
        news_tags['utilities'] = [int(st.checkbox('Утилиты', key='check_util'))]
        news_tags['ai'] = [int(st.checkbox('ИИ', key='check_ai'))]

st.title('')
clear_col, delete_col, next_col, export_col = st.columns(4)
with clear_col:
    if st.button('Clear', on_click=clear_news_text):
        news_tags = NEWS_DATA_DEFAULT

with delete_col:
    if st.button('Delete'):
        delete_prev(FILE_NAME)
with next_col:
    if st.button('Next ->', on_click=clear_news_text):
        news_tags['text'] = [text_copy]
        react_news(news_tags, FILE_NAME)
        news_tags = NEWS_DATA_DEFAULT

with export_col:
    if os.path.isfile(f'{FILE_NAME}.csv'):
        st.download_button('Export',
                           data=convert_df(pd.read_csv(f'{FILE_NAME}.csv', sep=';')),
                           file_name=f'{FILE_NAME}.csv')
