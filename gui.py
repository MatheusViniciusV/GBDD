import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as dlg
import os

class Inicio:

    frame = None
    buttonopen = None
    buttonclose = None
    buttonnew = None
    buttondelete = None
    buttontablecreate = None
    buttontabledelete = None
    buttontableopen = None
    stringvarlabeldb = None
    labelframe = None
    labeldb = None
    lablestable = []
    listtables = ()
    listbox = None
    var = None
    file = None
    gui = None

    def __init__(self, gui, tabcontrol):
        self.frame = ttk.Frame(tabcontrol)
        self.buttonopen = ttk.Button(self.frame, text='Abrir banco de dados', command=self.opendb).grid(column=0, row=0, padx=10, pady=10)
        self.buttonclose = ttk.Button(self.frame, text='Fechar banco de dados', command=self.closedb).grid(column=1, row=0, padx=10, pady=10)
        self.buttonnew = ttk.Button(self.frame, text='Novo banco de dados', command=None).grid(column=2, row=0, padx=10, pady=10)
        self.buttondelete = ttk.Button(self.frame, text='Deletar banco de dados', command=None).grid(column=3, row=0, padx=10, pady=10)
        self.buttontablecreate = ttk.Button(self.frame, text='Criar tabela', command=None).grid(sticky=tk.S,column=1, row=2, padx=10, pady=10)
        self.buttontabledelete = ttk.Button(self.frame, text='Deletar tabela', command=None).grid(column=1, row=3, padx=10, pady=10)
        self.buttontableopen = ttk.Button(self.frame, text='Abrir tabela', command=None).grid(sticky=tk.N, column=1, row=4, padx=10, pady=10)
        self.stringvarlabeldb = tk.StringVar()
        self.stringvarlabeldb.set('Ainda não há nenhum banco de dados aberto.')
        self.labeldb = ttk.Label(self.frame, textvariable=self.stringvarlabeldb).grid(sticky=tk.W, column=0, row=1, padx=10, pady=10, columnspan=2)
        self.var = tk.StringVar()
        self.var.set(self.listtables)
        self.listbox = tk.Listbox(self.frame, listvariable=self.var).grid(sticky=tk.W,column=0, row=2, padx=10, pady=15, rowspan=3)
        self.labelframe = tk.LabelFrame(self.frame, text='Informações da tabela selecionada', width=280, height=220).grid(column=2, row=1, padx=10, pady=10, columnspan=2, rowspan=4)
        self.lablestable.append(ttk.Label(self.labelframe, text='Nome: ').place(x=312, y=100))
        self.lablestable.append(ttk.Label(self.labelframe, text='Número de colunas: ').place(x=312, y=120))
        self.lablestable.append(ttk.Label(self.labelframe, text='Número de linhas: ').place(x=312, y=140))
        self.lablestable.append(ttk.Label(self.labelframe, text='Nome das colunas: ', wraplength=265).place(x=312, y=160))
        self.gui = gui
        
    def configlistbox(self):
        for i in self.listtables:
            self.listbox.insert('end', i)

    def opendb(self):
        self.file = dlg.askopenfilename();
        self.stringvarlabeldb.set('Banco de dados: ' + os.path.split(self.file)[1])
    
    def closedb(self):
        self.stringvarlabeldb.set('Ainda não há nenhum banco de dados aberto.')


class Gui:

    root = tk.Tk()
    tabcontrol = ttk.Notebook(root)
    tabs = []
    inicio = None

    def __init__(self):
        self.root.title('DDM')
        self.root.geometry('600x320')
        self.root.resizable(False, False)

        self.inittabs()

    def inittabs(self):
        self.inicio = Inicio(gui=self, tabcontrol=self.tabcontrol)
        self.addtab(self.inicio.frame, 'Início')
        self.tabcontrol.pack(expand=1, fill="both")

    def addtab(self, tab, name):
        self.tabs.append(tab)
        self.tabcontrol.add(self.tabs[len(self.tabs) - 1], text=name)

    def exit(self):
        self.root.destroy() 

    def run(self): 
        self.root.mainloop()
