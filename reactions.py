import pandas as pd

idea_data = pd.DataFrame.from_dict({'text': ['хуета, а не идея'], 'idea': [0]})
tech_data = pd.DataFrame.from_dict(
    {'text': ['гениальный проект дрона доставщика пиццы'], 'WEB': [1], 'Mobile': [0], 'Engineering': [1],
     'Metverse': [0], 'Data Science': [0],
     'Desktop': [0],
     'ChatBot': [0], 'Management': [0], 'B2B': [0], 'B2C': [1], 'B2G': [0],
     'Социальные': [0], 'Наукоемкие': [0], 'Инженерные': [0], 'Прикладные': [1], 'Медицинские': [0]})
news_data = pd.DataFrame.from_dict({'text': ['ШОК, ДАНЯ ПОСТАВИЛ В CSV ;'], 'support': [0],
                                    'hack': [0],
                                    'accelerator': [1],
                                    'grant': [0],
                                    'market': [1],
                                    'market_news': [1],
                                    'market_review': [0],
                                    'market_expert_opinion': [1],
                                    'product': [0]})


def react_idea(data):
    global idea_data
    df = pd.DataFrame.from_dict(data)
    idea_data = pd.concat([idea_data, df])


def react_tech(data):
    global tech_data
    df = pd.DataFrame.from_dict(data)
    tech_data = pd.concat([tech_data, df])


def news_data(data):
    global news_data
    df = pd.DataFrame.from_dict(data)
    news_data = pd.concat([news_data, df])


def delete_prev():
    global idea_data
    global tech_data
    global news_data
    idea_data.drop(idea_data.tail(1).index, inplace=True)
    tech_data.drop(tech_data.tail(1).index, inplace=True)
    news_data.drop(news_data.tail(1).index, inplace=True)
