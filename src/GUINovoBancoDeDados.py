from tkinter import *
from GUIInicio import *

class GUINovoBancoDeDados:

    janela = None
    label_nome = None
    button_criar = None
    banco_de_dados = None
    janela_principal = None

    def __init__(self, banco_de_dados, janela_principal):

        self.banco_de_dados = banco_de_dados
        self.janela_principal = janela_principal

        self.janela = Tk()
        self.label_nome = Label(self.janela, text="Nome do Banco de dados:")
        self.entry_nome = Entry(self.janela, width=20)
        self.button_criar = Button(self.janela, text="Criar", width=10, command=self.criarbd)

        self.label_nome.grid(column=0, row=0, pady=5)
        self.entry_nome.grid(column=0, row=1, pady=5)
        self.button_criar.grid(column=0, row=2, pady=5)

    def criarbd(self):
        self.janela_principal.caminho_arquivo = self.entry_nome.get()+'.db'
        self.banco_de_dados.conectar(self.janela_principal.caminho_arquivo)
        self.janela_principal.label_banco_de_dados.config(text='Banco de dados: ' + self.janela_principal.caminho_arquivo)
        self.janela_principal.configurar_listbox()
        self.fechar()

    def fechar(self):
        self.janela.destroy()
