from utilitaire import *
import random
import tkinter as Tk

def AireTRResult(main, userInput, resultat):
    clean(main)
    if userInput.get() == resultat:
        Label(main, text="Bravo!").pack()
    else:
        Label(main, text="Perdu...").pack()
    Button(main, text="Encore !", command=lambda: AireTRStart(main)).pack()


def AireTRStart(main):
    clean(main)
    Button(main, text="NOUVEAU", command=lambda: AireTRStart(main)).pack()

    L= random.randint(0, 20)
    l= random.randint(1, 10)

    result = int(round((L*l)/ 2, 0))
    string = "Soit le triangle ABC rectangle en A, le côté AB vaut"+str(l)+"cm et le côté AC vaut"+str(L)+ " cm." 
    Label(main, text=string).pack()
    Label(main, text="Quelle est l'aire de ce triangle rectangle?").pack()

    userInput = IntVar()

    Entry(main, textvariable=userInput).pack()
    Button(main, text="Valider", command=lambda: AireTRResult(main, userInput, result)).pack()


