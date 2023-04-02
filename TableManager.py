from tkinter import *
import tkinter.ttk as ttk

class TableManager:

    root = None

    procura = None
    barraprocura = None
    botaoprocura = None

    body = None
    scrollbary = None
    scrollbarx = None
    tree = None
    
    bottom = None
    botaoadicionarlinha = None
    botaoremoverlinha = None
    botaoeditarlinha = None

    def __init__(self):

        self.root = Tk()
        self.root.title('Table Manager')
        self.root.geometry('630x450')
        self.root.resizable(False, False)

        self.barraprocura = Entry(self.root, width=75)
        self.barraprocura.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        self.botaoprocura = Button(self.root, text='Procurar na tabela', command=None, width=15)
        self.botaoprocura.grid(column=2, row=0, padx=10, pady=10)

        self.body = Frame(self.root, height=400)
        self.body.grid(column=0, row=1, columnspan=3, padx=10)
        self.scrollbary = Scrollbar(self.body, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.body, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.body, columns=("Firstname", "Lastname", "Address"), selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set, height=15)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('Firstname', text="Firstname", anchor=W)
        self.tree.heading('Lastname', text="Lastname", anchor=W)
        self.tree.heading('Address', text="Address", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=400)
        self.tree.column('#2', stretch=NO, minwidth=0, width=75)
        self.tree.column('#3', stretch=NO, minwidth=0, width=100)
        self.tree.pack()

        self.bottom = Frame(self.root, height=30)
        self.bottom.grid(column=0, row=2, columnspan=3)
        self.botaoadicionarlinha = Button(self.bottom, text='Adicionar linha', command=None)
        self.botaoadicionarlinha.grid(column=0, row=0, padx=10, pady=10)
        self.botaoaremoverlinha = Button(self.bottom, text='Remover linha', command=None)
        self.botaoaremoverlinha.grid(column=1, row=0, padx=10, pady=10)
        self.botaoeditarlinha = Button(self.bottom, text='Editar linha', command=None)
        self.botaoeditarlinha.grid(column=2, row=0, padx=10, pady=10)


    def run(self):
        self.root.mainloop()

bingos = TableManager()
bingos.run()