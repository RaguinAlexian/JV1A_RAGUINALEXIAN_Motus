from colorama import init
init()
from colorama import Fore, Back, Style
import random

victoire = False
nbtour = 0
fichier = open("mot.txt", "r")
listeMot = fichier.read().splitlines()
chiffre = random.randint(0,9)
motatrouver = listeMot[chiffre]
ok = 0
miok = 0
nonok = 0
special = False
specialCompte = 0
double = []
lettreDouble = []
iteration = 0

while(victoire == False and nbtour < 8) :
    essai = input("Indiquez un mot à 6 lettres : ")
    for l in range(6) :
        double.append(motatrouver[l])
    for m in range(6) :
        specialCompte = 0
        for n in range(6) :
            if(double[m] == motatrouver[n]) :
                specialCompte = specialCompte + 1
            if(specialCompte == 2) :
                lettreDouble.append(motatrouver[n])
                specialCompte = 0
                special = True
    for i in range(6) :
        ok = 0
        miok = 0
        nonok = 0
        for j in range(6) :
            if(essai[i] == motatrouver[j] and i == j) :
                ok = ok + 1
            elif(essai[i] == motatrouver[j] and i != j):
                miok = miok +1
            else :
                nonok = nonok+1
        if(nonok == 6) :
            print(Back.BLUE + essai[i], end="")
            print(Style.RESET_ALL)
        elif(ok > 0) :
            if(special == True and len(lettreDouble) !=0) :
                for k in range(len(lettreDouble)) :
                    if essai[i] == lettreDouble[k] :
                        lettreDouble.pop(k)
                        print(Back.RED + essai[i], end="")
                        print(Style.RESET_ALL)
                        break
            elif(special == True and len(lettreDouble) == 0) :
                print(Back.BLUE + essai[i], end="")
                print(Style.RESET_ALL)
            elif(special == False) :
                print(Back.RED + essai[i], end="")
                print(Style.RESET_ALL)
            else :
                print(Back.RED + essai[i], end="")
                print(Style.RESET_ALL)
        elif(miok > 0 and ok == 0) :
            if(special == True and len(lettreDouble) !=0) :
                for k in range(len(lettreDouble)) :
                    if essai[i] == lettreDouble[k] :
                        lettreDouble.pop(k)
                        print(Back.YELLOW + Fore.BLACK + essai[i], end="")
                        print(Style.RESET_ALL)
                        break
            elif(special == True and len(lettreDouble) == 0) :
                print(Back.BLUE + essai[i], end="")
                print(Style.RESET_ALL)
            elif(special == False) :
                print(Back.YELLOW + Fore.BLACK + essai[i], end="")
                print(Style.RESET_ALL)
            else :
                print(Back.YELLOW + Fore.BLACK + essai[i], end="")
                print(Style.RESET_ALL)
    if(essai == motatrouver) :
        victoire = True    
    nbtour = nbtour + 1
    double = []
    lettreDouble = [] 

if(victoire == True) :
    print("Félicitation, vous avez gagné !")
else :
    print("Dommage, vous avez perdu, le mot était : ", motatrouver)
        
fichier.close()
