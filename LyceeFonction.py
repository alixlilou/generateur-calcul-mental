from utilitaire import *
import random
import tkinter as Tk

def LyceeFonctionResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: LyceeFonctionStart(main)).pack()


def LyceeFonctionStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceeFonctionStart(main)).pack()

    n= float( random.randint(1, 100))
    u = float(random.randint(1, 100))
    d= float( random.randint(1,100))
    r= random.randint(1,100)
    
    result = (round(((n*r**2)+u*r)/d),1)
    string = "f(x)=(" + str(n)+ "x^2+" + str(u) + "x)/ "+str(d)
    Label(main, text=string).pack()
    choix= "Quel est la valeur de f("+str(r)+")?Arrondir le résultat au dixième près."
    Label(main, text=choix).pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: LyceeFonctionResult(main, userInput, result)).pack()

