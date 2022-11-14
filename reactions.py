import pandas as pd
import os.path
import streamlit as st

IDEA_DATA = pd.DataFrame.from_dict({'text': ['хуета, а не идея'], 'idea': [0]})
TECH_DATA_DEFAULT = {'text': [''], 'WEB': [0], 'Mobile': [0], 'Engineering': [0],
                     'Metaverse': [0], 'Data Science': [0],
                     'Desktop': [0],
                     'ChatBot': [0], 'B2B': [0], 'B2C': [0], 'B2G': [0],
                     'Социальные': [0], 'Прикладные': [0], 'Наукоемкие': [0], 'Инженерные': [0], 'Медицинские': [0]}

NEWS_DATA_DEFAULT = {
    'text': [''],
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


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


def clear_news_checks(tags: dict = None, filename: str = None):
    if tags is not None and filename is not None:
        react_news(tags, filename)
    st.session_state['news_text'] = ""
    for state in st.session_state.keys():
        if 'check' in state:
            st.session_state[state] = False


def clear_tech_checks(tags: dict = None, filename: str = None):
    if tags is not None and filename is not None:
        react_news(tags, filename)
    st.session_state['tech_text'] = ""
    for state in st.session_state.keys():
        if 'check1' in state:
            st.session_state[state] = False


def react_news(data, typ):
    if os.path.isfile(typ + '.csv'):
        df = pd.DataFrame.from_dict(data)
        tech_data = pd.concat([pd.read_csv(typ + '.csv', sep=';'), df])
        tech_data.to_csv(typ + '.csv', sep=';', index=False)
    else:
        df = pd.DataFrame.from_dict(data)
        df.to_csv(typ + '.csv', sep=';', index=False)


def delete_prev(typ):
    if os.path.isfile(typ + '.csv'):
        dt = pd.read_csv(typ + '.csv', sep=';')
        dt.drop(dt.tail(1).index, inplace=True)
        dt.to_csv(typ + '.csv', sep=';', index=False)
