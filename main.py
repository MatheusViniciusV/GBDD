from tkinter import *
from tkinter import ttk
from tkinter import filedialog as dlg
from DBManager import *
from TableManager import *
import os


class Gui:

    root = Tk()
    controleabas = ttk.Notebook(root)
    abas = []
    inicio = None

    def __init__(self):
        self.root.title('DDM')
        self.root.geometry('600x320')
        self.root.resizable(False, False)

        self.iniciarabas()

    def iniciarabas(self):
        self.inicio = Inicio(gui=self, controleabas=self.controleabas)
        self.adicionaraba(self.inicio.frame, 'Início')
        self.controleabas.pack(expand=1, fill="both")

    def adicionaraba(self, tab, name):
        self.abas.append(tab)
        self.controleabas.add(self.abas[len(self.abas) - 1], text=name)

    def sair(self):
        self.root.destroy()

    def rodar(self):
        self.root.mainloop()


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
    table = None

    def __init__(self, gui, controleabas):

        #vars

        self.frame = Frame(controleabas)
        self.var = StringVar()
        self.var.set(self.listatabelas)
        self.gui = gui
        self.listbox = Listbox(self.frame, listvariable=self.var)
        self.listbox.grid(sticky=W, column=0, row=2, padx=10, pady=15, rowspan=4)

        #buttons

        self.botaoabrir = Button(self.frame, text='Abrir banco de dados', command=self.abrirbancodedados)
        self.botaofechar = Button(self.frame, text='Fechar banco de dados', command=self.fecharbancodedados)
        self.botaonovo = Button(self.frame, text='Novo banco de dados', command=None)
        self.botaodeletar = Button(self.frame, text='Deletar banco de dados', command=None)
        self.buttontableselect = Button(self.frame, text='Selecionar tabela', command=self.selecionartabela)
        self.botaotabelacriar = Button(self.frame, text='Criar tabela', command=self.criartabela)
        self.botaotabeladeletar = Button(self.frame, text='Deletar tabela', command=self.deletartabela)
        self.botaotabelaabrir = Button(self.frame, text='Abrir tabela', command=self.abrirtabela)
        self.labelbancodedados = Label(self.frame, text='Ainda não há nenhum banco de dados aberto.')

        #buttons grid

        self.botaoabrir.grid(column=0, row=0, padx=10, pady=10)
        self.botaofechar.grid(column=1, row=0, padx=10, pady=10)
        self.botaonovo.grid(column=2, row=0, padx=10, pady=10)
        self.botaodeletar.grid(column=3, row=0, padx=10, pady=10)
        self.buttontableselect.grid(column=1, row=2, padx=10, pady=3)
        self.botaotabelacriar.grid(column=1, row=3, padx=10, pady=3)
        self.botaotabeladeletar.grid(column=1, row=4, padx=10, pady=3)
        self.botaotabelaabrir.grid(column=1, row=5, padx=10, pady=3)
        self.labelbancodedados.grid(sticky=W, column=0, row=1, padx=10, pady=10, columnspan=2)

        #labels

        self.labelframe = LabelFrame(self.frame, text='Informações da tabela selecionada', width=1000, height=220)
        self.lablestabela.append(Label(self.labelframe, text='Nome: '))
        self.lablestabela.append(Label(self.labelframe, text='Número de colunas: '))
        self.lablestabela.append(Label(self.labelframe, text='Número de linhas: '))
        self.lablestabela.append(Label(self.labelframe, text='Nome das colunas: ', wraplength=255))

        #labels grid

        self.labelframe.grid(column=2, row=1, padx=10, pady=10, columnspan=2, rowspan=5)
        self.lablestabela[0].grid(column=0, row=0, padx=10, pady=5, sticky=W)
        self.lablestabela[1].grid(column=0, row=1, padx=10, pady=5, sticky=W)
        self.lablestabela[2].grid(column=0, row=2, padx=10, pady=5, sticky=W)
        self.lablestabela[3].grid(column=0, row=3, padx=10, pady=5, sticky=W)

    def configurarlistbox(self):

        self.var.set(self.listatabelas)

    def abrirbancodedados(self):

        self.arquivo = dlg.askopenfilename()
        self.labelbancodedados.config(text='Banco de dados: ' + os.path.split(self.arquivo)[1])
        bancodedados.conectar(self.arquivo)
        self.listatabelas = bancodedados.listtables()
        self.configurarlistbox()
        bancodedados.connected = True

    def fecharbancodedados(self):

        self.labelbancodedados.config(text='O banco de dados foi fechado.')
        self.lablestabela[0].config(text='Nome: ')
        self.listatabelas = ()
        self.configurarlistbox()
        bancodedados.fechar()

    def selecionartabela(self):

        if self.listbox.curselection() != ():
            self.table = self.listbox.get(self.listbox.curselection()[0])[0]
            self.lablestabela[0].config(text='Nome: ' + self.listbox.get(self.listbox.curselection()[0])[0])
        else:
            print('Aviso: Não há nenhuma tabela selecionada.')

    def deletartabela(self):

        if self.listbox.curselection() != ():
            bancodedados.droptables(self.table)
            self.listatabelas = bancodedados.listtables()
            self.configurarlistbox()
        else:
            print('Aviso: Não há nenhuma tabela selecionada.')

    def abrirtabela(self):
        if self.listbox.curselection() != ():
            TableManager()
        else:
            print('Aviso: Não há nenhuma tabela selecionada.')

    def criartabela(self):
        #if bancodedados.connected:
        TableCreator(bancodedados)







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
    __root = Tk()

    def __init__(self):
        self.__root.title('DDM')
        self.__root.geometry('800x600')
        self.__root.resizable(False, False)

    def __exit(self):
        self.__root.destroy()
        sqlclose()

    def run(self):
        self.__root.mainloop()

    label_nome = Label(__root, text="Nome")
    label_nome.grid(row=0, column=0, padx=10, pady=10)
    global entry_nome
    entry_nome = Entry(__root, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    label_nomecurto = Label(__root, text="Nome curto")
    label_nomecurto.grid(row=1, column=0, padx=10, pady=10)
    global entry_nomecurto
    entry_nomecurto = Entry(__root, width=30)
    entry_nomecurto.grid(row=1, column=1, padx=10, pady=10)

    label_sipae = Label(__root, text="Sipae")
    label_sipae.grid(row=2, column=0, padx=10, pady=10)
    global entry_sipae
    entry_sipae = Entry(__root, width=30)
    entry_sipae.grid(row=2, column=1, padx=10, pady=10)

    label_email = Label(__root, text="email")
    label_email.grid(row=3, column=0, padx=10, pady=10)
    global entry_email
    entry_email = Entry(__root, width=30)
    entry_email.grid(row=3, column=1, padx=10, pady=10)

    label_telefone = Label(__root, text="Telefone")
    label_telefone.grid(row=4, column=0, padx=10, pady=10)
    global entry_telefone
    entry_telefone = Entry(__root, width=30)
    entry_telefone.grid(row=4, column=1, padx=10, pady=10)

    botao_cadastro = Button(__root, text="Cadastrar Professor", width=40, command=cadastro)

    botao_cadastro.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

main = GUIMain()
main.run()
'''

bancodedados = BancoDeDados()
main = Gui()
main.rodar()
