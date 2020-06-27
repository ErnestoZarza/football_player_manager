import os

from sqlalchemy import create_engine
import pandas as pd

# base path
basePath = os.path.dirname(os.path.abspath(__file__))


class DBConfig:
    #'mysql+pymysql://root:Panda@#35@0.0.0.0:3309/football_players_db', pool_recycle=3600)
    DB_USERNAME = 'root'
    DB_PASSWORD = 'Panda@#35'
    DATABASE_NAME = 'football_players_db'
    DB_HOST = '0.0.0.0'
    DB_URI = "mysql+pymysql://{user}:{password}@{host}/{db_name}".format(user=DB_USERNAME, password=DB_PASSWORD,
                                                                         host=DB_HOST, db_name=DATABASE_NAME)
    MYSQL_ROOT_PASSWORD = 'Panda@#35'
    MYSQL_USER = 'root'
    MYSQL_ALLOW_EMPTY_PASSWORD = True

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DataManager:

    def __init__(self):
        self.db_config = DBConfig()

    def get_value_int(self, value):
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

    def read_data_csv(self):
        """
        Method to read the original csv file
        :return: a customized dataframe with the significant fields
        """
        path = basePath + '/data/data.csv'
        df = pd.read_csv(path)
        data_set = df[['ID', 'Name', 'Age', 'Nationality', 'Club', 'Photo', 'Overall', 'Value', 'Position']]
        data_set['Value'] = data_set['Value'].apply(self.get_value_int)
        return data_set

    def save_data(self):
        """
        Save the data from the csv in the db
        :return:
        """

        table_name = "Players"

        data_frame = self.read_data_csv()

        sql_engine = create_engine(self.db_config.SQLALCHEMY_DATABASE_URI, pool_recycle=3600)

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

    def get_data_from_db(self, name=None, club=None, nationality=None):
        """
        Filter method
        :param name: filter by name
        :param club: filter by club
        :param nationality: filter by nationality
        :return: customized dataframe
        """
        sql_engine = create_engine(self.db_config.SQLALCHEMY_DATABASE_URI, pool_recycle=3600)

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

    def get_data_frame_from_db(self):
        """
        :return: returns the db as a dataframe
        """
        sql_engine = create_engine(self.db_config.SQLALCHEMY_DATABASE_URI, pool_recycle=3600)
        db_connection = sql_engine.connect()
        frame = pd.read_sql("SELECT * FROM football_players_db.players", db_connection);
        pd.set_option('display.expand_frame_repr', False)
        db_connection.close()
        return frame


if __name__ == '__main__':
    data_manager = DataManager()
    data_manager.save_data()
