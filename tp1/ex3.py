d = int(input("Veillez saisir la distance en kilomètre: "))
t = int(input("Veillez saisir  le temps en minute : "))
d = d * 1000
t = t * 60
v = d / t

print("la vitesse en mètre par seconde est: ", v ,"m/s.")