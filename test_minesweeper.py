import random
import numpy

import pytest


test2 = [[[True, False, 0], [True, False, 0], [True, False, 0], [False, False, 0], [True, False, 0], [False, False, 0], [False, False, 0]], [[True, False, 0], [False, False, 0], [False, False, 0], [False, False, 0], [False, False, 0], [False, False, 0], [False, False, 0]], [[True, False, 0], [False, False, 0], [True, False, 0], [
    True, False, 0], [False, False, 0], [False, False, 0], [True, False, 0]], [[True, False, 0], [True, False, 0], [True, False, 0], [True, False, 0], [False, False, 0], [False, False, 0], [False, False, 0]], [[True, False, 0], [True, False, 0], [True, False, 0], [False, False, 0], [False, False, 0], [False, False, 0], [False, False, 0]]]  # (5,7)

test3 = [[[True, False, 0], [False, False, 0], [True, False, 0]], [[False, False, 0], [True, False, 0], [False, False, 0]], [
    [False, False, 0], [False, False, 0], [True, False, 0]], [[False, False, 0], [True, False, 0], [True, False, 0]]]  # (4,3)

test4 = [[[True, False, 0], [True, False, 0], [False, False, 0], [True, False, 0], [False, False, 0]], [[True, False, 0], [False, False, 0], [True, False, 0], [False, False, 0], [False, False, 0]], [[False, False, 0], [True, False, 0], [
    True, False, 0], [False, False, 0], [True, False, 0]], [[False, False, 0], [False, False, 0], [False, False, 0], [True, False, 0], [False, False, 0]], [[True, False, 0], [False, False, 0], [False, False, 0], [False, False, 0], [False, False, 0]]]


def mod(l):
    l2 = [[] for j in range(len(l))]
    for i in range(len(l)):
        c = l[i]
        for k in range(len(c)):
            l2[i].append([c[k][0], False, False])
    return l2
# create_grid Genere une table de jeu de taille l*c

# Chaque case est représentée par un triplet.
# le premier élèment du triplet indique s'il y'a une mine ou non (True il y a une mine , False sinon),
# le second élément indique si l'emplacement a été visité ou non ( False si pas encore de visite, True sinon).
# le troisième élément indique si le joueur a décidé de marquer la case comme "minée" (True s'il le fait, False sinon)
# la table est représentée par une liste de liste.


TorF = [False for i in range(7)]+[True for i in range(3)]
Grid_test = 0
print(TorF)

# une améliotation possible = augmenter la diffultée en jouant sur la fréquence des bombes, voir sur la distribution de celle-ci. Ici c'est 50/50.

# il serait aussi interessant de modifier cette fonction pour qu'elle ne génère pas des "packet" de bombe , pour faciliter le jeu. Ni un seul packet de case sans bombe car ça serait trop facile


def create_grid(l, c, n):
    TorF2 = [True for i in range(n)] + [False for i in range(100-n)]
    game_grid = []
    for i in range(0, l):
        ligne = []
        for j in range(0, c):
            ligne += [[random.choice(TorF2), False, 0]]
        game_grid.append(ligne)
    return game_grid


def test_create_grid():
    tabletest = create_grid(15, 15)
    for i in range(15):
        for j in range(15):
            assert tabletest[i][j][0] in TorF
            assert not(tabletest[i][j][1])
            assert tabletest[i][j][2] == 0

# la fonction suivante prend une table de jeux et un point ( coordonnée (x,y)) et renvoie le nombre de bombe située au tour du point. ce nombre servira d'indice a affiché si le joueur choisit ce point et qu'il n'y a pas de point dessus.


