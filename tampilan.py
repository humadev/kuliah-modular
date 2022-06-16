import mysql.connector

koneksi = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="root",
   database="kampus"
)

programming = koneksi.cursor()

programming.execute('select*from mahasiswa')

data = programming.fetchall()

print(data)

print("test")