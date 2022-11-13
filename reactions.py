import pandas as pd
import streamlit as st

IDEA_DATA = pd.DataFrame.from_dict({'text': ['хуета, а не идея'], 'idea': [0]})
TECH_DATA = pd.DataFrame.from_dict(
    {'text': ['гениальный проект дрона доставщика пиццы'], 'WEB': [1], 'Mobile': [0], 'Engineering': [1],
     'Metverse': [0], 'Data Science': [0],
     'Desktop': [0],
     'ChatBot': [0], 'Management': [0], 'B2B': [0], 'B2C': [1], 'B2G': [0],
     'Социальные': [0], 'Наукоемкие': [0], 'Инженерные': [0], 'Прикладные': [1], 'Медицинские': [0]})

NEWS_DATA = pd.DataFrame.from_dict({
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
})


def clear_news_text():
    st.session_state["news_text"] = ""


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


def react_idea(data: dict):
    global IDEA_DATA
    df = pd.DataFrame.from_dict(data)
    IDEA_DATA = pd.concat([IDEA_DATA, df])


def react_tech(data: dict):
    global TECH_DATA
    df = pd.DataFrame.from_dict(data)
    TECH_DATA = pd.concat([TECH_DATA, df])


def delete_prev():
    global IDEA_DATA
    global TECH_DATA
    global NEWS_DATA
    IDEA_DATA.drop(IDEA_DATA.tail(1).index, inplace=True)
    TECH_DATA.drop(TECH_DATA.tail(1).index, inplace=True)
    NEWS_DATA.drop(NEWS_DATA.tail(1).index, inplace=True)
