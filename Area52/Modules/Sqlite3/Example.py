import sqlite3


# connection = sqlite3.connect("company.db")
# cursor = connection.cursor()

# # delete
# # cursor.execute("""DROP TABLE employee;""")

# sql_command = """
# CREATE TABLE employee (
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1),
# joining DATE,
# birth_date DATE);"""

# cursor.execute(sql_command)

# sql_command = """
# INSERT INTO employee (
# staff_number,
# fname,
# lname,
# gender,
# birth_date)
# VALUES (
# NULL,
# "William",
# "Shakespeare",
# "m",
# "1961-10-25");"""

# cursor.execute(sql_command)


# sql_command = """
# INSERT INTO employee (
# staff_number,
# fname,
# lname,
# gender,
# birth_date)
# VALUES (
# NULL,
# "Frank",
# "Schiller",
# "m",
# "1955-08-17");"""

# cursor.execute(sql_command)

# # never forget this, if you want the changes to be saved:
# connection.commit()
# connection.close()


'''
Of course, in most cases, you will not literally insert data into
a SQL table. You will rather have a lot of data inside of some
Python data type e.g. a dictionary or a list, which has to be
used as the input of the insert statement.

The following working example, assumes that you have already an
existing database company.db and a table employee. We have a
list with data of persons which will be used in the INSERT statement:
'''

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

staff_data = [("William", "Shakespeare", "m", "1961-10-25"),
              ("Frank", "Schiller", "m", "1955-08-17"),
              ("Jane", "Wall", "f", "1989-03-14")]

for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate = p[3])
    cursor.execute(sql_command)

# The time has come now to finally query our employee table:


connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)

# If we run this program, saved as "sql_company_query.py", we get
# the following result, depending on the actual data:

'''
$ python3 sql_company_query.py
fetchall:
(1, 'William', 'Shakespeare', 'm', None, '1961-10-25')
(2, 'Frank', 'Schiller', 'm', None, '1955-08-17')
(3, 'Bill', 'Windows', 'm', None, '1963-11-29')
(4, 'Esther', 'Wall', 'm', None, '1991-05-11')
(5, 'Jane', 'Thunder', 'f', None, '1989-03-14')

fetch one:
(1, 'William', 'Shakespeare', 'm', None, '1961-10-25')
'''
