from tkinter import *

import SQLmain


class GUIMain:

    __root = Tk()

    def __init__(self):
        self.__root.title('DDM')
        self.__root.geometry('800x600')
        self.__root.resizable(False, False)

    def __exit(self):
        SQLmain.SQLclose()
        self.__root.destroy() 

    def run(self): 
        self.__root.mainloop()


SQLmain.SQLmain()

main = GUIMain()
main.run()
