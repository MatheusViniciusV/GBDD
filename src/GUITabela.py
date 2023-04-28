from tkinter import *
import tkinter.ttk as ttk
from BancoDeDados import *
from GUIAdicionarLinha import *

class GUITabela:

    root = None
    procura = None
    barraprocura = None
    botaoprocura = None
    body = None
    scrollbary = None
    scrollbarx = None
    tree = None
    bottom = None
    botaoadicionarlinha = None
    botaoremoverlinha = None
    botaoeditarlinha = None
    botaolimparpesquisa = None
    bancodedados = None
    tabela = None

    def __init__(self, bancodedados, nometabela):

        self.root = Tk()
        self.root.title('Table Manager')
        self.root.geometry('530x450')
        self.root.resizable(False, False)

        self.bancodedados = bancodedados
        self.tabela = nometabela

        self.barraprocura = Entry(self.root, width=37)
        self.barraprocura.grid(column=0, row=0, padx=5, pady=10, columnspan=2)
        self.botaoprocura = Button(self.root, text='Procurar na tabela', command=self.pesquisartabela, width=15)
        self.botaoprocura.grid(column=2, row=0, padx=5, pady=10)
        self.botaolimparpesquisa = Button(self.root, text='Limpar pesquisa', command=self.limparpesquisa, width=12)
        self.botaolimparpesquisa.grid(column=3, row=0, padx=5, pady=10)

        self.body = Frame(self.root, height=400)
        self.body.grid(column=0, row=1, columnspan=4, padx=10)
        self.scrollbary = Scrollbar(self.body, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.body, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.body, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set, height=15)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.mostrartabela()
        self.tree.pack()

        self.bottom = Frame(self.root, height=30)
        self.bottom.grid(column=0, row=2, columnspan=4)
        
        self.botaoadicionarlinha = Button(self.bottom, text='Adicionar linha', command=self.adicionarlinha)
        self.botaoadicionarlinha.grid(column=0, row=0, padx=10, pady=10)
        
        self.botaoaremoverlinha = Button(self.bottom, text='Remover linha', command=self.removernatabela)
        self.botaoaremoverlinha.grid(column=1, row=0, padx=10, pady=10)
        
        self.botaoeditarlinha = Button(self.bottom, text='Editar linha', command=self.debug)
        self.botaoeditarlinha.grid(column=2, row=0, padx=10, pady=10)

    def pesquisartabela(self):

        self.tree.delete(*self.tree.get_children())

        listacolunas = self.bancodedados.listacolunas(self.tabela)
        procura = self.barraprocura.get()
        resultado = None

        for coluna in listacolunas:

            resultado = self.bancodedados.procurarnatabela(self.tabela, coluna, procura)

            for linha in resultado: 
                
                linhastreeview = [[]]

                for i in self.tree.get_children():
                    linhaaux = []
                    for valor in list(self.tree.item(i)['values']):
                        linhaaux.append(valor)
                    linhastreeview.append(linhaaux)

                if(list(linha) not in linhastreeview):
                    self.tree.insert("", END, values=linha)

    def limparpesquisa(self):

        self.tree.delete(*self.tree.get_children())

        cont = 0
        listacolunas = self.bancodedados.listacolunas(self.tabela)
        listalinhas = self.bancodedados.listalinhas(self.tabela)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)

        for coluna in listacolunas:
            cont = cont + 1
            self.tree.heading(coluna, text=coluna, anchor=W)
            self.tree.column('#' + str(cont), stretch=NO, minwidth=20, width=500//(len(listacolunas)))

        for linha in listalinhas:
            self.tree.insert("", END, values=linha)

    def mostrartabela(self):

        self.tree.delete(*self.tree.get_children())

        cont = 0
        listacolunas = self.bancodedados.listacolunas(self.tabela)
        listalinhas = self.bancodedados.listalinhas(self.tabela)

        self.tree.config(columns=listacolunas)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)

        for coluna in listacolunas:
            cont = cont + 1
            self.tree.heading(coluna, text=coluna, anchor=W)
            self.tree.column('#' + str(cont), stretch=NO, minwidth=20, width=500//(len(listacolunas)))

        for linha in listalinhas:
            self.tree.insert("", END, values=linha)

    def adicionarlinha(self):
        GUIAdicionarLinha(self.bancodedados, self, self.tabela)

    def removernatabela(self):
        selection = self.tree.selection()
        self.bancodedados.removernatabela(self.tabela, self.bancodedados.listacolunas(self.tabela)[0], self.tree.set(selection, "#1"))
        self.tree.delete(selection)

    def run(self):
        self.root.mainloop()

    def debug(self):
        print(self.tree.get_children())
