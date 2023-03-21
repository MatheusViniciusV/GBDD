import sqlite3

connection = sqlite3.connect("banco_docente.db")
cursor = connection.cursor()


def newrow(name, shortname, sipae, email, telefone):

    cursor.execute("INSERT INTO professores VALUES (:name, :shortname, :sipae, :email, :telefone)",
                    {
                       'name': name,
                       'shortname': shortname,
                       'sipae': sipae,
                       'email': email,
                       'telefone': telefone

                    }
                   )
    connection.commit()


def sqlclose():
    connection.close()
    print("fechando conexão!")
