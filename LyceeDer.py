from utilitaire import *
import random
import tkinter as Tk

def LyceeDerResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: LyceeDerStart(main)).pack()


def LyceeDerStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceeDerStart(main)).pack()

    a= str(random.randint(1, 50))
    b = str(random.randint(1, 50))
    d= random.randint(1,50)
    
    result = str((a*2)+'x+'+b)
    string = "f(x)=" + str(a)+ "x^2+" + str(b)+ " x+ "+str(d)
    Label(main, text=string).pack()
    Label(main, text="Quelle est la dérivée de cette fonction? On donnera la réponse en évitant de mettre des espaces").pack()

    userInput =str( IntVar())

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: LyceeDerResult(main, userInput, result)).pack()


