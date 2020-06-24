import os

from sqlalchemy import create_engine
import pymysql
import pandas as pd


basePath = os.path.dirname(os.path.abspath(__file__))


def get_value_int(value):
    magnitude = ''
    if len(value) > 2:
        if str(value[-1]).isalpha():
            magnitude = value[-1]
            v = value[1:-1]
        else:
            v = value[1:]
    else:
        v = value[1]

    data = float(v)

    if magnitude == 'M':
        data *= 10**6
    elif magnitude == 'K':
        data *= 10**3
    return data


def read_data_csv():
    path = basePath + '/data/data.csv'
    df = pd.read_csv(path)
    data_set = df[['ID', 'Name', 'Age', 'Nationality', 'Club', 'Photo', 'Overall', 'Value', 'Position']]
    data_set['Value'] = data_set['Value'].apply(get_value_int)
    return data_set


def save_data():

    table_name = "Players"

    data_frame = read_data_csv()

    sql_engine = create_engine('mysql+pymysql://root:Panda@#35@127.0.0.1/football_players_db', pool_recycle=3600)

    db_connection = sql_engine.connect()

    try:

        frame = data_frame.to_sql(table_name, db_connection, if_exists='fail')

    except ValueError as error:

        print(error)

    except Exception as ex:

        print(ex)

    else:

        print("Table %s created successfully." % table_name);

    finally:

        db_connection.close()

save_data()