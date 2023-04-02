import sqlite3


class BancoDeDados:
    connection = None
    connected = False
    cursor = None

    def conectar(self, arquivo):
        self.connection = sqlite3.connect(arquivo)
        self.cursor = self.connection.cursor()

    def fechar(self):
        self.connection.close()
        self.connected = False

    def execute(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()

    def listtables(self):
        return self.execute('''SELECT name FROM sqlite_master WHERE type='table';''')

    def droptables(self, table):
        return self.execute('''DROP TABLE ''' + table)

    def newtable(self, table, columns):

        command = ''' CREATE TABLE  ''' + table + " ("

        for i in range(len(columns)-1):
            command = command + columns[i] + " text, "
        command = command + columns[len(columns)-1] + " text)"

        return self.execute(command)
