from tkinter import *

class GUIAdicionarLinha:

    janela = None
    label_linha = None
    entry_linha = None
    button_criar = None
    banco_de_dados = None
    janela_principal = None
    tabela = None

    def __init__(self, banco_de_dados, janela_principal, tabela):

        self.banco_de_dados = banco_de_dados
        self.janela_principal = janela_principal
        self.tabela = tabela

        self.janela = Tk()
        self.janela.title('Inserir linha na tabela')
        self.janela.resizable(False, False)

        self.label_linha = Label(self.janela, text="Digite os valores para serem inseridos usando \'|\' para separá-los:")
        self.entry_linha = Entry(self.janela, width=75)
        self.button_criar = Button(self.janela, text="Inserir", width=10, command=self.inserir)

        self.label_linha.grid(column=0, row=0, padx=10, pady=10)
        self.entry_linha.grid(column=0, row=1, padx=10, pady=10)
        self.button_criar.grid(column=0, row=2, padx=10, pady=10)

    def inserir(self):
        linha = (self.entry_linha.get()).split("|")
        self.banco_de_dados.inserir_na_tabela(self.tabela, linha)
        self.janela_principal.tree.insert("", END, values=linha)
        self.janela.destroy()