def nb_bombe_voisin(table, point):
    l = len(table)
    n = len(table[0])
    a, b = point
    x, y = b-1, a-1
    c = 0
    if x == l-1:
        # Y a beaucoups de if parcequ'il faut faire attention au cas ou la case est sur les frontieres.
        if y == n-1:
            if table[x-1][y][0]:
                c += 1
            if table[x-1][y-1][0]:
                c += 1
            if table[x][y-1][0]:
                c += 1
        elif y == 0:
            if table[x-1][y][0]:
                c += 1
            if table[x-1][y+1][0]:
                c += 1
            if table[x][y+1][0]:
                c += 1
        else:
            if table[x-1][y][0]:
                c += 1
            if table[x-1][y-1][0]:
                c += 1
            if table[x][y-1][0]:
                c += 1
            if table[x-1][y+1][0]:
                c += 1
            if table[x][y+1][0]:
                c += 1
    elif x == 0:
        # Y a beaucoups de if parcequ'il faut faire attention au cas ou la case est sur les frontieres.
        if y == n-1:
            if table[x+1][y][0]:
                c += 1
            if table[x+1][y-1][0]:
                c += 1
            if table[x][y-1][0]:
                c += 1
        elif y == 0:
            if table[x+1][y][0]:
                c += 1
            if table[x+1][y+1][0]:
                c += 1
            if table[x][y+1][0]:
                c += 1
        else:
            if table[x+1][y][0]:
                c += 1
            if table[x+1][y-1][0]:
                c += 1
            if table[x][y-1][0]:
                c += 1
            if table[x+1][y+1][0]:
                c += 1
            if table[x][y+1][0]:
                c += 1
    else:
        if y == n-1:
            if table[x-1][y][0]:
                c += 1
            if table[x-1][y-1][0]:
                c += 1
            if table[x][y-1][0]:
                c += 1
            if table[x+1][y-1][0]:
                c += 1
            if table[x+1][y][0]:
                c += 1
        elif y == 0:
            if table[x-1][y][0]:
                c += 1
            if table[x-1][y+1][0]:
                c += 1
            if table[x][y+1][0]:
                c += 1
            if table[x+1][y+1][0]:
                c += 1
            if table[x+1][y][0]:
                c += 1
        else:
            if table[x][y+1][0]:
                c += 1
            if table[x+1][y][0]:
                c += 1
            if table[x-1][y][0]:
                c += 1
            if table[x+1][y+1][0]:
                c += 1
            if table[x-1][y-1][0]:
                c += 1
            if table[x][y-1][0]:
                c += 1
            if table[x-1][y+1][0]:
                c += 1
            if table[x+1][y-1][0]:
                c += 1
    return c


def test_nb_bombe_voisin():
    assert nb_bombe_voisin(test2, (1, 1)) == 2
    assert nb_bombe_voisin(test3, (2, 3)) == 4
    assert nb_bombe_voisin(test4, (5, 2)) == 2


# Une première fonction pour représenter notre grille.
# si la case n'a pas été visité et non marquée, elle sera représentée par un vide . si elle a été marquée , elle contiendra "M". Si elle a été visitée et appartient à un connexe elle contiendra 'v', et enfin si elle a été visité et est à la frontière , elle contiendra un indice


def grid_to_string(table):
    string = ''
    c = len(table[0])
    l = len(table)
    for i in range(l):
        string += ' ==='*c
        string += '\n'
        string += '| '
        for j in range(c):
            x, y = pci((j+1, i+1))
            if table[x][y][1]:
                if table[x][y][0]:
                    string += 'B'
                elif connexe_test(table, (j+1, i+1)):
                    string += 'v'
                elif table[x][y][0]:
                    string += 'B'
                else:
                    string += str(nb_bombe_voisin(table, (j+1, i+1)))
            elif table[x][y][2] == 1:
                string += 'M'
            elif table[x][y][2] == 2:
                string += '?'
            else:
                string += ' '
            string += ' | '
        string += '\n'
    string += ' ==='*c
    return string
    print(string)


