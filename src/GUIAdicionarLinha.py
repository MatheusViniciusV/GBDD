from tkinter import *

class GUIAdicionarLinha:

    janela = None
    labellinha = None
    entrylinha = None
    buttoncriar = None
    bancodedados = None
    janelaprincipal = None
    tabela = None

    def __init__(self, bancodedados, janelaprincipal, tabela):

        self.bancodedados = bancodedados
        self.janelaprincipal = janelaprincipal
        self.tabela = tabela

        self.janela = Tk()
        self.janela.title('Inserir linha na tabela')
        self.janela.resizable(False, False)

        self.labellinha = Label(self.janela, text="Digite os valores para serem inseridos usando \'|\' para separá-los:")
        self.entrylinha = Entry(self.janela, width=75)
        self.buttoncriar = Button(self.janela, text="Inserir", width=10, command=self.inserir)

        self.labellinha.grid(column=0, row=0, padx=10, pady=10)
        self.entrylinha.grid(column=0, row=1, padx=10, pady=10)
        self.buttoncriar.grid(column=0, row=2, padx=10, pady=10)

    def inserir(self):
        linha = (self.entrylinha.get()).split("|")
        self.bancodedados.inserirnatabela(self.tabela, linha)
        self.janelaprincipal.tree.insert("", END, values=linha)
        self.janela.destroy()
