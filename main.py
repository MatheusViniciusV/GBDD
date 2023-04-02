import tkinter.messagebox
from TableManager import *
from DBManager import *
import os


class GuiInicio:

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

    def __init__(self):

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

    def configurarlistbox(self): 
        self.listatabelas.set(bancodedados.listatabelas())

    def abrirbancodedados(self): 
        self.caminhoarquivo = dlg.askopenfilename()  # abre janela de procurar arquivo
        self.labelbancodedados.config(text='Banco de dados: ' + os.path.split(self.caminhoarquivo)[1])
        bancodedados.conectar(self.caminhoarquivo)
        self.configurarlistbox()

    def fecharbancodedados(self): 

        self.labelbancodedados.config(text='O banco de dados foi fechado.')
        self.lablestabela[0].config(text='Nome: ')
        self.lablestabela[1].config(text='Número de colunas: ')
        self.lablestabela[3].config(text='Nome das colunas: ')

        self.listatabelas.set('')  # esvazia o listbox
        bancodedados.fechar()

    def criarbancodedados(self):

        def criarbd():
            self.caminhoarquivo = entrynome.get()+'.db'
            bancodedados.conectar(self.caminhoarquivo)
            nameroot.destroy()
            self.labelbancodedados.config(text='Banco de dados: ' + self.caminhoarquivo)
            self.configurarlistbox()

        nameroot = Tk()

        labelnome = Label(nameroot, text="Nome do Banco de dados:")
        entrynome = Entry(nameroot, width=20)
        buttoncriar = Button(nameroot, text="criar", width=10, command=criarbd)

        labelnome.grid(column=0, row=0)
        entrynome.grid(column=0, row=1)
        buttoncriar.grid(column=0, row=2)

    def deletarbancodedados(self):

        if tkinter.messagebox.askokcancel(title='Deletar Arquivo', message='Tem certeza que quer deletar esse arquivo?'
                                                                           'Isso não poderá ser desfeito.'):
            self.labelbancodedados.config(text='O banco de dados foi fechado.')
            bancodedados.fechar()
            os.remove(self.caminhoarquivo)

        return

    def selecionartabela(self): 

        if self.listbox.curselection() != ():
            self.nometabela = self.listbox.get(self.listbox.curselection()[0])[0]
            listacolunas = bancodedados.listacolunas(self.nometabela)
            numerocolunas = bancodedados.numerocolunas(self.nometabela)
            
            self.lablestabela[0].config(text='Nome: ' + self.nometabela)
            self.lablestabela[1].config(text='Número de colunas: ' + str(numerocolunas))
            self.lablestabela[3].config(text='Nome das colunas: ' + listacolunas)

            self.tabelaselecionada = True
        else:
            print('Aviso: Não há nenhuma tabela selecionada.')

    def deletartabela(self): 

        if self.tabelaselecionada:
            bancodedados.apagartabela(self.nometabela)
            self.configurarlistbox()
        else:
            print('Aviso: Não há nenhuma tabela selecionada.')

    def abrirtabela(self): 

        if self.tabelaselecionada:
            TableManager(self.nometabela)
        else:
            print('Aviso: Não há nenhuma tabela selecionada.')

    def criartabela(self):
        if bancodedados.conectado:
            TableCreator(bancodedados, self)

    def sair(self): 
        self.janela.destroy()

    def rodar(self): 
        self.janela.mainloop()


bancodedados = BancoDeDados()
main = GuiInicio()
main.rodar()
