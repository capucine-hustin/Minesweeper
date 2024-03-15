import csv
import numpy as np
import os
liste=[]
with open(r"C:\Users\capuc\OneDrive\Documents\Y_train_CVw08PX.csv", encoding="Macintosh") as file_name:
    for el in file_name :
        el=el[:-1]
        ele=el.split(';')
        liste.append(ele)


n=len(liste)
d_classe={}
l_classe=[]
for i in range(1,n) :
    d_classe[int(liste[i][1])]=""

for elt in d_classe :
    l=[]
    for i in range(1,n):
        if int(liste[i][1])==elt:
            l+=[int(liste[i][0])]
    d_classe[elt]=l

import numpy as np
import matplotlib.pyplot as plt

def get_num_words_per_sample(n):
    l=[]
    for elt in d_classe :
        l+=[[elt,len(d_classe[elt])]]
    return l

print(get_num_words_per_sample(1))

def tokenize(word):
    