
from reactions import *
import streamlit as st

st.subheader('Идея или нет')

text = st.text_area('idea text', key='idea_text')

idea_tags = IDEA_DATA_DEFAULT
idea_tags['text'] = [text]

FILE_NAME = 'idea'

st.subheader('Тип')
id_col = st.columns(1)
with id_col[0]:
    id_n = int(st.checkbox('Это идея проекта', key='check3_ide'))
    idea_tags['idea'] = [id_n]

st.title('')
clear_col_3, delete_col_3, next_col_3, export_col_3 = st.columns(4)
with clear_col_3:
    if st.button('Clear', on_click=clear_idea_checks):
        idea_tags = IDEA_DATA_DEFAULT

with delete_col_3:
    if st.button('Delete'):
        delete_prev(FILE_NAME)
with next_col_3:
    if st.button('Next ->', on_click=clear_idea_checks, args=[idea_tags, FILE_NAME]):
        idea_tags = IDEA_DATA_DEFAULT

with export_col_3:
    if os.path.isfile(f'{FILE_NAME}.csv'):
        st.download_button('Export',
                           data=convert_df(pd.read_csv(f'{FILE_NAME}.csv', sep=';')),
                           file_name=f'{FILE_NAME}.csv')
