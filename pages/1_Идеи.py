
from reactions import *
import streamlit as st

st.subheader('Идеи проектов')

text = st.text_area('Текст', key='tech_text')

tech_tags = TECH_DATA_DEFAULT
tech_tags['text'] = [text]

FILE_NAME = 'tech'

st.subheader('Навыки')
web_col, mobile_col, ds_col, eng_col, meta_col, desktop_col, chatbot_col = st.columns([1 for i in range(7)])


with web_col:
    tech_tags['WEB'] = [int(st.checkbox('Web', key='check1_web'))]

with mobile_col:
    tech_tags['Mobile'] = [int(st.checkbox('Mobile', key='check1_mobile'))]

with eng_col:
    tech_tags['Engineering'] = [int(st.checkbox('Engineer', key='check1_engineer'))]

with meta_col:
    tech_tags['Metaverse'] = [int(st.checkbox('Metaverse', key='check1_meta'))]

with ds_col:
    tech_tags['Data Science'] = [int(st.checkbox('Data Science', key='check1_ds'))]

with desktop_col:
    tech_tags['Desktop'] = [int(st.checkbox('Desktop', key='check1_desktop'))]

with chatbot_col:
    tech_tags['ChatBot'] = [int(st.checkbox('ChatBot', key='check1_chat'))]

st.subheader('Направление')
b2b_col, b2c_col, b2g_col = st.columns(3)
with b2b_col:
    tech_tags['B2B'] = [int(st.checkbox('B2B', key='check1_b2b'))]
with b2c_col:
    tech_tags['B2C'] = [int(st.checkbox('B2C', key='check1_b2c'))]
with b2g_col:
    tech_tags['B2G'] = [int(st.checkbox('B2G', key='check1_b2g'))]

applied_col, social_col, engineer_col, medicine_col, science_col, = st.columns(5)
with social_col:
    tech_tags['Социальные'] = [int(st.checkbox('Социальные', key='check1_social'))]
with medicine_col:
    tech_tags['Медицинские'] = [int(st.checkbox('Медицинские', key='check1_medicine'))]
with science_col:
    tech_tags['Наукоемкие'] = [int(st.checkbox('Наукоемкие', key='check1_science'))]
with engineer_col:
    tech_tags['Инженерные'] = [int(st.checkbox('Инженерные', key='check1_eng'))]
with applied_col:
    tech_tags['Прикладные'] = [int(st.checkbox('Прикладные', key='check1_apply'))]

st.subheader('')
clear_col, delete_col, next_col, export_col = st.columns(4)
with clear_col:
    if st.button('Clear', on_click=clear_tech_checks):
        tech_tags = TECH_DATA_DEFAULT

with delete_col:
    if st.button('Delete'):
        delete_prev(FILE_NAME)
with next_col:
    if st.button('Next ->', on_click=clear_tech_checks, args=[tech_tags, FILE_NAME]):
        tech_tags = TECH_DATA_DEFAULT

with export_col:
    if os.path.isfile(f'{FILE_NAME}.csv'):
        st.download_button('Export',
                           data=convert_df(pd.read_csv(f'{FILE_NAME}.csv', sep=';')),
                           file_name=f'{FILE_NAME}.csv')
