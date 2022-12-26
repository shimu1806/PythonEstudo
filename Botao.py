"""

Alterando propriedades, adicionando botões, atribuindo funçoes e configurando

"""

from tkinter import *

def btnClick(mensagem):
    print(mensagem)

menuInicial = Tk()
menuInicial['bg'] = "red" # alter BackGround color
#menuInicial.geometry("500x300+0+0")

# botao

btn1 = Button(menuInicial,
            text="Nome do botao",
            command=lambda: btnClick("Click")
        )
btn1.pack()

btn2 = Button(menuInicial,
            text="Outro botao",
            command=lambda: print("o que é a vida?") # tanto print quanto o def__btnClick__ mostrarão a mensagem
        )
btn2.pack()


# dimensoes da janela
largura = 800
altura = 720

# resolução do nosso sistema]
larguraScreen = menuInicial.winfo_screenwidth() # para retornar valor em pixels
alturaScreen = menuInicial.winfo_screenwidth()

# posição da janela
posx = larguraScreen/2 - largura/2
posy = alturaScreen/2 - altura/2

# definir a geometry
menuInicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))



menuInicial.mainloop()