import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as dlg


class EditableListbox(Listbox):
    """A listbox where you can directly edit an item via double-click"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.edit_item = None
        self.bind("<Double-1>", self._start_edit)

    def _start_edit(self, event):
        index = self.index(f"@{event.x},{event.y}")
        self.start_edit(index)
        return "break"

    def start_edit(self, index):
        self.edit_item = index
        text = self.get(index)
        y0 = self.bbox(index)[1]
        entry = Entry(self, borderwidth=0, highlightthickness=1)
        entry.bind("<Return>", self.accept_edit)
        entry.bind("<Escape>", self.cancel_edit)

        entry.insert(0, text)
        entry.selection_from(0)
        entry.selection_to("end")
        entry.place(relx=0, y=y0, relwidth=1, width=-1)
        entry.focus_set()
        entry.grab_set()

    def cancel_edit(self, event):
        event.widget.destroy()

    def accept_edit(self, event):
        new_data = event.widget.get()
        self.delete(self.edit_item)
        self.insert(self.edit_item, new_data)
        event.widget.destroy()


class TableManager:

    root = None

    def __init__(self):
        self.root = Tk()
        self.root.title('Table Manager')
        self.root.geometry('680x400')
        self.root.resizable(False, False)


def validate(action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type, widget_name):
    if value_if_allowed:
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False


class TableCreator:

    root = None
    frame = None
    lb = None
    listboxlabels = None
    nomeentry = None
    columnsentry = None
    bdm = None

    def __init__(self, bdm):
        #init settings
        self.bdm = bdm
        self.frame = Frame()
        self.root = Tk()
        self.root.title('Table Creator')
        self.root.geometry('360x170')
        self.root.resizable(False, False)

        #validation command
        vcmd = (self.root.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        #button
        createbutton = Button(self.root, text="Criar Tabela", command=self.criartabela)

        #entrys
        self.columnsentry = Entry(self.root, width=4, validate='key', validatecommand=vcmd)
        self.nomeentry = Entry(self.root, width=20)

        #labels
        columnslabel = Label(self.root, text="Numero de\nColunas:", width=10, height=2)
        listboxlabel = Label(self.root, text="Colunas:", width=10, height=2)
        nomelabel = Label(self.root, text="Nome:", width=10, height=2)

        #listboxes
        self.lb = EditableListbox(self.root, height=3, font=30)

        #grids
        createbutton.grid(column=3, row=3, padx=10, pady=10, sticky="s")

        columnslabel.grid(column=1, row=0, padx=10, pady=1)
        listboxlabel.grid(column=1, row=2, padx=10, pady=1)
        nomelabel.grid(column=3, row=0, padx=10, pady=1)

        self.columnsentry.grid(column=1, row=1, padx=10, pady=1)
        self.nomeentry.grid(column=3, row=1, padx=20, pady=1)

        self.lb.grid(column=0, row=3, columnspan=3, padx=10)

        #lb template
        for i in range(3):
            self.lb.insert("end", f"Item #{i + 1}")

        def updatelistbox():
            #lb update
            self.lb.destroy()
            self.lb = EditableListbox(self.root, height=min(int(self.columnsentry.get()), 10), font=30)
            self.lb.grid(column=0, row=3, columnspan=3, padx=10)

            #window update
            self.root.geometry("360x" + str(110+min(int(self.columnsentry.get()), 10)*20))

            #lb template update
            for i in range(min(int(self.columnsentry.get()), 10)):
                self.lb.insert("end", f"Item #{i + 1}")

            #warning check
            if int(self.columnsentry.get()) > 10:
                tkinter.messagebox.showwarning(title="Máximo excedido", message="Você ultrapassou o limite de 10 "
                                                                                "colunas")

        def entrylostfocus(event):
            self.root.focus_force()
            updatelistbox()
            print(int(self.columnsentry.get()))

        self.columnsentry.bind("<Return>", entrylostfocus)

    def criartabela(self):
        listacolunas = []

        for i in range(int(self.columnsentry.get())):
            listacolunas.insert(i, self.lb.get(i))

        self.bdm.newtable(self.nomeentry.get(), listacolunas)