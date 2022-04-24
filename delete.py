from locale import currency
import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='Baqtyzh2003@'
)

current = config.cursor()
id = 1
username = "Bakytzhan"
number = "88005553535"
email = "GG@mail.kz"
sql = '''
    DROP TABLE phonebook;
'''

current.execute(sql)
config.commit()


current.close()
config.close()