from tkinter import *

class GUI_GED:

    __root = Tk()

    def __init__(self):
        self.__root.title('GED')
        self.__root.geometry('800x600')
        self.__root.resizable(False, False)

    def __exit(self): 
        self.__root.destroy() 

    def run(self): 
        self.__root.mainloop()

main = GUI_GED()
main.run()