def test_grid_to_string():
    a = ' === === === === === === ===\n| B | B | B | 2 | B | 1 | v | \n === === === === === === ===\n| B | 6 | 4 | 4 | 2 | 2 | 1 | \n === === === === === === ===\n| B | 6 | B | B | 2 | 1 | B | \n === === === === === === ===\n| B | B | B | B | 2 | 1 | 1 | \n === === === === === === ===\n| B | B | B | 3 | 1 | v | v | \n === === === === === === ==='
    Mark_all_as_visited(test3)
    print(a)
    b = ' === === ===\n| B | 3 | B | \n === === ===\n| 2 | B | 3 | \n === === ===\n| 2 | 4 | B | \n === === ===\n| 1 | B | B | \n === === ==='
    print(b)
    Mark_all_as_visited(test2)
    assert grid_to_string(test2) == a
    assert grid_to_string(test3) == b

# rajout d'axe pour fciliter la lecture


def grid_to_string_with_axes(table):
    string = ''
    c = len(table[0])
    l = len(table)
    string += '  1'
    string += "".join(['   ' + str(i) for i in range(2, c+1)])
    string += '\n'
    for i in range(l):
        string += ' '
        string += ' ==='*c
        string += '\n'
        string += str(i+1) + '| '
        for j in range(c):
            x, y = pci((j+1, i+1))
            if table[x][y][1]:
                if table[x][y][0]:
                    string += 'B'
                else:
                    if connexe_test(table, (j+1, i+1)):
                        string += 'v'
                    else:
                        string += str(nb_bombe_voisin(table, (j+1, i+1)))
            elif table[x][y][2] == 1:
                string += 'M'
            elif table[x][y][2] == 1:
                string += '?'
            else:
                string += ' '
            string += ' | '
        string += '\n'
    string += ' '
    string += ' ==='*c
    print(string)


# On va essayer de determiner les connexes de la  grille générée. un connexe = un ensemble de point sans mines. Au tour de chaque point d'un connexe, il n'y a aucun mine.

# Si le joueur  décide de visiter un point appartenant à un connexe , il dévoile automatiquement tout les autres points appartenant à ce connexe ainsi que les points extremaux et les indices les contenants.

# un point appartient à un connexe si et seulement il n'a pas de bombe au tour.


# ces trois fonctions sont pas importantes, elles servent à s'implifier le code (dernière étape).

def pci(point):  # retourn x,y
    a, b = point
    return b-1, a-1


def pcf(point):  # retourn a,b
    a, b = point
    return b+1, a+1


def ajouter_el(l, e):
    if not(e in l):
        return l + [e]
    else:
        return l

# la fonction suivante permet d'indiquer si un point appartient à un connexe.


def connexe_test(table, point):
    x, y = pci(point)
    if table[x][y][0]:
        return False
    elif nb_bombe_voisin(table, point) == 0:
        return True
    else:
        return False


def test_connexe_test():
    assert connexe_test(test2, (7, 5))
    assert not(connexe_test(test3, (1, 3)))
    assert not(connexe_test(test4, (4, 4)))


# La suivante permet de déterminer le connexe auquel appartient un point , lorsque ce point appartient à un connexe.
# elle va avoir une apporche réccursive, parcourrant la table de proche en proche

