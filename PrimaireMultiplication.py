from utilitaire import *
import random
import tkinter as Tk

def PrimaireMultiplicationResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: PrimaireMultiplicationStart(main)).pack()


def PrimaireMultiplicationStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: PrimaireMultiplicationStart(main)).pack()

    nombre1 = random.randint(0, 50)
    nombre2 = random.randint(1, 50)

    result = int(nombre1*nombre2)
    string = str(nombre1) + " x " + str(nombre2) + " = "
    Label(main, text=string).pack()
    Label (main, text= "Quel est le résultat de cette multiplication?").pack()
    
    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: PrimaireMultiplicationResult(main, userInput, result)).pack()

