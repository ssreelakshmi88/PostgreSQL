import psycopg2

# #connect to "chinook" database
connection = psycopg2.connect(database = "chinook")

# build a cursor object of the database
cursor = connection.cursor()

cursor.execute('SELECT "Name" FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