def connexe_appartient(table, point):
    a, b = point
    x, y = pci(point)
    print((x, y))
    connexe = [point]
    h = len(table)
    print(h)
    n = len(table[0])
    print(n)
    def aux(pnt, l):
        x, y = pci(pnt)
        if x == h-1:
            # beaucoups de if encore.
            if y == n-1:
                if not(pcf((x-1, y)) in l):
                    l.append(pcf((x-1, y)))
                    if connexe_test(table, (pcf((x-1, y)))):
                        aux(pcf((x-1, y)), l)
                if not(pcf((x-1, y-1)) in l):
                    l.append(pcf((x-1, y-1)))
                    if connexe_test(table, (pcf((x-1, y-1)))):
                        aux(pcf((x-1, y-1)), l)
                if not(pcf((x, y-1)) in l):
                    l.append(pcf((x, y-1)))
                    if connexe_test(table, (pcf((x, y-1)))):
                        aux(pcf((x, y-1)), l)
            elif y == 0:
                if not(pcf((x-1, y)) in l):
                    l.append(pcf((x-1, y)))
                    if connexe_test(table, (pcf((x-1, y)))):
                        aux(pcf((x-1, y)), l)
                if not(pcf((x-1, y+1)) in l):
                    l.append(pcf((x-1, y+1)))
                    if connexe_test(table, (pcf((x-1, y+1)))):
                        aux(pcf((x-1, y+1)), l)
                if not(pcf((x, y+1)) in l):
                    l.append(pcf((x, y+1)))
                    if connexe_test(table, (pcf((x, y+1)))):
                        aux(pcf((x, y+1)), l)
            else:
                if not(pcf((x-1, y)) in l):
                    l.append(pcf((x-1, y)))
                    if connexe_test(table, (pcf((x-1, y)))):
                        aux(pcf((x-1, y)), l)
                if not(pcf((x-1, y-1)) in l):
                    l.append(pcf((x-1, y-1)))
                    if connexe_test(table, (pcf((x-1, y-1)))):
                        aux(pcf((x-1, y-1)), l)
                if not(pcf((x, y-1)) in l):
                    l.append(pcf((x, y-1)))
                    if connexe_test(table, (pcf((x, y-1)))):
                        aux(pcf((x, y-1)), l)
                if not(pcf((x-1, y+1)) in l):
                    l.append(pcf((x-1, y+1)))
                    if connexe_test(table, (pcf((x-1, y+1)))):
                        aux(pcf((x-1, y+1)), l)
                if not(pcf((x, y+1)) in l):
                    l.append(pcf((x, y+1)))
                    if connexe_test(table, (pcf((x, y+1)))):
                        aux(pcf((x, y+1)), l)
        elif x == 0:
            if y == n-1:
                if not(pcf((x, y-1)) in l):
                    l.append(pcf((x, y-1)))
                    if connexe_test(table, pcf((x, y-1))):
                        aux(pcf((x, y-1)), l)
                if not(pcf((x+1, y-1)) in l):
                    l.append(pcf((x+1, y-1)))
                    if connexe_test(table, (pcf((x+1, y-1)))):
                        aux(pcf((x+1, y-1)), l)
                if not(pcf((x+1, y)) in l):
                    l.append(pcf((x+1, y)))
                    if connexe_test(table, (pcf((x+1, y)))):
                        aux(pcf((x+1, y)), l)
            elif y == 0:
                if not(pcf((x, y+1)) in l):
                    l.append(pcf((x, y+1)))
                    if connexe_test(table, pcf((x, y+1))):
                        aux(pcf((x, y+1)), l)
                if not(pcf((x+1, y+1)) in l):
                    l.append(pcf((x+1, y+1)))
                    if connexe_test(table, (pcf((x+1, y+1)))):
                        aux(pcf((x+1, y+1)), l)
                if not(pcf((x+1, y)) in l):
                    l.append(pcf((x+1, y)))
                    if connexe_test(table, (pcf((x+1, y)))):
                        aux(pcf((x+1, y)), l)
            else:
                if not(pcf((x, y+1)) in l):
                    l.append(pcf((x, y+1)))
                    if connexe_test(table, (pcf((x, y+1)))):
                        aux(pcf((x, y+1)), l)
                if not(pcf((x+1, y)) in l):
                    l.append(pcf((x+1, y)))
                    if connexe_test(table, (pcf((x+1, y)))):
                        aux(pcf((x+1, y)), l)
                if not(pcf((x+1, y+1)) in l):
                    l.append(pcf((x+1, y+1)))
                    if connexe_test(table, (pcf((x+1, y+1)))):
                        aux(pcf((x+1, y+1)), l)
                if not(pcf((x, y-1)) in l):
                    l.append(pcf((x, y-1)))
                    if connexe_test(table, (pcf((x, y-1)))):
                        aux(pcf((x, y-1)), l)
                if not(pcf((x+1, y-1)) in l):
                    l.append(pcf((x+1, y-1)))
                    if connexe_test(table, (pcf((x+1, y-1)))):
                        aux(pcf((x+1, y-1)), l)
        else:
            if y == n-1:
                if not(pcf((x-1, y)) in l):
                    l.append(pcf((x-1, y)))
                    if connexe_test(table, (pcf((x-1, y)))):
                        aux(pcf((x-1, y)), l)
                if not(pcf((x-1, y-1)) in l):
                    l.append(pcf((x-1, y-1)))
                    if connexe_test(table, (pcf((x-1, y-1)))):
                        aux(pcf((x-1, y-1)), l)
                if not(pcf((x, y-1)) in l):
                    l.append(pcf((x, y-1)))
                    if connexe_test(table, pcf((x, y-1))):
                        aux(pcf((x, y-1)), l)
                if not(pcf((x+1, y-1)) in l):
                    l.append(pcf((x+1, y-1)))
                    if connexe_test(table, (pcf((x+1, y-1)))):
                        aux(pcf((x+1, y-1)), l)
                if not(pcf((x+1, y)) in l):
                    l.append(pcf((x+1, y)))
                    if connexe_test(table, (pcf((x+1, y)))):
                        aux(pcf((x+1, y)), l)
            elif y == 0:
                if not(pcf((x-1, y)) in l):
                    l.append(pcf((x-1, y)))
                    if connexe_test(table, (pcf((x-1, y)))):
                        aux(pcf((x-1, y)), l)
                if not(pcf((x-1, y+1)) in l):
                    l.append(pcf((x-1, y+1)))
                    if connexe_test(table, (pcf((x-1, y+1)))):
                        aux(pcf((x-1, y+1)), l)
                if not(pcf((x, y+1)) in l):
                    l.append(pcf((x, y+1)))
                    if connexe_test(table, pcf((x, y+1))):
                        aux(pcf((x, y+1)), l)
                if not(pcf((x+1, y+1)) in l):
                    l.append(pcf((x+1, y+1)))
                    if connexe_test(table, (pcf((x+1, y+1)))):
                        aux(pcf((x+1, y+1)), l)
                if not(pcf((x+1, y)) in l):
                    l.append(pcf((x+1, y)))
                    if connexe_test(table, (pcf((x+1, y)))):
                        aux(pcf((x+1, y)), l)
            else:
                if not(pcf((x, y+1)) in l):
                    l.append(pcf((x, y+1)))
                    if connexe_test(table, (pcf((x, y+1)))):
                        aux(pcf((x, y+1)), l)
                if not(pcf((x+1, y)) in l):
                    l.append(pcf((x+1, y)))
                    if connexe_test(table, (pcf((x+1, y)))):
                        aux(pcf((x+1, y)), l)
                if not(pcf((x-1, y)) in l):
                    l.append(pcf((x-1, y)))
                    if connexe_test(table, (pcf((x-1, y)))):
                        aux(pcf((x-1, y)), l)
                if not(pcf((x+1, y+1)) in l):
                    l.append(pcf((x+1, y+1)))
                    if connexe_test(table, (pcf((x+1, y+1)))):
                        aux(pcf((x+1, y+1)), l)
                if not(pcf((x-1, y-1)) in l):
                    l.append(pcf((x-1, y-1)))
                    if connexe_test(table, (pcf((x-1, y-1)))):
                        aux(pcf((x-1, y-1)), l)
                if not(pcf((x, y-1)) in l):
                    l.append(pcf((x, y-1)))
                    if connexe_test(table, (pcf((x, y-1)))):
                        aux(pcf((x, y-1)), l)
                if not(pcf((x-1, y+1)) in l):
                    l.append(pcf((x-1, y+1)))
                    if connexe_test(table, (pcf((x-1, y+1)))):
                        aux(pcf((x-1, y+1)), l)
                if not(pcf((x+1, y-1)) in l):
                    l.append(pcf((x+1, y-1)))
                    if connexe_test(table, (pcf((x+1, y-1)))):
                        aux(pcf((x+1, y-1)), l)
    aux(point, connexe)
    return connexe

