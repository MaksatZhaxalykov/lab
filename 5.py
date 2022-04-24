import psycopg2, csv

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='Baqtyzh2003@'
)
current  = config.cursor()


id_number = input("ID:")
sql = '''
    DELETE FROM phonebook 
    WHERE id = %s;

'''
current.execute(sql, (id_number)) #однозначные

config.commit()
current.close()
config.close()