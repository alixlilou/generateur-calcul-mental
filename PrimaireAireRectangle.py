from utilitaire import *
import random
import tkinter as Tk

def AireRectangleResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: AireRectangleStart(main)).pack()


def AireRectangleStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: AireRectangleStart(main)).pack()

    L= random.randint(1, 100)
    l = random.randint(1, 100)

    result = int(l*L)
    string = "Soit le rectangle ABCD, le côté AB vaut"+ str(l)+"cm et le côté AD vaut"+str(L)+"cm." 
    Label(main, text=string).pack()
    Label(main, text= "Quelle est l'aire de ce rectangle ?").pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: AireRectangleResult(main, userInput, result)).pack()

