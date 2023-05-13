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
    lista_tabelas = None

    botao_abrir = None
    botao_fechar = None
    botao_novo = None
    botao_deletar = None
    botao_tabela_visualizar = None
    botao_tabela_criar = None
    botao_tabela_deletar = None
    botao_tabela_abrir = None

    labelframe = None
    label_banco_de_dados = None
    labels_tabela = []
    
    caminho_arquivo = None
    nome_tabela = None

    tabela_selecionada = False

    banco_de_dados = None

    def __init__(self, banco_de_dados):

        #janela

        self.janela.title('Início')
        self.janela.geometry('600x300')
        self.janela.resizable(False, False)

        #listbox

        self.lista_tabelas = StringVar()
        self.lista_tabelas.set('')
        self.listbox = Listbox(self.janela, listvariable=self.lista_tabelas)
        self.listbox.grid(sticky=W, column=0, row=2, padx=10, pady=15, rowspan=4)

        #botoes

        self.botao_abrir = Button(self.janela, text='Abrir banco de dados', command=self.abrir_banco_de_dados)
        self.botao_fechar = Button(self.janela, text='Fechar banco de dados', command=self.fechar_banco_de_dados)
        self.botao_novo = Button(self.janela, text='Novo banco de dados', command=self.criar_banco_de_dados)
        self.botao_deletar = Button(self.janela, text='Deletar banco de dados', command=self.deletar_banco_de_dados)
        self.buttontableselect = Button(self.janela, text='Selecionar tabela', command=self.selecionar_tabela)
        self.botao_tabela_criar = Button(self.janela, text='Criar tabela', command=self.criar_tabela)
        self.botao_tabela_deletar = Button(self.janela, text='Deletar tabela', command=self.deletar_tabela)
        self.botao_tabela_abrir = Button(self.janela, text='Abrir tabela', command=self.abrir_tabela)

        #botoes grid

        self.botao_abrir.grid(column=0, row=0, padx=10, pady=10)
        self.botao_fechar.grid(column=1, row=0, padx=10, pady=10)
        self.botao_novo.grid(column=2, row=0, padx=10, pady=10)
        self.botao_deletar.grid(column=3, row=0, padx=10, pady=10)
        self.buttontableselect.grid(column=1, row=2, padx=10, pady=3)
        self.botao_tabela_criar.grid(column=1, row=3, padx=10, pady=3)
        self.botao_tabela_deletar.grid(column=1, row=4, padx=10, pady=3)
        self.botao_tabela_abrir.grid(column=1, row=5, padx=10, pady=3)

        #labels

        self.label_banco_de_dados = Label(self.janela, text='Ainda não há nenhum banco de dados aberto.')
        self.labelframe = LabelFrame(self.janela, text='Informações da tabela selecionada', width=1000, height=220)
        self.labels_tabela.append(Label(self.labelframe, text='Nome: '))
        self.labels_tabela.append(Label(self.labelframe, text='Número de colunas: '))
        self.labels_tabela.append(Label(self.labelframe, text='Número de linhas: '))
        self.labels_tabela.append(Label(self.labelframe, text='Nome das colunas: ', wraplength=255))

        #labels grid

        self.label_banco_de_dados.grid(sticky=W, column=0, row=1, padx=10, pady=10, columnspan=2)
        self.labelframe.grid(column=2, row=1, padx=10, pady=10, columnspan=2, rowspan=5)
        self.labels_tabela[0].grid(column=0, row=0, padx=10, pady=5, sticky=W)
        self.labels_tabela[1].grid(column=0, row=1, padx=10, pady=5, sticky=W)
        self.labels_tabela[2].grid(column=0, row=2, padx=10, pady=5, sticky=W)
        self.labels_tabela[3].grid(column=0, row=3, padx=10, pady=5, sticky=W)

        #banco de dados
        self.banco_de_dados = banco_de_dados

    def configurar_listbox(self): 
        self.lista_tabelas.set(self.banco_de_dados.lista_tabelas())

    def abrir_banco_de_dados(self): 
        self.caminho_arquivo = dlg.askopenfilename()  # abre janela de procurar arquivo
        self.label_banco_de_dados.config(text='Banco de dados: ' + os.path.split(self.caminho_arquivo)[1])
        self.banco_de_dados.conectar(self.caminho_arquivo)
        self.configurar_listbox()

    def fechar_banco_de_dados(self): 

        self.label_banco_de_dados.config(text='O banco de dados foi fechado.')
        self.labels_tabela[0].config(text='Nome: ')
        self.labels_tabela[1].config(text='Número de colunas: ')
        self.labels_tabela[3].config(text='Nome das colunas: ')

        self.lista_tabelas.set('')  # esvazia o listbox
        self.banco_de_dados.fechar()

    def criar_banco_de_dados(self):
        GUINovoBancoDeDados(self.banco_de_dados, self)

    def deletar_banco_de_dados(self):

        if self.banco_de_dados.conectado and tkinter.messagebox.askokcancel(title='Deletar Arquivo', message='Tem certeza que quer deletar esse arquivo?'
                                                                           ' Isso não poderá ser desfeito.'):
            self.banco_de_dados.fechar()
            os.remove(self.caminho_arquivo)
            self.fechar_banco_de_dados()
            self.label_banco_de_dados.config(text='O banco de dados foi deletado.')

        return

    def selecionar_tabela(self): 

        if self.listbox.curselection() != ():
            self.nome_tabela = self.listbox.get(self.listbox.curselection()[0])[0]
            lista_colunas = "(" + ", ".join(self.banco_de_dados.lista_colunas(self.nome_tabela)) + ")"
            numero_colunas = self.banco_de_dados.numero_colunas(self.nome_tabela)
            
            self.labels_tabela[0].config(text='Nome: ' + self.nome_tabela)
            self.labels_tabela[1].config(text='Número de colunas: ' + str(numero_colunas))
            self.labels_tabela[3].config(text='Nome das colunas: ' + lista_colunas)

            self.tabela_selecionada = True
        else:
            tkinter.messagebox.showwarning(message="Selecione uma Tabela")

    def deletar_tabela(self): 

        if self.tabela_selecionada:
            if tkinter.messagebox.askokcancel(title='Deletar Arquivo', message='Tem certeza que quer deletar esse arquivo?'
                                                                           ' Isso não poderá ser desfeito.'):
                self.banco_de_dados.apagar_tabela(self.nome_tabela)
                self.configurar_listbox()
                self.labels_tabela[0].config(text='Nome: ')
                self.labels_tabela[1].config(text='Número de colunas: ')
                self.labels_tabela[3].config(text='Nome das colunas: ')
        else:
            tkinter.messagebox.showwarning(message="Selecione uma Tabela")

    def abrir_tabela(self): 

        if self.tabela_selecionada:
            GUITabela(self.banco_de_dados, self.nome_tabela)
        else:
            tkinter.messagebox.showwarning(message="Selecione uma Tabela")

    def criar_tabela(self):
        if self.banco_de_dados.conectado:
            GUICriarTabela(self.banco_de_dados, self)
        else:
            tkinter.messagebox.showwarning(message="Não há nenhum banco de dados selecionado")

    def sair(self): 
        self.janela.destroy()

    def rodar(self): 
        self.janela.mainloop()
