import psycopg2, csv

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='Baqtyzh2003@'
)
current = config.cursor()

try:
    user_id = input("Enter ID: ")
    to_change = input("What do you want to change?: ")
    data = input("To what value set the old value?: ")
    to_change = to_change.lower()
    if to_change == "username":

        sql = '''
            UPDATE phonebook SET username = %s WHERE id = %s;
        '''
        
    if to_change == "number":
        sql = '''
            UPDATE phonebook SET number = %s WHERE id = %s;
        '''
        
    if to_change == "email":
        sql = '''
            UPDATE phonebook SET email = %s WHERE id = %s;
        '''
    current.execute(sql, (data, user_id))
except:
    print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

config.commit()
current.close()
config.close()

