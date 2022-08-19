from random import *



armas = [".", "-", "+","*","T","Y", "|", "W", "X", "M"]

indice = randrange(len(armas))
reloj = armas[indice]
print(reloj, indice)
cont= 0
for i in reloj:
    vigbiana = str(input("Equipo vigbiana ingresa el arma con la que quieres atacar: "))
    fiotia = str(input("Equipo fiotia ingresa el arma con la que quieres atacar: "))

    if vigbiana == reloj:
        print("V")
    
    if fiotia == reloj:
        print("F")

    else:
        print("≈ EMPATE")

cont+=1   
    


