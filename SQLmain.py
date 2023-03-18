import sqlite3

connection = sqlite3.connect("banco_docente.db")
cursor = connection.cursor()


class SQLmain:
    pass


class SQLclose:
    connection.commit()
    connection.close()
    print("fechando conexão!")
