import tkinter.messagebox
from GUITabela import *
from BancoDeDados import *
from GUINovoBancoDeDados import *
from GUICriarTabela import *
from tkinter import filedialog as dlg
import os

class GUIInicio:

    janela = Tk()

    listbox = None
    listatabelas = None

    botaoabrir = None
    botaofechar = None
    botaonovo = None
    botaodeletar = None
    botaotabelavisualizar = None
    botaotabelacriar = None
    botaotabeladeletar = None
    botaotabelaabrir = None

    labelframe = None
    labelbancodedados = None
    lablestabela = []
    
    caminhoarquivo = None
    nometabela = None

    tabelaselecionada = False

    bancodedados = None

    def __init__(self, bancodedados):

        #janela

        self.janela.title('Início')
        self.janela.geometry('600x300')
        self.janela.resizable(False, False)

        #listbox

        self.listatabelas = StringVar()
        self.listatabelas.set('')
        self.listbox = Listbox(self.janela, listvariable=self.listatabelas)
        self.listbox.grid(sticky=W, column=0, row=2, padx=10, pady=15, rowspan=4)

        #botoes

        self.botaoabrir = Button(self.janela, text='Abrir banco de dados', command=self.abrirbancodedados)
        self.botaofechar = Button(self.janela, text='Fechar banco de dados', command=self.fecharbancodedados)
        self.botaonovo = Button(self.janela, text='Novo banco de dados', command=self.criarbancodedados)
        self.botaodeletar = Button(self.janela, text='Deletar banco de dados', command=self.deletarbancodedados)
        self.buttontableselect = Button(self.janela, text='Selecionar tabela', command=self.selecionartabela)
        self.botaotabelacriar = Button(self.janela, text='Criar tabela', command=self.criartabela)
        self.botaotabeladeletar = Button(self.janela, text='Deletar tabela', command=self.deletartabela)
        self.botaotabelaabrir = Button(self.janela, text='Abrir tabela', command=self.abrirtabela)

        #botoes grid

        self.botaoabrir.grid(column=0, row=0, padx=10, pady=10)
        self.botaofechar.grid(column=1, row=0, padx=10, pady=10)
        self.botaonovo.grid(column=2, row=0, padx=10, pady=10)
        self.botaodeletar.grid(column=3, row=0, padx=10, pady=10)
        self.buttontableselect.grid(column=1, row=2, padx=10, pady=3)
        self.botaotabelacriar.grid(column=1, row=3, padx=10, pady=3)
        self.botaotabeladeletar.grid(column=1, row=4, padx=10, pady=3)
        self.botaotabelaabrir.grid(column=1, row=5, padx=10, pady=3)

        #labels

        self.labelbancodedados = Label(self.janela, text='Ainda não há nenhum banco de dados aberto.')
        self.labelframe = LabelFrame(self.janela, text='Informações da tabela selecionada', width=1000, height=220)
        self.lablestabela.append(Label(self.labelframe, text='Nome: '))
        self.lablestabela.append(Label(self.labelframe, text='Número de colunas: '))
        self.lablestabela.append(Label(self.labelframe, text='Número de linhas: '))
        self.lablestabela.append(Label(self.labelframe, text='Nome das colunas: ', wraplength=255))

        #labels grid

        self.labelbancodedados.grid(sticky=W, column=0, row=1, padx=10, pady=10, columnspan=2)
        self.labelframe.grid(column=2, row=1, padx=10, pady=10, columnspan=2, rowspan=5)
        self.lablestabela[0].grid(column=0, row=0, padx=10, pady=5, sticky=W)
        self.lablestabela[1].grid(column=0, row=1, padx=10, pady=5, sticky=W)
        self.lablestabela[2].grid(column=0, row=2, padx=10, pady=5, sticky=W)
        self.lablestabela[3].grid(column=0, row=3, padx=10, pady=5, sticky=W)

        #banco de dados
        self.bancodedados = bancodedados

    def configurarlistbox(self): 
        self.listatabelas.set(self.bancodedados.listatabelas())

    def abrirbancodedados(self): 
        self.caminhoarquivo = dlg.askopenfilename()  # abre janela de procurar arquivo
        self.labelbancodedados.config(text='Banco de dados: ' + os.path.split(self.caminhoarquivo)[1])
        self.bancodedados.conectar(self.caminhoarquivo)
        self.configurarlistbox()

    def fecharbancodedados(self): 

        self.labelbancodedados.config(text='O banco de dados foi fechado.')
        self.lablestabela[0].config(text='Nome: ')
        self.lablestabela[1].config(text='Número de colunas: ')
        self.lablestabela[3].config(text='Nome das colunas: ')

        self.listatabelas.set('')  # esvazia o listbox
        self.bancodedados.fechar()

    def criarbancodedados(self):
        GUINovoBancoDeDados(self.bancodedados, self)

    def deletarbancodedados(self):

        if self.bancodedados.conectado and tkinter.messagebox.askokcancel(title='Deletar Arquivo', message='Tem certeza que quer deletar esse arquivo?'
                                                                           ' Isso não poderá ser desfeito.'):
            self.bancodedados.fechar()
            os.remove(self.caminhoarquivo)
            self.fecharbancodedados()
            self.labelbancodedados.config(text='O banco de dados foi deletado.')

        return

    def selecionartabela(self): 

        if self.listbox.curselection() != ():
            self.nometabela = self.listbox.get(self.listbox.curselection()[0])[0]
            listacolunas = "(" + ", ".join(self.bancodedados.listacolunas(self.nometabela)) + ")"
            numerocolunas = self.bancodedados.numerocolunas(self.nometabela)
            
            self.lablestabela[0].config(text='Nome: ' + self.nometabela)
            self.lablestabela[1].config(text='Número de colunas: ' + str(numerocolunas))
            self.lablestabela[3].config(text='Nome das colunas: ' + listacolunas)

            self.tabelaselecionada = True
        else:
            tkinter.messagebox.showwarning(message="Selecione uma Tabela")

    def deletartabela(self): 

        if self.tabelaselecionada:
            if tkinter.messagebox.askokcancel(title='Deletar Arquivo', message='Tem certeza que quer deletar esse arquivo?'
                                                                           ' Isso não poderá ser desfeito.'):
                self.bancodedados.apagartabela(self.nometabela)
                self.configurarlistbox()
                self.lablestabela[0].config(text='Nome: ')
                self.lablestabela[1].config(text='Número de colunas: ')
                self.lablestabela[3].config(text='Nome das colunas: ')
        else:
            tkinter.messagebox.showwarning(message="Selecione uma Tabela")

    def abrirtabela(self): 

        if self.tabelaselecionada:
            GUITabela(self.bancodedados, self.nometabela)
        else:
            tkinter.messagebox.showwarning(message="Selecione uma Tabela")

    def criartabela(self):
        if self.bancodedados.conectado:
            GUICriarTabela(self.bancodedados, self)
        else:
            tkinter.messagebox.showwarning(message="Não há nenhum banco de dados selecionado")

    def sair(self): 
        self.janela.destroy()

    def rodar(self): 
        self.janela.mainloop()