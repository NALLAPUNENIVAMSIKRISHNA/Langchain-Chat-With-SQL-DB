import sqlite3

# connection to sqlite
connection=sqlite3.connect("student.db")

# create cursor object to insert record, create table
cursor=connection.cursor()

# create table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""
cursor.execute(table_info)

# insert some more records
cursor.execute('''Insert Into Student values('Vamsi','Gen AI','A',95)''')
cursor.execute('''Insert Into Student values('Naveen','Data scientist','A+',99)''')
cursor.execute('''Insert Into Student values('Ashish','CS','A',90)''')
cursor.execute('''Insert Into Student values('Sumanth','Gen AI','A',95)''')
cursor.execute('''Insert Into Student values('Subhash','AI & ML','A',95)''')

# Display all records
print("The inserted records are")
data=cursor.execute('''select * from student''')
for row in data:
    print(row)
    
# commit your changes in the database
connection.commit()
connection.close()