def test_connexe_appartient():
    assert [(7, 5), (7, 4), (6, 4), (6, 5), (5, 4),
            (5, 5)] == connexe_appartient(test2, (7, 5))
    assert [(7, 1), (6, 1), (6, 2), (7, 2)
            ] == connexe_appartient(test2, (7, 1))

# maintenant  notre joueur peut peu être jouer

# testons que le jeu n'est pas game over = une case avec une bombe a été visité

def is_it_game_over(table):
    for i in table:
        for j in i:
            if j[0] and j[1]:
                return True
    return False

# testons que le jeu n'est pas fini = toute les cases sans bombe ont été visitée et les cases avec ont été marquée.


def is_it_over(table):
    for i in table:
        for j in i:
            if not(j[0]) and not(j[1]):
                return False
            elif j[0] and j[2] == 1:
                return False
    return True


possible_moves = ["Mark", "Visit", "Unmark"]

# des commendes simples.


def visit_point(table, point):
    x, y = pci(point)
    table[x][y][1] = True
    if connexe_test(table, point):
        connexe = connexe_appartient(table, point)
        for pnt in connexe:
            a, b = pci(pnt)
            table[a][b][1] = True


def Mark_point(table, point):
    x, y = pci(point)
    if table[x][y][2] == 0:
        table[x][y][2] = 1
    if table[x][y][2] == 1:
        table[x][y][2] = 2
    if table[x][y][2] == 2:
        table[x][y][2] = 0
