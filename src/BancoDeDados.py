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
    
    def commit(self):
        self.conexao.commit()

    def nova_tabela(self, tabela, colunas):

        comando = ''' CREATE TABLE  ''' + tabela + " ("

        for i in range(len(colunas) - 1):
            comando = comando + colunas[i] + " text, "
        comando = comando + colunas[len(colunas) - 1] + " text)"

        return self.execute(comando)

    def apagar_tabela(self, tabela):
        return self.execute('''DROP TABLE ''' + tabela)

    def dados_tabela(self, tabela):
        return self.cursor.execute('''SELECT * FROM ''' + tabela)
    
    def inserir_na_tabela(self, tabela, valores):

        linha = ''
        cont = 0

        for item in valores:
            linha += '\'' + item + '\''
            cont += 1
            if(cont != len(valores)):
                linha += ', '

        comando =  '''INSERT INTO '''+tabela+' '+ "(" + ", ".join(self.lista_colunas(tabela)) + ")"+''' VALUES '''+'('+linha+')'

        self.execute(comando)
        self.commit()

    def remover_na_tabela(self, tabela, coluna, valor):
        self.cursor.execute('DELETE FROM '+tabela+' WHERE '+coluna+' = ?', (valor,))
        self.commit()

    def lista_tabelas(self):
        return self.execute('''SELECT name FROM sqlite_master WHERE type='table';''')

    def numero_colunas(self, tabela):
        data = self.dados_tabela(tabela)
        return len(data.description)

    def numero_linhas(self, tabela):
        data = self.dados_tabela(tabela)
        return len(data)    

    def lista_colunas(self, tabela):

        colunas = []
        data = self.dados_tabela(tabela)

        for coluna in data.description:
            colunas.append(coluna[0])

        return colunas
    
    def lista_linhas(self, tabela):

        data = self.dados_tabela(tabela)
        lista_linhas = []

        for linha in data:
            lista_linhas.append(linha)

        return lista_linhas
    
    def procurar_na_tabela(self, tabela, coluna, procura):
        return self.cursor.execute("SELECT * FROM " + tabela + " WHERE " + coluna + " LIKE '%" + procura + "%'")

