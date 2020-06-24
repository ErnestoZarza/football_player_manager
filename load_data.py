import io
import csv
import os

import mysql.connector
import pandas as pd
import dask

basePath = os.path.dirname(os.path.abspath(__file__))
path = basePath + '/data/data.csv'





# region Create DB

# cursor.execute("CREATE DATABASE football_players_db")
#
# print("football_players_db Created")


# cursor.execute("SHOW DATABASES")
#
# for x in cursor:
#     print(x)

# endregion

# region Create Players Table

# Creating only the fields that are interesting for our service
# cursor.execute("CREATE TABLE players (id INT PRIMARY KEY, name VARCHAR(255), age INT, "
#                "nationality VARCHAR(255), club VARCHAR(255), photo VARCHAR(255), overall INT, "
#                "value FLOAT), position VARCHAR(255)")
#

# cursor.execute("SHOW TABLES")
#
# for x in cursor:
#     print(x)

# end region


# region Load Data from CSV

# csv_data = csv.reader('students.csv', delimiter=',')
# for row in csv_data:
#
#

# endregion

# region saving data from the csv and data cleaning

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
    df = pd.read_csv(path)
    data_set = df[['ID', 'Name', 'Age', 'Nationality', 'Club', 'Photo', 'Overall', 'Value', 'Position']]
    data_set['Value'] = data_set['Value'].apply(get_value_int)
    return data_set

# endregion


# region saving into mysql db

def drop_db():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Panda@#35",
        database="football_players_db"
    )

    cursor = my_db.cursor()
    cursor.execute("DROP TABLE players")


def load_data():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Panda@#35",
        database="football_players_db"
    )

    cursor = my_db.cursor()

    df = read_data_csv()

    # cursor.execute('INSERT INTO testcsv(names, \
    #           classes, mark )' \
    #           'VALUES("%s", "%s", "%s")',
#           row)
# #close the connection to the database.
# mydb.commit()
# cursor.close()


# endregion