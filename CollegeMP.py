from utilitaire import *
import random
import tkinter as Tk

def CollegeMPResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: CollegeMPStart(main)).pack()


def CollegeMPStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: CollegeMPStart(main)).pack()

    i = random.randint(1, 60)
    e= random.randint(1, 60)
    f= random.randint(1,60)

    result = int(e+f)
    string = str(i)+"^" + str(e) + " x " + str(i)+"^" + str(f)+ " = "
    Label(main, text=string).pack()
    Label(main, text="Simplifier cette multiplication en utilisant les propriétés de calcul des puissances. Ne repondre que par la valeur de l'exposant.").pack()
    r= str(i)+"^..."
    Label(main,text= r).pack()
    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: CollegeMPResult(main, userInput, result)).pack()

