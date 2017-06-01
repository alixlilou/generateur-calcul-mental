from utilitaire import *
import random
import tkinter as Tk

def PrimaireSoustractionResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: PrimaireSoustractionStart(main)).pack()


def PrimaireSoustractionStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: PrimaireSoustractionStart(main)).pack()

    nombre1 = random.randint(0, 50)
    nombre2 = random.randint(1, 50)

    result = int(nombre1-nombre2)
    string = str(nombre1) + " - " + str(nombre2) + " = "
    Label(main, text=string).pack()
    Label (main, text= "Quel est le résultat de cette soustraction?").pack()
    
    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: PrimaireSoustractionResult(main, userInput, result)).pack()

