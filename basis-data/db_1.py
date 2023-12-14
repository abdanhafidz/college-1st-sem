import mysql.connector

db_con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kuliah_db_1"
)

cr = db_con.cursor()
cr.execute("SELECT*FROM mahasiswa")
