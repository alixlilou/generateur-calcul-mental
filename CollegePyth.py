from utilitaire import *
import random
import tkinter as Tk
from math import sqrt

def CollegePythResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: CollegePythStart(main)).pack()


def CollegePythStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: CollegePythStart(main)).pack()

    a= random.randint(1, 60)
    b= random.randint(1, 60)
    text= "Nous avons un triangle rectangle noté R, dont le côté adjacent vaut"+str(a)+" cm, et dont le côté opposé vaut "+str(b)+"cm"
    Label(main, text=text).pack()
    Label(main, text="Quelle est la mesure, en cm, de l'hypoténuse du triangle T?").pack()
    result=sqrt((a**2)+(b**2))
    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: CollegePythResult(main, userInput, result)).pack()

