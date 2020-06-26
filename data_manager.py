import os

from sqlalchemy import create_engine
import pandas as pd

# base path
basePath = os.path.dirname(os.path.abspath(__file__))


def get_value_int(value):
    """
    Method to convert player's values into float
    :param value: string value
    :return: string value converted to float
    """
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
    """
    Method to read the original csv file
    :return: a customized dataframe with the significant fields
    """
    path = basePath + '/data/data.csv'
    df = pd.read_csv(path)
    data_set = df[['ID', 'Name', 'Age', 'Nationality', 'Club', 'Photo', 'Overall', 'Value', 'Position']]
    data_set['Value'] = data_set['Value'].apply(get_value_int)
    return data_set


def save_data():
    """
    Save the data from the csv in the db
    :return:
    """

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


def get_data_from_db(name=None, club=None, nationality=None):
    """
    Filter methos
    :param name: filter by name
    :param club: filter by club
    :param nationality: filter by nationality
    :return: customized dataframe
    """
    sql_engine = create_engine('mysql+pymysql://root:Panda@#35@127.0.0.1', pool_recycle=3600)

    db_connection = sql_engine.connect()

    where = ''

    # Next steps make the search by patterns
    if name:
        where = "WHERE Name LIKE '{name}'".format(name=name)
    if club:
        if "WHERE" in where:
            where += " AND Club LIKE '{club}'".format(club=club)
        else:
            where = "WHERE Club LIKE '{club}'".format(club=club)
    if nationality:
        if "WHERE" in where:
            where += " AND Nationality LIKE '{nationality}'".format(nationality=nationality)
        else:
            where = "WHERE Nationality LIKE '{nationality}'".format(nationality=nationality)
    query = "SELECT * FROM football_players_db.players {filter}".format(filter=where)

    frame = pd.read_sql(query, db_connection)

    pd.set_option('display.expand_frame_repr', False)

    result = frame[['Name', 'Age', 'Nationality', 'Club', 'Photo', 'Overall', 'Value']]
    result = result.to_json(force_ascii=False)

    db_connection.close()
    return result


def get_data_frame_from_db():
    """
    :return: returns the db as a dataframe
    """
    sql_engine = create_engine('mysql+pymysql://root:Panda@#35@127.0.0.1', pool_recycle=3600)
    db_connection = sql_engine.connect()
    frame = pd.read_sql("SELECT * FROM football_players_db.players", db_connection);
    pd.set_option('display.expand_frame_repr', False)
    db_connection.close()
    return frame


if __name__ == '__main__':
    save_data()
