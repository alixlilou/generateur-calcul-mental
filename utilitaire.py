from tkinter import*
import tkinter as Tk

def clean(main):
    for but in main.winfo_children():
        but.destroy()