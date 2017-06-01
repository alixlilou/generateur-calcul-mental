from utilitaire import *
import random
import tkinter as Tk

def CollegeFonctionResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: CollegeFonctionStart(main)).pack()


def CollegeFonctionStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: CollegeFonctionStart(main)).pack()

    i= random.randint(1, 120)
    e = random.randint(1, 120)
    x= random.randint(1,120)
    
    result = int(round((i*x)+e, 0))
    string = "f(x)=" + str(i)+ "x+" + str(e) + " = "
    Label(main, text=string).pack()
    choix= "Quel est la valeur de f("+str(x)+")?"
    Label(main, text=choix).pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: CollegeFonctionResult(main, userInput, result)).pack()

