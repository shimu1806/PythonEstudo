"""

Criando um menu janela no tkinter

"""


from tkinter import *

menuInicial = Tk()
menuInicial.title("Nome da janelinha")
menuInicial.geometry("500x300+0+0")  # size of the janelinha
menuInicial.resizable(1, 1) # se pode mudar o size

# menuInicial.minsize(500, 300)
# menuInicial.maxsize(1280, 920)

menuInicial.state("zoomed") # para janela fullsize
# menuInicial.state("iconic") # para janela pequena

menuInicial.iconbitmap("C:/Users/samuel/PythonTkinter/icon/icone.ico") # tem que ser externção .ico

menuInicial.mainloop()