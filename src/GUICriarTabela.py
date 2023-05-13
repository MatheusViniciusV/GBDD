from tkinter import *

class GUICriarTabela:

    janela = None
    label_colunas = None
    entry_colunas = None
    button_criar = None
    banco_de_dados = None
    janela_principal = None
    tabela = None

    def __init__(self, banco_de_dados, janela_principal):

        self.banco_de_dados = banco_de_dados
        self.janela_principal = janela_principal

        self.janela = Tk()
        self.janela.title('Criar tabela')
        self.janela.resizable(False, False)

        self.label_nome = Label(self.janela, text="Digite o nome da tabela (sem espaços):")
        self.entry_nome = Entry(self.janela, width=15)

        self.label_colunas = Label(self.janela, text="Digite os nomes das colunas (sem espaços) da tabela usando \'|\' para separá-los:")
        self.entry_colunas = Entry(self.janela, width=60)

        self.button_criar = Button(self.janela, text="Criar tabela", width=15, command=self.criartabela)

        self.label_nome.grid(column=0, row=0, padx=10, pady=5)
        self.entry_nome.grid(column=0, row=1, padx=10, pady=5)
        self.label_colunas.grid(column=0, row=2, padx=10, pady=5)
        self.entry_colunas.grid(column=0, row=3, padx=10, pady=5)
        self.button_criar.grid(column=0, row=4, padx=10, pady=5)

    def criartabela(self):
        nome = self.entry_nome.get()
        lista_colunas = (self.entry_colunas.get()).split("|")
        self.banco_de_dados.nova_tabela(nome, lista_colunas)
        self.janela_principal.configurar_listbox()
        self.janela.destroy()
