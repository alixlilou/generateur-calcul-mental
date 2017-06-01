from utilitaire import *
import random
import tkinter as Tk

def AireTQResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: AireTQStart(main)).pack()


def AireTQStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: AireTQStart(main)).pack()

    L= random.randint(0, 20)
    h= random.randint(1, 10)

    result = int(round((L*h)/ 2, 0))
    string = "Soit le triangle ABC, sa base AB vaut"+str(L)+"cm et et sa hauteur vaut"+str(h)+"cm." 
    Label(main, text=string).pack()
    Label(main, text="Quelle est l'aire de ce triangle?").pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: AireTQResult(main, userInput, result)).pack()

