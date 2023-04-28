from tkinter import *

class GUICriarTabela:

    janela = None
    labelcolunas = None
    entrycolunas = None
    buttoncriar = None
    bancodedados = None
    janelaprincipal = None
    tabela = None

    def __init__(self, bancodedados, janelaprincipal):

        self.bancodedados = bancodedados
        self.janelaprincipal = janelaprincipal

        self.janela = Tk()
        self.janela.title('Criar tabela')
        self.janela.resizable(False, False)

        self.labelnome = Label(self.janela, text="Digite o nome da tabela (sem espaços):")
        self.entrynome = Entry(self.janela, width=15)

        self.labelcolunas = Label(self.janela, text="Digite os nomes das colunas (sem espaços) da tabela usando \'|\' para separá-los:")
        self.entrycolunas = Entry(self.janela, width=60)

        self.buttoncriar = Button(self.janela, text="Criar tabela", width=15, command=self.criartabela)

        self.labelnome.grid(column=0, row=0, padx=10, pady=5)
        self.entrynome.grid(column=0, row=1, padx=10, pady=5)
        self.labelcolunas.grid(column=0, row=2, padx=10, pady=5)
        self.entrycolunas.grid(column=0, row=3, padx=10, pady=5)
        self.buttoncriar.grid(column=0, row=4, padx=10, pady=5)

    def criartabela(self):
        nome = self.entrynome.get()
        listacolunas = (self.entrycolunas.get()).split("|")
        self.bancodedados.novatabela(nome, listacolunas)
        self.janelaprincipal.configurarlistbox()
        self.janela.destroy()
