from sre_constants import CATEGORY_UNI_LINEBREAK
import psycopg2, csv

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='Baqtyzh2003@'
)
current  = config.cursor()
sql1 = '''
    SELECT * FROM phonebook;
'''
current.execute(sql1, [])
table = current.fetchall()

for i in table:
    print(*i, sep = "     ")
print("~~~~~~")
id_number = input("ID:")
column = input("What do you want to see?  Print '*' if you want to see full information: ")
if column == '*':

    sql = '''
        SELECT * from phonebook
        WHERE id = %s;

    '''
    current.execute(sql, [id_number])

    data = current.fetchone()
    
    print(f"ID: {data[0]}")
    print(f"Username: {data[1]}")
    print(f"Phone number: {data[2]}")
    print(f"Email: {data[3]}")

else:
    if column == "username":
        sql = '''
            SELECT username from phonebook
            WHERE id = %s;
        '''
        current.execute(sql, [id_number])
    if column == "number":
        sql = '''
            SELECT number from phonebook
            WHERE id = %s;
        '''
        current.execute(sql, [id_number])
    if column == "email":
        sql = '''
            SELECT email from phonebook
            WHERE id = %s;
        '''
        current.execute(sql, [id_number])
    data = current.fetchone()

    print(*data)
f = open("Result.csv", "w")
writer = csv.writer(f)

writer.writerow(data)
f.close()
config.commit()
current.close()
config.close()