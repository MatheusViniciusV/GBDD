from BancoDeDados import *

class GUINovoQuadro:

    def obtercargahoraria(self, tabela):
        cargahoraria = self.listalinhas(tabela)[0][2] #célula reservada à carga horária total

        return cargahoraria

    def obterlinhas(self, tabela):

        linhas = [[], [], [], [], [], [], [], [], [], [], [], []]
        numerodalinha = 0 

        for largura in range(0, 12):
            numerodacelula = 3 #a partir dessa célula temos os dados vitais para construção do quadro
            for comprimento in range(0, 6):
                linhas[largura][comprimento] = self.listalinhas(tabela)[numerodalinha][numerodacelula]
                numerodacelula += 1
            numerodalinha += 1
        
        return linhas
