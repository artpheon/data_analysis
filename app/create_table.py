import psycopg2

try:
    connection = psycopg2.connect(database='staff', user='artur', password='python', host='127.0.0.1', port='5432')

except psycopg2.Error as err:
    print('\033[91m' + 'An error occurred!', err, + '\033[0m')

else:
    print('\033[92m' + 'Connection to database was successful!' + '\033[0m')



cursor = connection.cursor()

cursor.execute('''create table mystaff.employees
(id int primary key not null,
first_name varchar(25) not null,
last_name varchar(25) not null,
department varchar(25) not null,
phone varchar(25),
address varchar(50),
salary int);''')

connection.commit()
connection.close()