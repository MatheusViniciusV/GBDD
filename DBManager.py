import sqlite3


class BancoDeDados:
    conexao = None
    conectado = False
    cursor = None

    def conectar(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()
        self.conectado = True

    def fechar(self):
        self.conexao.close()
        self.conectado = False

    def execute(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()

    def novatabela(self, tabela, colunas):

        comando = ''' CREATE TABLE  ''' + tabela + " ("

        for i in range(len(colunas) - 1):
            comando = comando + colunas[i] + " text, "
        comando = comando + colunas[len(colunas) - 1] + " text)"

        return self.execute(comando)

    def apagartabela(self, tabela):
        return self.execute('''DROP TABLE ''' + tabela)

    def dadostabela(self, tabela):
        return self.cursor.execute('''SELECT * FROM ''' + tabela)

    def listatabelas(self):
        return self.execute('''SELECT name FROM sqlite_master WHERE type='table';''')

    def numerocolunas(self, tabela):
        data = self.dadostabela(tabela)
        return len(data.description)

    def numerolinhas(self, tabela):
        data = self.dadostabela(tabela)
        return len(data)    

    def listacolunas(self, tabela):

        colunas = ''
        data = self.dadostabela(tabela)

        for coluna in data.description:
            colunas = colunas + ' ' + coluna[0]

        return colunas
