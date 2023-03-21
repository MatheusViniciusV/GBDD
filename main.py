from tkinter import *
from SQLmain import *

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
