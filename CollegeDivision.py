from utilitaire import *
import random
import tkinter as Tk

def CollegeDivisionResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: CollegeDivisionStart(main)).pack()


def CollegeDivisionStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: CollegeDivisionStart(main)).pack()

    nombre1 = random.randint(0, 20)
    nombre2 = random.randint(1, 10)

    result = int(round(nombre1 / nombre2, 0))
    string = str(nombre1) + " / " + str(nombre2) + " = "
    Label(main, text=string).pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: CollegeDivisionResult(main, userInput, result)).pack()
