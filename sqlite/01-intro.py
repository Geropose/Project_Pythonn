import sqlite3

con = sqlite3.connect("sqlite/app.db")
# Intenta conectarse con un archivo con ese nombre, en caso que no exista, lo crea.
# Cada vez que me conecto a una base de datos siempre tengo que CERRARLA!!
con.close()
