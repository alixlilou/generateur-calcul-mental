from tkinter import*
import tkinter as Tk

from utilitaire import *
from CollegeDivision import CollegeDivisionStart
from LyceePolynomes import LyceePolynomesStart
from LyceeComplexes import LyceeComplexeStart
from CollegeFonction import CollegeFonctionStart
from PrimaireAddition import PrimaireAdditionStart
from PrimaireAireRectangle  import AireRectangleStart
from PrimaireAireTQ import AireTQStart
from PrimaireAireTR import AireTRStart
from PrimaireDivision import PrimaireDivisionStart
from PrimaireMultiplication import PrimaireMultiplicationStart
from PrimaireSoustraction import PrimaireSoustractionStart
from CollegeDivisionP import CollegeDivisionPStart
from CollegeMP import CollegeMPStart
from CollegePyth import CollegePythStart
from LyceeDer import LyceeDerStart
from LyceeFonction import LyceeFonctionStart

def ouvrirExercise(main, exercise):
    fenetre = Tk.Toplevel(main) #Créer une nouvelle fenetre
    fenetre.wm_geometry("500x500")
    exercise(fenetre)

def createPrimaire(main):
    clean(main)
    Button(main, text="Retour", command=lambda: createStartWindow(main)).pack()
    Button(main, text="Addition", command=lambda: ouvrirExercise(main, PrimaireAdditionStart)).pack()
    Button(main, text="Aire d'un rectangle", command=lambda: ouvrirExercise(main, AireRectangleStart)).pack()
    Button(main, text="Aire d'un triangle quelconque", command=lambda: ouvrirExercise(main, AireTQStart)).pack()
    Button(main, text="Aire d'un triangle rectangle", command=lambda: ouvrirExercise(main, AireTRStart)).pack()
    Button(main, text="Division", command=lambda: ouvrirExercise(main, PrimaireDivisionStart)).pack()
    Button(main, text="Multiplication", command=lambda: ouvrirExercise(main, PrimaireMultiplicationStart)).pack()
    Button(main, text="Soustraction", command=lambda: ouvrirExercise(main, PrimaireSoustractionStart)).pack()

def createCollege(main):
    clean(main)
    Button(main, text="Retour", command=lambda: createStartWindow(main)).pack()
    Button(main, text="Division", command=lambda: ouvrirExercise(main, CollegeDivisionStart)).pack()
    Button(main, text="Fonction", command=lambda: ouvrirExercise(main, CollegeFonctionStart)).pack()
    Button(main, text="Division de puissances", command=lambda: ouvrirExercise(main,CollegeDivisionPStart)).pack()
    Button(main, text="Multiplication de puissances", command=lambda: ouvrirExercise(main,CollegeMPStart)).pack()
    Button(main, text="Multiplication", command=lambda: ouvrirExercise(main,PrimaireMultiplicationStart)).pack()
    Button(main, text="Théorème de Pythagore",command=lambda: ouvrirExercise(main,CollegePythStart)).pack()

def createLycee(main):
    clean(main)
    Button(main, text="Retour", command=lambda: createStartWindow(main)).pack()
    Button(main, text="Polynomes", command=lambda: ouvrirExercise(main, LyceePolynomesStart)).pack()
    Button(main, text="Complexes", command=lambda: ouvrirExercise(main, LyceeComplexeStart)).pack()
    Button(main, text="Dérivées", command=lambda: ouvrirExercise(main, LyceeDerStart)).pack()
    Button(main, text="Fonctions", command=lambda: ouvrirExercise(main, LyceeFonctionStart)).pack()


def createStartWindow(main):
    clean(main)
    Button(main, text="Primaire", command=lambda: createPrimaire(main)).pack()
    Button(main, text="College", command=lambda: createCollege(main)).pack()
    Button(main, text="Lycee", command=lambda: createLycee(main)).pack()

main = Tk.Tk()
main.wm_geometry("500x500")
createStartWindow(main)
main.mainloop()
