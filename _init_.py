#Ceci est le fichier d'initialisation du projet
from tkinter import *
import random, winsound, sys
import webbrowser
from PIL import Image, ImageTk


root=Tk()
dessin=Canvas(height=400,width=400)
bomb = Image.open("./minesweeper_cs/KC-Heart_Black.png")
bomb=bomb.resize((100,100))
bomb.save('./KC-Heart_Black_resized.png')
a=PhotoImage(file=r'./KC-Heart_Black_resized.png')
dessin.create_image(200,200,image=a)
dessin.pack()

root.mainloop()