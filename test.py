import tkinter as tk
from tkinter import font
from tkinter.constants import RAISED
from tkinter import *
from PIL import ImageTk, Image
import os


OptionList = [
"Facile",
"Normal",
"Difficile"
] 

OptionListb = [
"Classique",
"Noël",
"Halloween"
] 


app = tk.Tk()
app.geometry('400x400')
app.title("Paramètres")
app.config(background="grey")

frame = tk.Frame()
frameb= tk.Frame()

variable = tk.StringVar(frame)
variable.set("Difficulté")
variableb = tk.StringVar(frameb)
variableb.set("Thématique")

frame.pack()
frameb.pack()
opt = tk.OptionMenu(frame, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 18), background= "grey", fg="white", relief = RAISED)
opt.pack(side="top")

labelTest = tk.Label(text="", font=('Helvetica', 18), fg='red')
#labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="Le niveau de difficulté sélectionné est {}".format(variable.get()), bg="grey", fg="white")

optb = tk.OptionMenu(frameb, variableb, *OptionListb)
optb.config(width=90, font=('Helvetica', 18), background= "grey", fg="white", relief = RAISED)
optb.pack(side="top")

labelTestb = tk.Label(text="", font=('Helvetica', 18))
#labelTestb.pack(side="top")

def callbackb(*args):
    labelTest.configure(text="La thématique sélectionnée est {}".format(variableb.get()), bg="grey", fg="white")




variable.trace("w", callback)
variableb.trace("w", callbackb)

def debut():
    newWindow = tk.Toplevel(app)


bouton_play = tk.Button (app, text = "Commencer à jouer", font=("Helvetica",25),background="grey", fg='grey', command=debut())
bouton_play.pack(pady=25)


#[imageSizeWidth, imageSizeHeight] = imageb.size
#newImageSizeWidth = int(imageSizeWidth*n)
#newImageSizeHeight = int(imageSizeHeight*n)

Canvas1 = Canvas(app)
imageb = Image.open("C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/MINESWEEPER.png")
print(imageb.size)

img = ImageTk.PhotoImage(imageb)

Canvas1.create_image(0,0,image = img)      
#newImageSizeWidth/2,newImageSizeHeight/2,
Canvas1.config(bg = "grey")
#,width = newImageSizeWidth, height = newImageSizeHeight
Canvas1.pack(side=LEFT,expand=True,fill=BOTH)



 




app.mainloop()