import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as dlg
import sqlite3
import os

class BancoDeDados:

    conexao = None
    cursor = None

    def conectar(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

    def execute(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()
    
    def listabelas(self):
        return self.execute('''SELECT name FROM sqlite_master WHERE type='table';''')


class Gui:

    janela = tk.Tk()
    controleabas = ttk.Notebook(janela)
    abas = []
    inicio = None

    def __init__(self):
        self.janela.title('DDM')
        self.janela.geometry('600x320')
        self.janela.resizable(False, False)

        self.iniciarabas()

    def iniciarabas(self):
        self.inicio = Inicio(gui=self, controleabas=self.controleabas)
        self.adicionaraba(self.inicio.frame, 'Início')
        self.controleabas.pack(expand=1, fill="both")

    def adicionaraba(self, tab, name):
        self.abas.append(tab)
        self.controleabas.add(self.abas[len(self.abas) - 1], text=name)

    def sair(self):
        self.janela.destroy()

    def rodar(self):
        self.janela.mainloop()


class Inicio:

    frame = None
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
    listatabelas = ()
    listbox = None
    var = None
    arquivo = None
    gui = None

    def __init__(self, gui, controleabas):
        self.frame = ttk.Frame(controleabas)
        self.botaoabrir = ttk.Button(self.frame, text='Abrir banco de dados', command=self.abrirbancodedados)
        self.botaoabrir.grid(column=0, row=0, padx=10, pady=10)
        self.botaofechar = ttk.Button(self.frame, text='Fechar banco de dados', command=self.fecharbancodedados)
        self.botaofechar.grid(column=1, row=0, padx=10, pady=10)
        self.botaonovo = ttk.Button(self.frame, text='Novo banco de dados', command=None)
        self.botaonovo.grid(column=2, row=0, padx=10, pady=10)
        self.botaodeletar = ttk.Button(self.frame, text='Deletar banco de dados', command=None)
        self.botaodeletar.grid(column=3, row=0, padx=10, pady=10)
        self.buttontableselect = ttk.Button(self.frame, text='Selecionar tabela', command=self.selecionartabela)
        self.buttontableselect.grid(column=1, row=2, padx=10, pady=3)
        self.botaotabelacriar = ttk.Button(self.frame, text='Criar tabela', command=None)
        self.botaotabelacriar.grid(column=1, row=3, padx=10, pady=3)
        self.botaotabeladeletar = ttk.Button(self.frame, text='Deletar tabela', command=None)
        self.botaotabeladeletar.grid(column=1, row=4, padx=10, pady=3)
        self.botaotabelaabrir = ttk.Button(self.frame, text='Abrir tabela', command=None)
        self.botaotabelaabrir.grid(column=1, row=5, padx=10, pady=3)
        self.labelbancodedados = ttk.Label(self.frame, text='Ainda não há nenhum banco de dados aberto.')
        self.labelbancodedados.grid(sticky=tk.W, column=0, row=1, padx=10, pady=10, columnspan=2)
        self.var = tk.StringVar()
        self.var.set(self.listatabelas)
        self.listbox = tk.Listbox(self.frame, listvariable=self.var)
        self.listbox.grid(sticky=tk.W, column=0, row=2, padx=10, pady=15, rowspan=4)
        self.labelframe = tk.LabelFrame(self.frame, text='Informações da tabela selecionada', width=1000, height=220)
        self.labelframe.grid(column=2, row=1, padx=10, pady=10, columnspan=2, rowspan=5)
        self.lablestabela.append(ttk.Label(self.labelframe, text='Nome: '))
        self.lablestabela[0].grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.lablestabela.append(ttk.Label(self.labelframe, text='Número de colunas: '))
        self.lablestabela[1].grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.lablestabela.append(ttk.Label(self.labelframe, text='Número de linhas: '))
        self.lablestabela[2].grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        self.lablestabela.append(ttk.Label(self.labelframe, text='Nome das colunas: ', wraplength=255))
        self.lablestabela[3].grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
        self.gui = gui

    def configurarlistbox(self):
        self.var.set(self.listatabelas)

    def abrirbancodedados(self):
        self.arquivo = dlg.askopenfilename()
        self.labelbancodedados.config(text='Banco de dados: ' + os.path.split(self.arquivo)[1])
        bancodedados.conectar(self.arquivo)
        self.listatabelas = bancodedados.listabelas()
        self.configurarlistbox()

    def fecharbancodedados(self):
        self.labelbancodedados.config(text='O banco de dados foi fechado.')
        self.lablestabela[0].config(text='Nome: ')
        self.listatabelas = ()
        self.configurarlistbox()
        bancodedados.fechar()

    def selecionartabela(self):
        if(self.listbox.curselection() == ()):
            print('Aviso: Não há nenhuma tabela selecionada.')
        else:
            self.lablestabela[0].config(text='Nome: ' + self.listbox.get(self.listbox.curselection()[0])[0])

'''
def cadastro():
    newrow(entry_nome.get(),
           entry_nomecurto.get(),
           entry_sipae.get(),
           entry_email.get(),
           entry_telefone.get())
    entry_nome.delete(0, "end")
    entry_nomecurto.delete(0, "end")
    entry_sipae.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")

class GUIMain:
    __janela = Tk()

    def __init__(self):
        self.__janela.title('DDM')
        self.__janela.geometry('800x600')
        self.__janela.resizable(False, False)

    def __exit(self):
        self.__janela.destroy()
        sqlclose()

    def run(self):
        self.__janela.mainloop()

    label_nome = Label(__janela, text="Nome")
    label_nome.grid(row=0, column=0, padx=10, pady=10)
    global entry_nome
    entry_nome = Entry(__janela, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    label_nomecurto = Label(__janela, text="Nome curto")
    label_nomecurto.grid(row=1, column=0, padx=10, pady=10)
    global entry_nomecurto
    entry_nomecurto = Entry(__janela, width=30)
    entry_nomecurto.grid(row=1, column=1, padx=10, pady=10)

    label_sipae = Label(__janela, text="Sipae")
    label_sipae.grid(row=2, column=0, padx=10, pady=10)
    global entry_sipae
    entry_sipae = Entry(__janela, width=30)
    entry_sipae.grid(row=2, column=1, padx=10, pady=10)

    label_email = Label(__janela, text="email")
    label_email.grid(row=3, column=0, padx=10, pady=10)
    global entry_email
    entry_email = Entry(__janela, width=30)
    entry_email.grid(row=3, column=1, padx=10, pady=10)

    label_telefone = Label(__janela, text="Telefone")
    label_telefone.grid(row=4, column=0, padx=10, pady=10)
    global entry_telefone
    entry_telefone = Entry(__janela, width=30)
    entry_telefone.grid(row=4, column=1, padx=10, pady=10)

    botao_cadastro = Button(__janela, text="Cadastrar Professor", width=40, command=cadastro)

    botao_cadastro.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

main = GUIMain()
main.run()
'''

bancodedados = BancoDeDados()
main = Gui()
main.rodar()
