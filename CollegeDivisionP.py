from utilitaire import *
import random
import tkinter as Tk

def CollegeDivisionPResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: CollegeDivisionPStart(main)).pack()


def CollegeDivisionPStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: CollegeDivisionPStart(main)).pack()

    i = random.randint(1, 60)
    e= random.randint(1, 60)
    f= random.randint(1,60)

    result = int(e-f)
    string = str(i)+"^" + str(e) + " / " + str(i)+"^" + str(f)+ " = "
    Label(main, text=string).pack()
    Label(main, text="Simplifier cette division en utilisant les propriétés de calcul des puissances. Ne repondre que par la valeur de l'exposant.").pack()
    r= str(i)+"^..."
    Label(main,text= r).pack()
    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: CollegeDivisionPResult(main, userInput, result)).pack()
