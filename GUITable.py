from tkinter import *
from tkinter import ttk
import sqlite3

class GUITable:

    __root = None
    __mainframe = None
    __connection = None
    __cursor = None
    __treeview = None
    __columns = []
    __xscroll = None
    __yscroll = None

    def __init__(self, databasename, tablename):
        self.__root = Tk()
        self.__root.title(databasename + ' - ' + tablename)
        self.__root.geometry('1200x800')
        self.__root.resizable(True, True)

        self.__frame = Frame(self.__root)
        self.__frame.pack(fill='both', expand=1)

        self.__connection = sqlite3.connect(databasename + '.db')
        self.__cursor = self.__connection.cursor()

        self.__inittreeview(tablename)

    def __inittreeview(self, tablename):

        aux = self.__cursor.execute('SELECT * FROM ' + tablename)
        for i in aux.description:
            self.__columns.append(i[0])

        self.__treeview = ttk.Treeview(self.__frame, columns=self.__columns, show='headings')
        self.__treeview.pack(fill='both')

        for i in self.__columns:
            self.__treeview.column(i, minwidth=50, width=50)
            self.__treeview.heading(i, text=i)

        self.__treeview.pack()

        self.__cursor.execute('SELECT * FROM ' + tablename)
        rows = self.__cursor.fetchall()
        for i in rows:
            self.__treeview.insert('', 'end', values=i)

    def __initscrolls(self):
        #ainda para ser feito

    def __exit(self): 
        self.__root.destroy() 

    def run(self): 
        self.__root.mainloop()
