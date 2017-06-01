from utilitaire import *
import random
from math import sqrt
import tkinter as Tk

a = 0
b = 0
result = 0

def LyceeComplexeResult(main, SinInput, Resultat):
    clean(main)

    print(Resultat)
    if SinInput.get() == Resultat:
        Label(main, text="Bravo !").pack()
    else:
        Label(main, text="Faux, le sinus est:" + str(Resultat)).pack()

    Button(main, text="Encore !", command=lambda: LyceeComplexeStart(main)).pack()

def LyceeComplexeThird(main, CosInput, resultat):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceeComplexeStart(main)).pack()

    global result

    if CosInput.get() == resultat:
        Label(main, text="Bravo !").pack()
    else:
        Label(main, text="Faux, le cosinus est: " + str(resultat)).pack()
        return

    Label(main, text="Quel est le sinus de ce nombre complexe? On arrondira le résultat au centième.").pack()
    sinz = b / result
    sinz = round(sinz, 2)
    print(sinz)
    SinInput = DoubleVar()
    Entry(main, textvariable=SinInput).pack()

    Button(main, text="Valider", command=lambda: LyceeComplexeResult(main, SinInput, sinz)).pack()


def LyceeComplexeSecond(main, userInput, resultat):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceeComplexeStart(main)).pack()

    if userInput.get() == resultat:
        Label(main, text="Bravo !").pack()
    else:
        Label(main, text="Faux, le module est: " + str(resultat)).pack()
        return

    Label(main, text="Quel est le cosinus de ce nombre complexe? On arrondira le résultat au centième.").pack()
    cosz = a / resultat
    cosz = round(cosz, 2)
    print(cosz)
    CosInput = DoubleVar()
    Entry(main, textvariable=CosInput).pack()

    Button(main, text="Valider", command=lambda: LyceeComplexeThird(main, CosInput, cosz)).pack()



def LyceeComplexeStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceeComplexeStart(main)).pack()

    global a, b, result

    a = random.randint(1, 50)
    b = random.randint(1, 50)

    result = sqrt((a ** 2) + (b ** 2))
    resultRounded = int(round(result, 0))
    print(resultRounded)

    Label(main, text="Soit le nombre complexe tel que: Z=" + str(a) + "+i" + str(b)).pack()
    Label(main, text="Quel est le module de ce nombre complexe? On arrondira le résultat à l'unité.").pack()

    userInput = IntVar()
    Entry(main, textvariable=userInput).pack()

    Button(main, text="Valider", command=lambda: LyceeComplexeSecond(main, userInput, resultRounded)).pack()