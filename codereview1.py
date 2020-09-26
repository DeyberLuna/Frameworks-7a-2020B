import os
from random import randint
# Functions:::::::::::::::::::::::::::::


def dices():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    tot = d1 + d2
    return [d1, d2, tot]


# Main::::::::::::::::::::::::::::::::::
os.system("cls")
i = 1
total=0
totalpa=0
totalim=0
print("Bienvenido")
nu=int(input('introduce el numero de veces que lanzaras el dado '))
while i <= nu :
    print("Tiro Nro: ", i)
    dd = dices()
    print("d1: ", dd[0])
    print("d2: ", dd[1])
    print("Total: ",dd[2])
    i = i + 1
    total+=dd[2]
    if dd[0]==dd[1]==6:
         print("el par de 6 fue alcanzado en el intento  ", i)
         break
    if dd[2]%2==0:
        totalpa+=1
    else:totalim+=1
    if i!=nu:print("limite alcanzado\n")


    else:key = input("::: Lanzar nuevamente :::") 

print("sumatoria del valor total de lanzados: ",total)  
print("total de pares generados: ", totalpa)
print("total de impares generados: ",totalim)