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
    root = Toplevel(app)
    root.title("Minesweeper CS")
    # root.iconbitmap('./images/minesweeper.ico')
    root.resizable(width=False, height=False)

    # Paramètres par défaut correspondant au niveau débutant
    NB_COLS = 10
    NB_LINES = 10
    PC_MINES = 15

    # FONCTION 1 : Cette fonction renvoie pour chaque thème une liste contenant
    # des informations sur les dimensions du canvas,
    # et une liste des images à utiliser pour chaque thème


    def theme(numero_theme):
        listimages = []
        chiffres1 = []
        if numero_theme == 0:  # Celui-ci est le thème classique
            pict_size = 16  # Taille de l'image en pixel
            pad = 1  # Distance en pixel entre deux cases
            side = pict_size+pad
            width = side*NB_COLS
            height = side*NB_LINES
            abscisse = ordonnee = side//2+2
            # Coordonnées du centre de la première case
            numero_theme = [abscisse, ordonnee, side, width, height]
            listimages.append(numero_theme)
            # 1ère sous liste contenue dans la liste listimages,
            # elle donne des informations sur le canvas
            cover = PhotoImage(file="./images/pack_demineur_classique/inconnu.gif")
            # image de la face cachée de la case
            bomb = PhotoImage(file="./images/pack_demineur_classique/mine.gif")
            # image des bombes non perdantes
            bombp = PhotoImage(
                file="./images/pack_demineur_classique/mine_perdu.gif")
            # image de la bombe qui fait perdre la parte
            interr = PhotoImage(file="./images/pack_demineur_classique/interr.gif")
            # image du point d'interrogation
            flag = PhotoImage(file="./images/pack_demineur_classique/flag.gif")
            # image du drapeau
            mauv_flag = PhotoImage(file="./images/pack_demineur_classique/notmine.gif")
            #image mauvais placement drapeau
            listimages.append([cover, bomb, bombp, interr, flag, mauv_flag])
            # 2ème sous liste de la liste listimages,
            # elle contient toutes les images des cases en dehors des cases contenant un chiffre
            for i in range(9):
                chiffres = "./images/pack_demineur_classique/mine" + str(i)+".gif"
                # image contenant le nombre de voisin de la case
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
                # 3ème sou sliste de la liste listimages, elle contient les images des cases chiffrées
            listimages.append(chiffres1)
        if numero_theme == 1:
            # Il s'agit d'un premier thème bleuté
            pict_size = 26
            pad = 1
            side = pict_size+pad
            width = side*NB_COLS
            height = side*NB_LINES
            abscisse = ordonnee = side//2+2
            numero_theme = [abscisse, ordonnee, side, width, height]
            listimages.append(numero_theme)
            cover = PhotoImage(file="./images/themejoli/inconnu.gif")
            bomb = PhotoImage(file="./images/themejoli/mine.gif")
            bombp = PhotoImage(file="./images/themejoli/mine_perdu.gif")
            interr = PhotoImage(file="./images/themejoli/interr.gif")
            flag = PhotoImage(file="./images/themejoli/flag.gif")
            mauv_flag = PhotoImage(file="./images/themejoli/notmine.gif")
            listimages.append([cover, bomb, bombp, interr, flag, mauv_flag])
            for i in range(9):
                chiffres = "./images/themejoli/mine" + str(i)+".gif"
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
            listimages.append(chiffres1)
        if numero_theme == 2:
            # il s'agit d'un deuxième thème bleuté
            pict_size = 24
            pad = 0
            side = pict_size+pad
            width = side*NB_COLS
            height = side*NB_LINES
            abscisse = ordonnee = side//2+2
            numero_theme = [abscisse, ordonnee, side, width, height]
            listimages.append(numero_theme)
            cover = PhotoImage(file="./images/Gnome/inconnu.gif")
            bomb = PhotoImage(file="./images/Gnome/mine.gif")
            bombp = PhotoImage(file="./images/Gnome/mine_perdu.gif")
            interr = PhotoImage(file="./images/Gnome/interr.gif")
            flag = PhotoImage(file="./images/Gnome/flag.gif")
            mauv_flag = PhotoImage(file="./images/Gnome/notmine.gif")
            listimages.append([cover, bomb, bombp, interr, flag, mauv_flag])
            for i in range(9):
                chiffres = "./images/Gnome/mine" + str(i)+".gif"
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
            listimages.append(chiffres1)
        if numero_theme == 3:
            # il s'agit d'un thème avec des cases noires
            pict_size = 16
            pad = 1
            side = pict_size+pad
            width = side*NB_COLS
            height = side*NB_LINES
            abscisse = ordonnee = side//2+2
            numero_theme = [abscisse, ordonnee, side, width, height]
            listimages.append(numero_theme)
            cover = PhotoImage(file="./images/Black/inconnu.gif")
            bomb = PhotoImage(file="./images/Black/mine.gif")
            bombp = PhotoImage(file="./images/Black/mine_perdu.gif")
            interr = PhotoImage(file="./images/Black/interr.gif")
            flag = PhotoImage(file="./images/Black/flag.gif")
            mauv_flag = PhotoImage(file="./images/Black/notmine.gif")
            listimages.append([cover, bomb, bombp, interr, flag, mauv_flag])
            for i in range(9):
                chiffres = "./images/Black/mine" + str(i)+".gif"
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
            listimages.append(chiffres1)
        if numero_theme == 4:
            # il s'agit d'un thème Saint Valentin avec des cases roses
            pict_size = 16
            pad = 1
            side = pict_size+pad
            width = side*NB_COLS
            height = side*NB_LINES
            abscisse = ordonnee = side//2+2
            numero_theme = [abscisse, ordonnee, side, width, height]
            listimages.append(numero_theme)
            cover = PhotoImage(file="./images/pack_saint_valentin/inconnu.gif")
            bomb = PhotoImage(file="./images/pack_saint_valentin/mine.gif")
            bombp = PhotoImage(file="./images/pack_saint_valentin/mine_perdu.gif")
            interr = PhotoImage(file="./images/pack_saint_valentin/interr.gif")
            flag = PhotoImage(file="./images/pack_saint_valentin/flag.gif")
            mauv_flag = PhotoImage(file="./images/pack_saint_valentin/notmine.gif")
            listimages.append([cover, bomb, bombp, interr, flag, mauv_flag])
            for i in range(9):
                chiffres = "./images/pack_saint_valentin/mine" + str(i)+".gif"
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
            listimages.append(chiffres1)
        if numero_theme == 5:
            # il s'agit d'un thème Noël avec des cases vertes
            pict_size = 16
            pad = 1
            side = pict_size+pad
            width = side*NB_COLS
            height = side*NB_LINES
            abscisse = ordonnee = side//2+2
            numero_theme = [abscisse, ordonnee, side, width, height]
            listimages.append(numero_theme)
            cover = PhotoImage(file="./images/pack_noel/inconnu.gif")
            bomb = PhotoImage(file="./images/pack_noel/mine.gif")
            bombp = PhotoImage(file="./images/pack_noel/mine_perdu.gif")
            interr = PhotoImage(file="./images/pack_noel/interr.gif")
            flag = PhotoImage(file="./images/pack_noel/flag.gif")
            mauv_flag = PhotoImage(file="./images/pack_noel/notmine.gif")
            listimages.append([cover, bomb, bombp, interr, flag, mauv_flag])
            for i in range(9):
                chiffres = "./images/pack_noel/mine" + str(i)+".gif"
                chiffre = PhotoImage(file=chiffres)
                chiffres1.append(chiffre)
            listimages.append(chiffres1)
        return listimages
    themec = [0]
    # thème par défaut correspondant au thème classique
    THEME = theme(themec[0])
    # FONCTION 2 : Cette fonction permet de sélectionner le thème à partir de la combobox
    def select_theme(event):
        global themec, THEME
        if themesc.get() == 'Thème classique':
            themec[0] = 0
            THEME = theme(themec[0])
        if themesc.get() == 'Thème Saint Valentin':
            themec[0] = 4
            THEME = theme(themec[0])
        if themesc.get() == 'Thème noir':
            themec[0] = 3
            THEME = theme(themec[0])
        if themesc.get() == 'Thème bleu clair':
            themec[0] = 1
            THEME = theme(themec[0])
        if themesc.get() == 'Thème bleu foncé':
            themec[0] = 2
            THEME = theme(themec[0])
        if themesc.get() == 'Thème Noël':
            themec[0] = 5
            THEME = theme(themec[0])
    cnv = Canvas(root, width=THEME[0][3]+1, height=THEME[0][4]+1)
    # on crée un premier canvas avec des dimensions associées à la grille du thème classique
    cnv.pack(side=RIGHT)

    # FONCTION 3: Cette fonction permet de récupérer le difficulté souhaitée par le joueur


    def init_difficulte():
        global NB_LINES, NB_COLS, PC_MINES
        value = diff.get()
        if value == 1:
            # cela correspond au niveau débutant
            NB_COLS, NB_LINES, PC_MINES = 10, 10, 10
        elif value == 2:
            # cela correspond au niveau avancé
            NB_COLS, NB_LINES, PC_MINES = 20, 20, 20
        elif value == 3:
            # cela correpsond au niveau expérimenté
            NB_COLS, NB_LINES, PC_MINES = 25, 25, 30

    # FONCTION 4 : Cette fonction permet d'initialiser la grille de jeu
    # en affichant les cases recouvertes
    # ie on ne voit pas si c'est une bombe ou une case ne contenant pas de bombe


    def init_jeu(grid):
        table = grid
        global NB_LINES, NB_COLS
        for line in range(NB_LINES):
            for col in range(NB_COLS):
                centre = (THEME[0][0]+col*THEME[0][2],
                      THEME[0][1]+line*THEME[0][2])
                cnv.create_image(centre, image=THEME[1][0])


    # FONCTION 5 : Cette fonction permet d'exécuter le jeu


    def run():
        #global themec
        global state
        global start_time
        state = 1
        start_time = time()
        update_chrono()
        THEME = theme(themec[0])
        # On rappelle que cette liste contient trois listes,
        # une première contennat des informations sur les cases
        # et sur la grilles en termes de dimension et de positionnement,
        # il y a deux autres sous listes contenant des images pour les cases
        cnv.configure(width=THEME[0][3]+1)
        cnv.configure(height=THEME[0][4]+1)
        grid = create_grid(NB_COLS, NB_COLS, PC_MINES)
        init_jeu(grid)
        remaining_flag = nb_drapeau_restant(grid)
        decompte_mines.configure(text=str(remaining_flag))
        cnv.bind("<Button-1>", partial(clicg, grid))
        cnv.bind("<Button-3>", partial(clicd, grid))

    # FONCTION 6 : Cette fonction permet d'effectuer des changements
    # lorsque l'on effectue un clique gauche


    def clicg(grid, event):
        print (state)
        if is_it_game_over(grid) is False and is_it_over(grid) is False:
            # si le jeu n'est pas perdu et si le jeu n'est pas gagné
            abscisse, ordonnee = (event.x, event.y)
            # on récupère les coordonnées du point de la grille sur lequel on a cliqué avec la souris
            col = abscisse//THEME[0][2]
            # on récupère la colonne associée au point sur lequel on a cliqué
            lig = ordonnee//THEME[0][2]
            # on récupère la ligne associée au point sur lequel on a cliqué
            centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+lig*THEME[0][2])
            grid[lig][col][1] = True
            # on précise que l'on a découvert la case
            affichage(lig, col, centre, grid)
            game_over(lig, col, centre, grid)
            # over(grid)
        remaining_flag = nb_drapeau_restant(grid)
        decompte_mines.configure(text=str(remaining_flag))

    # FONCTION 7 : Cette fonction permet d'effectuer des changements
    # lorsque l'on effectue un clique droit


    def clicd(grid, event):
        remaining_flag = nb_drapeau_restant(grid)
        if is_it_game_over(grid) is False and is_it_over(grid) is False and remaining_flag != 0:
            abscisse, ordonnee = (event.x, event.y)
            col = abscisse//THEME[0][2]
            lig = ordonnee//THEME[0][2]
            centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+lig*THEME[0][2])
            grid[lig][col][2] = (grid[lig][col][2]+1) % 3
            affichage(lig, col, centre, grid)
        elif is_it_game_over(grid) is False and is_it_over(grid) is False and remaining_flag == 0:
            abscisse, ordonnee = (event.x, event.y)
            col = abscisse//THEME[0][2]
            lig = ordonnee//THEME[0][2]
            centre = (THEME[0][0]+col*THEME[0][2], THEME[0][1]+lig*THEME[0][2])
            grid[lig][col][2] = 0
            affichage(lig, col, centre, grid)
        remaining_flag = nb_drapeau_restant(grid)
        decompte_mines.configure(text=str(remaining_flag))
    # FONCTION 8 : Cette fonction permet d'afficher le contenu d'une case
    # ou bien de placer un drapeau ou un point d'interrogation


    def affichage(lig, col, centre, grid):
        if grid[lig][col][1] is True:
            # on vient de cliquer sur la case, elle est donc passée au statut de "visitée"
            if grid[lig][col][0] is True:
                # on vérifie que la case est une bombe
                cnv.create_image(centre, image=THEME[1][2])
                # on place une image de bombe sur la case
            else:
                if connexe_test(grid, (col+1, lig+1)):
                    # si la case n'est pas une bombe, on regarde
                    # si par hasard elle appartient à un connexe
                    liste = connexe_appartient(grid, (col+1, lig+1))
                    # liste des cases à afficher autour de cette case
                    for i in liste:
                        compteur = nb_bombe_voisin(grid, i)
                        variable1, variable2 = i
                        if not grid[variable2-1][variable1-1][1]:
                            grid[variable2-1][variable1-1][1] = True
                            centrei = (THEME[0][0]+(variable1-1)*THEME[0]
                                   [2], THEME[0][1]+(variable2-1)*THEME[0][2])
                            cnv.create_image(centrei, image=THEME[2][compteur])
                compteur = nb_bombe_voisin(grid, (col+1, lig+1))
                cnv.create_image(centre, image=THEME[2][compteur])
        elif grid[lig][col][2] == 0:
            # si on a appuyé un nombre multiple de trois fois sur la case,
            # alors on retourne sur l'image cover qui par définition cache la case
            cnv.create_image(centre, image=THEME[1][0])
        elif grid[lig][col][2] == 1:
            # si on a appuyé une fois modulo trois sur la case
            # alors cela signifie que l'on pose un drapeau sur la case
            cnv.create_image(centre, image=THEME[1][4])
        elif grid[lig][col][2] == 2:
            # si on a appuyé deux fois modulo trois sur la case alors
            # cela signifie que l'on pose un point d'interrogation sur la case
            cnv.create_image(centre, image=THEME[1][3])

    # FONCTION 9 : Cette fonction permet d'afficher toutes les bombes lorsque la partie est perdue


    def affichage_tout(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j][0]:
                    centre = (THEME[0][0]+(j)*THEME[0][2],
                          THEME[0][1]+(i)*THEME[0][2])
                    # Bombe dans la case correspondant à i+1,j=1
                    cnv.create_image(centre, image=THEME[1][1])
                if not(grid[i][j][0]) and grid[i][j][2]==1 and not(grid[i][j][1]):
                    centre = (THEME[0][0]+(j)*THEME[0][2],
                          THEME[0][1]+(i)*THEME[0][2])
                    # Bombe dans la case correspondant à i+1,j=1
                    cnv.create_image(centre, image=THEME[1][5])

    # FONCTION 10 : Cette fonction permet de vérifier si la partie est gagnée
    def over(grid):
        global state
        centre2 = (THEME[0][3]/2, THEME[0][4]/2)
        if is_it_over(grid):
            state = 0
            cnv.create_text(centre2,
            text='You Win',
            font=('System', int(THEME[0][3]/14)),
            fill='green')
            #si la partie est gagnée, on signale au joueur qu'il a gagné

    # FONCTION 11 : Cette fonction permet de vérifier si la partie est perdue


    def game_over(lig, col, centre, grid):
        global state
        #ligne = lig
        #colonne = col
        #centre2 = (THEME[0][3]/2, THEME[0][3]/2)
        if is_it_game_over(grid):
            state = 0
            dsong = pygame.mixer.Sound('./songs/explosion.wav')
            # On joue un son d'explosion
            dsong.play()
            affichage_tout(grid)
            # on affiche toutes les bombes
            cnv.create_image(centre, image=THEME[1][2])
            # on affiche l'image de la bomobe qui a fait perdre la partie,
            # celle-ci a une couleur d'arrière-plan rouge qui la distingue ainsi des autres
            centre2 = (THEME[0][3]/2, THEME[0][4]/2)
            #cnv.create_text(centre2, text='GameOver', font=('System', int(THEME[0][3]/8)), fill='red')


    ####    Paramètres d'AFFICHAGE de la fenêtre    #####
    # On crée un frame qui contiendra tous nos botuons
    f1 = Frame(root)

    # Combobox qui nous permettra de choisir le thème
    themesc = ttk.Combobox(f1, values=['Thème classique', 'Thème Saint Valentin',
                       'Thème bleu clair',  'Thème noir', 'Thème bleu foncé', 'Thème Noël'])
    # on crée une liste déroulante permettant de choisir le thème
    themesc_label = Label(f1, text="Veuillez préciser le thème :")
    themesc_label.pack()
    themesc.pack()
    themesc.bind('<<ComboboxSelected>>', select_theme)

    bou1 = Button(f1, width=14, text="Nouvelle partie",
              font="Arial 10", bg='#3AC2F7', fg='white', command=run)
    bou1.pack(side=BOTTOM, padx=5, pady=5)

    # Liste des Radiobuttons qui permettront de choisir la difficulté
    diff_label = Label(f1, text="Veuillez préciser la difficulté :")
    diff_label.pack()
    diff = IntVar()
    diff.set(1)
    case1 = Radiobutton(f1)
    case1.configure(text='Débutant', command=init_difficulte,
                variable=diff, value=1)
    case1.pack(anchor=W, padx=30)
    case2 = Radiobutton(f1)
    case2.configure(text='Intermédiaire', padx=3,
                command=init_difficulte, variable=diff, value=2)
    case2.pack(anchor=W, padx=30)
    case3 = Radiobutton(f1)
    case3.configure(text='Experimenté', padx=3,
                command=init_difficulte, variable=diff, value=3)
    case3.pack(anchor=W, padx=30)

    # Ajout d'une musique dans le jeu
    pygame.mixer.init()

    # Fonction permmetant de lancer la musique


    def play():
        pygame.mixer.music.load("./songs/song.wav")
        pygame.mixer.music.play(loops=-1)
        # on précise que l'on joue la musique en boucle

    # Fonction permettant d'arrêter la musique


    def stop():
        pygame.mixer.music.stop()


    # Boutons permettant de lancer/arrêter la musique
    my_button = Button(f1, text="Play Song", bg='#20bebe',
                   fg="white", command=play)
    my_button.pack(pady=1)
    stop_button = Button(f1, text="Stop Song", bg="#9F3333",
                     fg='white', command=stop)
    stop_button.pack(pady=1)

    # Fonction permettant d'ouvrir le repo distant sur gitlab


    def openj():
        webbrowser.open_new(
            "https://gitlab-ovh-01.cloud.centralesupelec.fr/jordan.boutoux/minesweeper_cs")


    # Création d'une barre de menu
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Ouvrir le repo GitLab", command=openj)
    # Une première tâche pouvant être réalisée est l'ouverture du dépôt GitLab du projet
    file_menu.add_command(label="Quitter", command=root.quit)
    # Une seconde tâche pouvant être réalisée est la fermeture de la page
    menu_bar.add_cascade(label="Options", menu=file_menu, command=openj)
    f1.pack(side=BOTTOM)
    root.config(menu=menu_bar)

    texte_mines = Label(f1, text="Mines restantes :")
    decompte_mines = Label(f1, text="Veuillez lancer le jeu")
    texte_mines.pack()
    decompte_mines.pack()

    case_chrono = Label(root, text="Time:")
    chrono_str = StringVar()
    chrono_str.set("00:00")
    chrono = Label(root, textvariable=chrono_str)
    case_chrono.pack()
    chrono.pack()


    def update_chrono():
        if state == 1:
            now = int(time() - start_time)
            min = str(now // 60)
            sec = str(now % 60)
            if len(min) < 2:
                min = "0" + min
            if len(sec) < 2:
                sec = "0" + sec
            chrono_str.set(min+":"+sec)
            root.after(1000, update_chrono)


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