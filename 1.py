import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='Baqtyzh2003@'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook(
        id INTEGER PRIMARY KEY(5),
        username VARCHAR(20),
        number VARCHAR(12),
        email VARCHAR(30)

    )
    '''
)
config.commit()



current.close()
config.close()