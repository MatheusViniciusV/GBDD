from BancoDeDados import *

class GUINovoQuadro:

    def obter_carga_horaria(self, tabela):
        carga_horaria = self.lista_linhas(tabela)[0][2] #célula reservada à carga horária total

        return carga_horaria

    def obter_linhas(self, tabela):

        matriz_das_linhas = self.lista_linhas(tabela)
        linhas = [[], [], [], [], [], [], [], [], [], [], [], []]
        numero_da_linha = 0 

        for largura in range(0, 12):
            numero_da_celula = 3 #a partir dessa célula temos os dados vitais para construção do quadro
            for comprimento in range(0, 6):
                linhas[largura][comprimento] = matriz_das_linhas[numero_da_linha][numero_da_celula]
                numero_da_celula += 1
            numero_da_linha += 1
        
        return linhas

    def obter_colunas(self, tabela):

        matriz_colunas = self.lista_colunas(tabela)
        colunas = []

        for numero_da_coluna in range(0,6):
            colunas[numero_da_coluna] = matriz_colunas[numero_da_coluna]

        return colunas
