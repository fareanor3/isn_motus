from tkinter import *
from tkinter import font
from random import randrange
import random
import os


def clic_Aléatoire ():
    ouv_fen(True,0) # aléatoire = true , nombre de lettre sans importance: exemple 15312.

def clic_5():
    ouv_fen(False,5)

def clic_6():
    ouv_fen(False,6)

def clic_7():
    ouv_fen(False,7)

def clic_8():
    ouv_fen(False,8)

def clic_9():
    ouv_fen(False,9)


fen1=Tk()

def ouv_fen(Aléatoire,NbreL): # fait passer les informations entre deux programes
    fen1.destroy()
    import Projet_final
    Projet_final.initialiser (Aléatoire,NbreL)

Can=Canvas(fen1,width=225, height=500, bg='white')
ImMotus = PhotoImage (file="2.png")
item=Can.create_image(112,250,image=ImMotus)
Can.place(x=200,y=150)
Motus=Label(fen1, text="MOTUS", font=font.Font(family="Consolas",size=100))
Motus.place(x=0,y=0, width=450, height=150)
Cinq=Button(fen1, text="Mots de 5 lettres",command=clic_5)
Cinq.place(x=0,y=150, width=200, height=75)
Six=Button(fen1, text="Mots de 6 lettres",command=clic_6)
Six.place(x=0,y=225,width=200, height=75)
Sept=Button(fen1, text="Mots de 7 lettres",command=clic_7)
Sept.place(x=0,y=300,width=200, height=75)
Huit=Button(fen1, text="Mots de 8 lettres",command=clic_8)
Huit.place(x=0,y=375,width=200, height=75)
Neuf=Button(fen1, text="Mots de 9 lettres",command=clic_9)
Neuf.place(x=0,y=450,width=200, height=75)
BoutonAléatoire=Button(fen1, text="Nombre de lettres aléatoires",command=clic_Aléatoire)
BoutonAléatoire.place(x=0,y=525,width=200, height=75)
Quit=Button(fen1, text="Quitter",command=fen1.quit)
Quit.place(x=0,y=600,width=200, height=50)

fen1.geometry("425x650")
fen1.mainloop()