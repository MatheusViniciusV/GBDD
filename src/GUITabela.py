from tkinter import *
import tkinter.ttk as ttk
from BancoDeDados import *
from GUIAdicionarLinha import *

class GUITabela:

    root = None
    procura = None
    barra_procura = None
    botao_procura = None
    body = None
    scroll_bar_y = None
    scroll_bar_x = None
    tree = None
    bottom = None
    botao_adicionar_linha = None
    botao_remover_linha = None
    botao_editar_linha = None
    botao_limpar_pesquisa = None
    banco_de_dados = None
    tabela = None

    def __init__(self, banco_de_dados, nometabela):

        self.root = Tk()
        self.root.title('Table Manager')
        self.root.geometry('1060x450')
        self.root.resizable(False, False)

        self.banco_de_dados = banco_de_dados
        self.tabela = nometabela

        self.barra_procura = Entry(self.root, width=37)
        self.barra_procura.grid(column=0, row=0, padx=5, pady=10, columnspan=2)
        self.botao_procura = Button(self.root, text='Procurar na tabela', command=self.pesquisar_tabela, width=15)
        self.botao_procura.grid(column=2, row=0, padx=5, pady=10)
        self.botao_limpar_pesquisa = Button(self.root, text='Limpar pesquisa', command=self.limpar_pesquisa, width=12)
        self.botao_limpar_pesquisa.grid(column=3, row=0, padx=5, pady=10)

        self.body = Frame(self.root, height=400)
        self.body.grid(column=0, row=1, columnspan=4, padx=10)
        self.scroll_bar_y = Scrollbar(self.body, orient=VERTICAL)
        self.scroll_bar_x = Scrollbar(self.body, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.body, selectmode="extended", yscrollcommand=self.scroll_bar_y.set, xscrollcommand=self.scroll_bar_x.set, height=15)
        self.scroll_bar_y.config(command=self.tree.yview)
        self.scroll_bar_y.pack(side=RIGHT, fill=Y)
        self.scroll_bar_x.config(command=self.tree.xview)
        self.scroll_bar_x.pack(side=BOTTOM, fill=X)
        self.mostrar_tabela()
        self.tree.pack()

        self.bottom = Frame(self.root, height=30)
        self.bottom.grid(column=0, row=2, columnspan=4)
        
        self.botao_adicionar_linha = Button(self.bottom, text='Adicionar linha', command=self.adicionar_linha)
        self.botao_adicionar_linha.grid(column=0, row=0, padx=10, pady=10)
        
        self.botao_remover_linha = Button(self.bottom, text='Remover linha', command=self.remover_na_tabela)
        self.botao_remover_linha.grid(column=1, row=0, padx=10, pady=10)
        
        self.botao_editar_linha = Button(self.bottom, text='Editar linha', command=self.debug)
        self.botao_editar_linha.grid(column=2, row=0, padx=10, pady=10)

    def pesquisar_tabela(self):

        self.tree.delete(*self.tree.get_children())

        lista_colunas = self.banco_de_dados.lista_colunas(self.tabela)
        procura = self.barra_procura.get()
        resultado = None

        for coluna in lista_colunas:

            resultado = self.banco_de_dados.procurar_na_tabela(self.tabela, coluna, procura)

            for linha in resultado: 
                
                linha_street_view = [[]]

                for i in self.tree.get_children():
                    linha_aux = []
                    for valor in list(self.tree.item(i)['values']):
                        linha_aux.append(valor)
                    linha_street_view.append(linha_aux)

                if(list(linha) not in linha_street_view):
                    self.tree.insert("", END, values=linha)

    def limpar_pesquisa(self):

        self.tree.delete(*self.tree.get_children())

        cont = 0
        lista_colunas = self.banco_de_dados.lista_colunas(self.tabela)
        lista_linhas = self.banco_de_dados.lista_linhas(self.tabela)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)

        for coluna in lista_colunas:
            cont = cont + 1
            self.tree.heading(coluna, text=coluna, anchor=W)
            self.tree.column('#' + str(cont), stretch=NO, minwidth=20, width=500//(len(lista_colunas)))

        for linha in lista_linhas:
            self.tree.insert("", END, values=linha)

    def mostrar_tabela(self):

        self.tree.delete(*self.tree.get_children())

        cont = 0
        lista_colunas = self.banco_de_dados.lista_colunas(self.tabela)
        lista_linhas = self.banco_de_dados.lista_linhas(self.tabela)

        self.tree.config(columns=lista_colunas)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)

        for coluna in lista_colunas:
            cont = cont + 1
            self.tree.heading(coluna, text=coluna, anchor=W)
            self.tree.column('#' + str(cont), stretch=NO, minwidth=20, width=500//(len(lista_colunas)))

        for linha in lista_linhas:
            self.tree.insert("", END, values=linha)

    def adicionar_linha(self):
        GUIAdicionarLinha(self.banco_de_dados, self, self.tabela)

    def remover_na_tabela(self):
        selection = self.tree.selection()
        self.banco_de_dados.remover_na_tabela(self.tabela, self.banco_de_dados.lista_colunas(self.tabela)[0], self.tree.set(selection, "#1"))
        self.tree.delete(selection)

    def run(self):
        self.root.mainloop()

    def debug(self):
        print(self.tree.get_children())
