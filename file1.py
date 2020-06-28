import mysql.connector

conn = mysql.connector.connect(
user = "root",
password = "chimdindu",
host = "127.0.0.1",
database = "python"
)

cursor = conn.cursor()
data = cursor.execute("SELECT * FROM entries")
dataresults = cursor.fetchall()

def Convert(tups, di):
    di = dict(tups)
    return di

dictionary = {}

dictFormat = (Convert(dataresults, dictionary))

print(dictFormat['Game'])
