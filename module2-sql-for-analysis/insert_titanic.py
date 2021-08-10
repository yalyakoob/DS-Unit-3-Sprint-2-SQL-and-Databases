import pandas as pd
import psycopg2
import os
import sqlite3
from psycopg2.extras import execute_values
from sqlalchemy import create_engine


def df_create(file_name):
    df = pd.read_csv(file_name)
    # Remove apostrophes in name column
    df['Name'] = df['Name'].str.replace("'", '', regex=True)
    # Replace / and spaces with underscores
    df.columns = df.columns.str.replace('/', '_')
    df.columns = df.columns.str.replace(' ', '_')
    return df


df = df_create('/Users/youssefalyakoob/Downloads/titanic.csv')

engine = create_engine('sqlite:///titanic.sqlite3', echo = False)


#Connecting to Sqlite DB
sl_conn = sqlite3.connect('titanic.sqlite3')
df.to_sql('titanic', con = engine, if_exists = 'replace',index = False, schema = 'main')
#Instantiate sqlite cursor
sl_curs = sl_conn.cursor()
# Save sql tabular data to result variable
result = sl_curs.execute('SELECT * FROM titanic').fetchall()

# Connecting to PostGreSQL DB
dbname = 'taeqsczj'
user = 'taeqsczj'
password = 'btSxYVWWuSdpFQRFSYZLVuStRkSnhvpC'
host = 'chunee.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

#Creating a Table
query = """CREATE TABLE IF NOT EXISTS titanic (
            Survived INTEGER, 
            Pclass INTEGER,
            Name VARCHAR(500),
            Sex VARCHAR(7),
            Age INTEGER,
            Siblings_Spouses_Aboard INTEGER,
            Parents_Children_Aboard INTEGER,
            Fare REAL
            )
            
"""
pg_curs.execute(query)

for row in result:
    insert_row = """
         INSERT INTO titanic
        (Survived, Pclass, Name,
         Sex, Age, Siblings_Spouses_Aboard,
         Parents_Children_Aboard, Fare)
         VALUES """ + str(row[:]) + ';'
    pg_curs.execute(insert_row)

pg_curs.close()
pg_conn.commit()
print(str(row[:]))