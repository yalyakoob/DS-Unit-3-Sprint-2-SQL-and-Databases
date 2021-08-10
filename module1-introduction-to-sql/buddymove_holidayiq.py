import numpy as np
import pandas as pd
import sqlite3

DB_FILEPATH_1 = "buddymove_holidayiq.db"
connection = sqlite3.connect(DB_FILEPATH_1)
cursor = connection.cursor()

df = pd.read_csv('/Users/youssefalyakoob/Downloads/buddymove_holidayiq.csv')

df.to_sql('review', con = connection, if_exists= 'replace', index = False)

'''Number of Rows'''
number_of_rows = cursor.execute('SELECT COUNT(*) FROM review').fetchone()
print(number_of_rows)

'''How many users who reviewed at least 100 in Nature category also rebviewed 100 in the shopping category'''
num_users = 'SELECT COUNT(*) FROM review WHERE Nature >= 100 AND SHOPPING >= 100'
result = cursor.execute(num_users).fetchall()
print(result)


'''What are the average number of users per category'''
avg_users = 'SELECT AVG(Sports), AVG(Religious), AVG(Nature), \
             AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM review'
result_1 = cursor.execute(avg_users).fetchall()
print(result_1)