from utilitaire import *
import random
from math import sqrt
import tkinter as Tk

a = 0
b = 0
c = 0

def LyceePolynomesResult(main, reussi1, reussi2):
    clean(main)
    if reussi1 and reussi2:
        Label(main, text="Tu a trouver les 2 bonnes solution !").pack()
    elif reussi1 and reussi2 == False:
        Label(main, text="Première solution juste , dommage pour la deuxième...").pack()
    elif reussi1 == False and reussi2:
        Label(main, text="Deuxième solution juste , dommage pour la première...").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: LyceePolynomesStart(main)).pack()

def polyresult(main, reussi):
    clean(main)
    if reussi:
        Label(main, text= "Bravo!").pack()
    else :
        Label(main, text= "Perdu...").pack()
    Button(main, text="Encore !", command=lambda: LyceePolynomesStart(main)).pack()

def resultpoly(main, reussi3):
    clean(main)
    if reussi3:
        Label(main, text= "Bravo!").pack()
    else :
        Label(main, text= "Perdu...").pack()
    Button(main, text="Encore !", command=lambda: LyceePolynomesStart(main)).pack()

def LyceePolynomesSecond(main, userInput, delta):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceePolynomesStart(main)).pack()
    if userInput.get() == delta:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
        return
    if delta > 0:
        solution = (-b + sqrt(delta)) / (2 * a)

        solution2 = (-b - sqrt(delta)) / (2 * a)

        Label(main, text=str(a) + " x^2 +" + str(b) + "x +"+ str(c) + "=0").pack()
        Label(main, text="Quel sont les solutions de cette équation? La première solution sera plus grande que la deuxième.").pack()

        Label(main, text="Première solution? On arrondiera le résultat au dizième près.").pack()
        SolutionInput = IntVar()
        Entry(main, textvariable=SolutionInput).pack()

        Label(main, text="Deuxième solution? On arrondiera le résultat au dizième près. ").pack()
        Solution2Input = IntVar()
        Entry(main, textvariable=Solution2Input).pack()

        Button(main, text="Valider", command=lambda: LyceePolynomesResult(main, solution == SolutionInput, solution2 == Solution2Input)).pack()

    elif delta == 0:
        r=-b/(2*a)
        Label(main, text=str(a) + " x^2 +" + str(b) + "x +"+ str(c) + "=0").pack()
        Label(main, text="Quelle est la solution de cette équation?").pack()

        m = IntVar()
        Entry(main, textvariable=m).pack()

        
        Button(main, text="Valider", command=lambda: polyresult(main, m == r)).pack()
        
    elif delta < 0 :
        s=0
        Label(main, text=str(a) + " x^2 +" + str(b) + "x +"+ str(c) + "=0").pack()
        Label(main, text="Quelle est la solution de cette équation?").pack()

        v = IntVar()
        Entry(main, textvariable=v).pack()

        
        Button(main, text="Valider", command=lambda: resultpoly(main, v == s)).pack() 


def LyceePolynomesStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: LyceePolynomesStart(main)).pack()

    global a, b, c

    a = random.randint(1, 50)
    b = random.randint(1, 50)
    c = random.randint(1, 50)

    result = (b ** 2) - (4 * a * c)
    string = str(a) + " x^2 +" + str(b) + "x +"+ str(c) + "=0"
    Label(main, text=string).pack()
    Label(main, text="Quel est le delta de ce polynome ?").pack()
    Label(main, text=result).pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: LyceePolynomesSecond(main, userInput, result)).pack()
