from distutils.command.install_scripts import install_scripts
import psycopg2, csv

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='Baqtyzh2003@'
)
current = config.cursor()
arr = []

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''

try:
    with open('1.csv') as f:
        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            # print(type(row))
            # print(row)
            row[0] = int(row[0])
            arr.append(row)
    for row in arr:
        current.execute(sql, row)

except:
    id = int(input("ID:"))

    username = input("Username:")

    number = input("Number:")

    email = input("eMail:")
    current.execute(sql, (id, username, number, email))








current.close()
config.commit()
config.close()