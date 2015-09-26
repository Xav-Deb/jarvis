# coding: utf8
# script lecture_gif.py
from Tkinter import *
import tkMessageBox
import tkFileDialog
import gmail, weather
from ScrolledText import *

def Fermer():
    Canevas.delete(ALL)
    Mafenetre.title("Jarvis")

def Apropos():
    tkMessageBox.showinfo("A propos","Jarvis system\n(C) Xavier DEBONTE")

Titre = 'J.A.R.V.I.S.\nJust A Rather Very Intelligent System\nVersion 0.1'
Largeur = 900
Hauteur = 700

Mafenetre = Tk()
Mafenetre.title("Jarvis")

Intro = Label(Mafenetre, text=Titre, font="Arial 10 italic underline", fg='green', bg='black', justify=CENTER, borderwidth=0)
Intro.place(x=450, y=30, anchor=CENTER)

background_image = PhotoImage(file="Jarvis.png")
background_label = Label(Mafenetre, image=background_image)
background_label.config(borderwidth=0)
background_label.place(x=0, y=0)

Output = ScrolledText(Mafenetre, width=120, height=30, background="black", foreground="green", borderwidth=0, wrap='word') 
Output.place(x=0, y=200)

def GMail():
	Output.insert(END,gmail.main())

def Meteo():
	Output.insert(END,weather.main())

Bouton=Label(Mafenetre)
Bouton.place(x=800, y=0)
GmailB = Button(Bouton, text="Gmail", command=GMail)
GmailB.pack()
MeteoB = Button(Bouton, text="Météo", command=Meteo)
MeteoB.pack()

menubar = Menu(Mafenetre)
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)

Mafenetre.config(menu=menubar, background="black", width=Largeur, height=Hauteur, borderwidth=0)

Mafenetre.mainloop()