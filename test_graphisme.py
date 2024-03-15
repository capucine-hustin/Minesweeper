from tkinter import *
from test_minesweeper import *
import webbrowser
import pygame
from functools import partial
from PIL import Image, ImageTk

NB_COLS = 10
NB_LINES = 10
PC_MINES = 15

OptionListb = [
"Classique",
"Noël",
"Halloween"
] 

def createNewWindow():
    def theme(a):
        listimages=[]
        chiffres1 = []
        if a==0: #Celui-ci est le thème classique
            PICT_SIZE = 16
            PAD = 1
            SIDE = PICT_SIZE+PAD
            WIDTH = SIDE*NB_COLS
            HEIGHT = SIDE*NB_LINES
            X0 = Y0 = SIDE//2+2
            a=[X0, Y0, SIDE,WIDTH,HEIGHT]
            listimages.append(a)
            cover = PhotoImage(file="C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/pack noel/inconnu.gif")
            bomb = PhotoImage(file="C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/pack noel/mine_perdu.gif")
            bombp = PhotoImage(file="C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/pack noel/bombe.gif")
            interr = PhotoImage(file="C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/pack noel/interr.gif")
            flag = PhotoImage(file="C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/pack noel/flag.gif")
            listimages.append([cover,bomb,bombp,interr,flag])
            for i in range(9):
                chiffres = "C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/pack noel/mine" + str(i)+".gif"
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
            listimages.append(chiffres1)
        return listimages
    THEME=theme(0)
    newWindow = Toplevel(app)
    f1 = Frame(newWindow)
    newWindow.title("Minesweeper CS")
    cnv = Canvas(newWindow, width=THEME[0][3]+1, height=THEME[0][4]+1)
    cnv.pack(side=RIGHT)
    def init_difficulte():
        global nb_col, nb_lig, nb_mines 
        niveau = choix.get()
        if niveau == 1:
            nb_col, nb_lig, nb_mines = 10, 10, 12 
        elif niveau == 2:
            nb_col, nb_lig, nb_mines = 15, 15, 30
        else:
            nb_col, nb_lig, nb_mines = 20, 20, 50
    def init_jeu(grid):
        global NB_LINES, NB_COLS
        m = []
        for line in range(NB_LINES):
            for col in range(NB_COLS):
                if grid[line][col][0] == True:
                    centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+line*THEME[0][2])
                    mind = cnv.create_image(centre, image=THEME[1][1])
                    m.append(mind)
                else:
                    c = nb_bombe_voisin(grid, (col+1, line+1))
                    centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+line*THEME[0][2])
                    mind = cnv.create_image(centre, image=THEME[2][c])
                    m.append(mind)
        ids_inc = []
        for line in range(NB_LINES):
            L = []
            for col in range(NB_COLS):
                centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+line*THEME[0][2])
                id_inc = cnv.create_image(centre, image=THEME[1][0])
                L.append(id_inc)
            ids_inc.append(L)
    def run():
        grid = create_grid(20,20,10)
        init_jeu(grid)
        print(is_it_game_over(grid))
        cnv.bind("<Button-1>", partial(clicg, grid))
        cnv.bind("<Button-3>", partial(clicd,grid))
    f1 = Frame(newWindow)
    bou1 = Button(f1, width=14, text="Nouvelle partie", font="Arial 10", bg='#3AC2F7', fg='white', command=run)
    bou1.pack(side=BOTTOM, padx=5, pady=5)
    f1.pack(side=BOTTOM)
    f2 = Frame(newWindow)
    choix=IntVar()
    choix.set(1)
    case1=Radiobutton(f2)
    case1.configure(text='Débutant', command=init_difficulte, variable=choix,value=1)
    case1.pack(anchor= NW ,padx=30)
    case2=Radiobutton(f2)
    case2.configure(text='Avancé', padx=3, command=init_difficulte, variable=choix,value=2)
    case2.pack(anchor= NW, padx=30)
    case3=Radiobutton(f2)
    case3.configure(text='Expert', padx=3, command=init_difficulte, variable=choix,value=3)
    case3.pack(anchor= NW ,padx=30)
    f2.pack()
    def clicg(grid, event):
        if is_it_game_over(grid)==False:
            X, Y = (event.x, event.y)
            col = X//THEME[0][2]
            lig = Y//THEME[0][2]
            centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+lig*THEME[0][2])
        # id_inc=ids_inc[lig][col]
            grid[lig][col][1] = True
        # cnv.delete(id_inc)
            affichage(lig, col, centre,grid)
            game_over(lig, col, centre, grid)
    def clicd(grid, event):
        if is_it_game_over(grid)==False:
            X, Y = (event.x, event.y)
            col = X//THEME[0][2]
            lig = Y//THEME[0][2]
            centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+lig*THEME[0][2])
            grid[lig][col][2] = (grid[lig][col][2]+1) % 3
            affichage(lig, col, centre,grid)
    def affichage(lig, col, centre,grid):
        if grid[lig][col][1] == True:
            if grid[lig][col][0] == True:
                cnv.create_image(centre, image=THEME[1][2])
            else:
                if connexe_test(grid, (col+1, lig+1)):
                    l = connexe_appartient(grid, (col+1, lig+1))
                    for i in l:
                        c = nb_bombe_voisin(grid, i)
                        a, b = i
                        if not(grid[b-1][a-1][1]):
                            grid[b-1][a-1][1] = True
                            centrei = (THEME[0][0]+(a-1)*THEME[0][2], THEME[0][1]+(b-1)*THEME[0][2])
                            cnv.create_image(centrei, image=THEME[2][c])
                c = nb_bombe_voisin(grid, (col+1, lig+1))
                #print(col+1, lig+1)
                cnv.create_image(centre, image=THEME[2][c])
        elif grid[lig][col][2] == 0:
            cnv.create_image(centre, image=THEME[1][0])
        elif grid[lig][col][2] == 1:
            cnv.create_image(centre, image=THEME[1][4])
        elif grid[lig][col][2] == 2:
            cnv.create_image(centre, image=THEME[1][3])
    def affichage_tout(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j][0]:
                    centre = (THEME[0][0]+(j)*THEME[0][2], THEME[0][1]+(i)*THEME[0][2])
                    # Bombe dans la case correspondant à i+1,j=1
                    cnv.create_image(centre, image=THEME[1][1])
    def over(grid):
        centre2 = (THEME[0][3]/2, THEME[0][4]/2)
        if is_it_over(grid):
            cnv.create_text(centre2, text='GameOver', font=(
                'Helvetica', int(THEME[0][3]/7)), fill='red')
    def game_over(lig, col, centre, grid):
        centre2 = (THEME[0][3]/2, THEME[0][3]/2)
        if is_it_game_over(grid):
            dsong=pygame.mixer.Sound('C:/Users/jorda/OneDrive/Bureau/Coding_Weeks/2048_game_codkings/explosion.wav')
            dsong.play()
            affichage_tout(grid)
            cnv.create_image(centre, image=THEME[1][2])  # bombe defaite
    f4 = Frame(newWindow)
    f4.pack(side=BOTTOM)
    pygame.mixer.init()
    def play():
        pygame.mixer.music.load("C:/Users/jorda/OneDrive/Bureau/test_demineur/vexento.wav")
        pygame.mixer.music.play(loops=-1)
    def stop():
        pygame.mixer.music.stop()
    my_button = Button(f4, text="Play Song", font="Ebrima",
                   bg='#20bebe', fg="white", height=2, width=10, command=play)
    my_button.pack(pady=20)
    stop_button = Button(f4, text="Stop Song", command=stop)
    stop_button.pack(pady=20)
    def openj():
        webbrowser.open_new(
            "https://gitlab-ovh-01.cloud.centralesupelec.fr/jordan.boutoux/minesweeper_cs")
    yt_button = Button(f4, text="Open repository GitLab", command=openj)
    yt_button.pack()
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Ouvrir le repo GitLab", command=openj)
    file_menu.add_command(label="Quitter", command=root.quit)
    menu_bar.add_cascade(label="Options", menu=file_menu, command=openj)






app = Tk()
app.geometry('400x400')
app.title("Paramètres")
app.config(background="grey")
buttonExample = Button(app, 
              text="Appuyer ici pour jouer !", font=('Helvetica', 18),background= "grey", fg="white", relief = RAISED,width=90,
              command=createNewWindow)
buttonExample.pack()

frameb= Frame()
variableb = StringVar(frameb)
variableb.set("Thématique")




accueil=Canvas(app, width=400, height=400)
accueil.pack(side=BOTTOM)
accueil.create_text((200,20), fill='black', text="Bienvenue sur minesweeper cs !", font=('Helvetica','18','bold'))


bomb = Image.open("C:/Users/capuc/Documents/sip_td_computer/minesweeper_cs/minesweeper_cs/MINESWEEPER.png")
bomb=bomb.resize((200,200))
bomb.save('./logo_resized.png')
a=PhotoImage(file=r'./KC-Heart_Black_resized.png')
accueil.create_image(200,180,image=a)
accueil.pack()



app.mainloop()
