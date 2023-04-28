from tkinter import *

class GUINovoBancoDeDados:

    janela = None
    labelnome = None
    buttoncriar = None
    bancodedados = None
    janelaprincipal = None
    caminhoarquivo = None

    def __init__(self, bancodedados, janelaprincipal):

        self.bancodedados = bancodedados
        self.janelaprincipal = janelaprincipal

        self.janela = Tk()
        self.labelnome = Label(self.janela, text="Nome do Banco de dados:")
        self.entrynome = Entry(self.janela, width=20)
        self.buttoncriar = Button(self.janela, text="Criar", width=10, command=self.criarbd)

        self.labelnome.grid(column=0, row=0, pady=5)
        self.entrynome.grid(column=0, row=1, pady=5)
        self.buttoncriar.grid(column=0, row=2, pady=5)

    def criarbd(self):
        self.caminhoarquivo = self.entrynome.get()+'.db'
        self.bancodedados.conectar(self.caminhoarquivo)
        self.janelaprincipal.labelbancodedados.config(text='Banco de dados: ' + self.caminhoarquivo)
        self.janelaprincipal.configurarlistbox()
        self.fechar()

    def fechar(self):
        self.janela.destroy()

