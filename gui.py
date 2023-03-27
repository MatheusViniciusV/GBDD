import tkinter as tk
from tkinter import ttk

connection = None
cursor = None

class Inicio:

    frame = None
    buttonopen = None
    buttonclose = None
    buttonnew = None
    buttondelete = None
    labelframe = None
    labeldb = None
    lablestable = []
    listtables = ()
    listbox = None
    var = None

    def __init__(self, tabcontrol):
        self.frame = ttk.Frame(tabcontrol)
        self.buttonopen = ttk.Button(self.frame, text='Abrir banco de dados', command=None).grid(column=0, row=0, padx=10, pady=10)
        self.buttonclose = ttk.Button(self.frame, text='Fechar banco de dados', command=None).grid(column=1, row=0, padx=10, pady=10)
        self.buttonnew = ttk.Button(self.frame, text='Novo banco de dados', command=None).grid(column=2, row=0, padx=10, pady=10)
        self.buttondelete = ttk.Button(self.frame, text='Deletar banco de dados', command=None).grid(column=3, row=0, padx=10, pady=10)
        self.label = ttk.Label(self.frame, text='Ainda não há um banco de dados aberto.').grid(sticky=tk.W, column=0, row=1, padx=10, pady=10, columnspan=2)
        self.var = tk.StringVar()
        self.var.set(self.listtables)
        self.listbox = tk.Listbox(self.frame, listvariable=self.var).grid(sticky=tk.W,column=0, row=2, padx=10, pady=15, columnspan=2, rowspan=3)
        self.labelframe = tk.LabelFrame(self.frame, text='Informações da tabela selecionada', width=280, height=220).grid(column=2, row=1, padx=10, pady=10, columnspan=2, rowspan=4)
        self.lablestable.append(ttk.Label(self.labelframe, text='Nome: ').place(x=312, y=100))
        self.lablestable.append(ttk.Label(self.labelframe, text='Número de colunas: ').place(x=312, y=120))
        self.lablestable.append(ttk.Label(self.labelframe, text='Número de linhas: ').place(x=312, y=140))
        self.lablestable.append(ttk.Label(self.labelframe, text='Nome das colunas: ').place(x=312, y=160))
        
    def initlistbox(self):
        for i in self.listtables:
            self.listbox.insert('end', i)


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
        self.inicio = Inicio(tabcontrol=self.tabcontrol)
        self.addtab(self.inicio.frame, 'Início')
        self.tabcontrol.pack(expand=1, fill="both")

    def addtab(self, tab, name):
        self.tabs.append(tab)
        self.tabcontrol.add(self.tabs[len(self.tabs) - 1], text=name)

    def exit(self):
        self.root.destroy() 

    def run(self): 
        self.root.mainloop()
