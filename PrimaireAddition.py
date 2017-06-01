from utilitaire import *
import random
import tkinter as Tk

def PrimaireAdditionResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: PrimaireAdditionStart(main)).pack()


def PrimaireAdditionStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: PrimaireAdditionStart(main)).pack()

    nombre1 = random.randint(0, 1000)
    nombre2 = random.randint(1, 100)

    result = int(round(nombre1 + nombre2, 0))
    string = str(nombre1) + " +" + str(nombre2) + " = "
    Label(main, text=string).pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: PrimaireAdditionResult(main, userInput, result)).pack()

