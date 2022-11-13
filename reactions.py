import pandas as pd
import os.path


def react_news(data, typ):
    if os.path.isfile(typ + '.csv'):
        df = pd.DataFrame.from_dict(data)
        tech_data = pd.concat([pd.read_csv(typ + '.csv', sep=';'), df])
        tech_data.to_csv(typ + '.csv', sep=';')
    else:
        df = pd.DataFrame.from_dict(data)
        df.to_csv(typ + '.csv', sep=';')


def delete_prev(typ):
    if os.path.isfile(typ + '.csv'):
        dt = pd.read_csv(typ + '.csv', sep=';')
        dt.drop(dt.tail(1).index, inplace=True)
        dt.to_csv(typ + '.csv', sep=';')

