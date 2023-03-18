from tkinter import *
from tkinter import ttk
import sqlite3

class GUITable:

    __root = None
    __frame = None
    __connection = None
    __cursor = None
    __treeview = None
    __columns = []

    def __init__(self, dataBaseName, tableName):
        self.__root = Tk()
        self.__root.title(dataBaseName + ' - ' + tableName)
        self.__root.geometry('600x400')
        self.__root.resizable(True, True)

        self.__frame = LabelFrame(self.__root, text=dataBaseName + ' - ' + tableName)
        self.__frame.pack(fill='both', expand='yes', padx=10, pady=10)

        self.__connection = sqlite3.connect(dataBaseName + '.db')
        self.__cursor = self.__connection.cursor()

        self.__initTreeview(tableName)

    def __initTreeview(self, tableName):

        aux = self.__cursor.execute('SELECT * FROM ' + tableName)
        for i in aux.description:
            self.__columns.append(i[0])

        self.__treeview = ttk.Treeview(self.__frame, columns=self.__columns, show='headings')

        for i in self.__columns:
            self.__treeview.column(i, minwidth=50)
            self.__treeview.heading(i, text=i)

        self.__treeview.pack()

        self.__cursor.execute('SELECT * FROM ' + tableName)
        rows = self.__cursor.fetchall()
        for i in rows:
            self.__treeview.insert('', 'end', values=i)

    def __exit(self): 
        self.__root.destroy() 

    def run(self): 
        self.__root.mainloop()
