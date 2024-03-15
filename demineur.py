from tkinter import *


dic_couleur_texte={1:'pink1',2:'DeepPink2',3:'DeepPink3',4:'DeepPink4',5:'gray11',6:'pink1',7:'DeepPink2',8:'DeepPink3'}

h=400
w=400


root = Tk()
root.title('minesweeper')

dessin=Canvas(root, bg="#a39489",height=h, width=w, highlightbackground="#a39489")
dessin.grid(row=0,column=0,columnspan=2, padx=1, pady=1)

def grille_depart(nb_colonnes,nb_lignes):
    #a est la largeur d'un cube
    a=min(h/nb_lignes,w/nb_colonnes)
    for i in range(nb_colonnes):
        for j in range (nb_lignes):
            dessin.create_polygon((a*i,a*j), (a*i,a+a*j), (a+a*i,a+a*j), (a+a*i,a*j), fill='HotPink2',outline="DeepPink3")



def init_niveau():
    global nb_col, nb_lig, nb_mines 
    niveau = choix.get()
    # niveau debutant
    if niveau == 1:
        nb_col, nb_lig, nb_mines = 10, 10, 12
    # niveau avance 
    elif niveau == 2:
        nb_col, nb_lig, nb_mines = 15, 15, 30
    # niveau expert
    else:
        nb_col, nb_lig, nb_mines = 20, 20, 50
    # taille du canevas pour chaque niveau
    dessin.configure(width=w , height=h)



grille_depart(10,10)

root.mainloop()