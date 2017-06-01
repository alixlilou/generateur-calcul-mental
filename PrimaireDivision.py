from utilitaire import *
import random
import tkinter as Tk

def PrimaireDivisionResult(main, reussi1, reussi2):
    clean(main)
    if reussi1 and reussi2:
        Label(main, text="Bravo !").pack()
    elif reussi1 and reussi2 == False:
        Label(main, text="Le quotient est juste , dommage pour le reste...").pack()
    elif reussi1 == False and reussi2:
        Label(main, text="Le reste est juste , dommage pour le quotient...").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: PrimaireDivisionStart(main)).pack()

    

def PrimaireDivisionStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: PrimaireDivisionStart(main)).pack()

    nombre1 = random.randint(0, 20)
    nombre2 = random.randint(1, 10)

    result = int(nombre1 // nombre2)
    reste= int(nombre1 % nombre2)
    
    string = str(nombre1) + " / " + str(nombre2) + " = "
    Label(main, text=string).pack()
    Label(main,text= "Quel est le quotient de cette division?").pack()
    userInput = IntVar()
    Entry(main, textvariable=userInput).pack()
    Label(main,text="Quel est le reste de cette division?").pack()
    y=IntVar()
    Entry(main, textvariable= y).pack()
    Button(main, text="Valider", command=lambda: PrimaireDivisionResult(main, userInput==result, y==reste)).pack()