# On demande poliment au joueur le next Move.


def next_():
    a = input('what is your next move ? \n')
    while not(a in possible_moves):
        print(' I do not understand , please repeat \n ')
        a = input('what is your next move? \n')
    return a

# On lui demande aussi le point concerné. Remarque immportant : l'entrée doit être de la forme (x, y) > il y a un espace entre y et ,


def next_point(l, c):
    points = []
    for j in range(1, l+1):
        for i in range(1, c+1):
            points += [str((i, j))]
    point = input('which point ? \n')
    while not(point in points):
        print(' I do not understand , please repeat \n ')
        point = input('which point? \n')
    c = 0
    while point[c] != ',':
        c += 1
    a = point[1:c]
    b = point[c+1:len(point)-1]
    return (int(a), int(b))

# On lui demande la taille de la table ((a,b) pour a le nombre de colonne et b et le nombre de ligne)


def table_dimension():
    print('please do not make mistakes \n')
    point = input('what dimensions ?')
    c = 0
    while point[c] != ',':
        c += 1
    a = point[1:c]
    b = point[c+1:len(point)-1]
    return (int(a), int(b))


def lets_play():
    print('welcome \n have fun \n \n')
    c, l = table_dimension()
    table = create_grid(l, c)
    # table=test2
    print(table)
    print(' let us begin ! \n ')
    print(grid_to_string_with_axes(table))
    while not(is_it_game_over(table)) and not(is_it_over(table)):
        next_move = next_()
        point = next_point(l, c)
        i = possible_moves.index(next_move)
        if i == 0:
            Mark_point(table, point)
        if i == 1:
            visit_point(table, point)
        print(grid_to_string_with_axes(table))
    if is_it_game_over(table):
        print(' \n G A M E O V E R ')
    if is_it_over(table):
        print(' \n W I N N E R')
    Mark_all_as_visited(table)
    print(grid_to_string_with_axes(table))
    return table


def Mark_all_as_visited(table):
    for a in table:
        for b in a:
            b[1] = True


def Print_list(table):
    l = [[] for i in range(len(table))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j][0]:
                l[i] += ['B']
            else:
                if connexe_test(table, pcf((i, j))):
                    l[i] += ['v']
                else:
                    l[i] += [nb_bombe_voisin(table, pcf((i, j)))]
    return l
