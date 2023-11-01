nh = int(input("Veillez saisir le nombre des heures de travail de cet employé: "))
g = input("Veillez saisir le grade de cet employé (A, B, C, D, E) :")
salaire = 0

if (g == "A"):
    salaire = (200*nh) + (1000*(int(nh/20)))
    print("Cet employé qui a un grade ", g ,", et qui a travaillé ", nh ," heures a comme salaire :" , salaire)
elif (g == "B") :
    salaire = (150*nh) + (800*(int(nh/20)))
    print("Cet employé qui a un grade ", g ,", et qui a travaillé ", nh ," heures a comme salaire :" , salaire)
elif (g == "C") :
    salaire = (120*nh) + (500*(int(nh/15)))
    print("Cet employé qui a un grade ", g ,", et qui a travaillé ", nh ," heures a comme salaire :" , salaire)    
elif (g == "D") :
    salaire = (100*nh) + (350*(int(nh/15)))
    print("Cet employé qui a un grade ", g ,", et qui a travaillé ", nh ," heures a comme salaire :" , salaire)
elif (g == "E") :
    salaire = (80*nh) + (100*(int(nh/10)))
    print("Cet employé qui a un grade ", g ,", et qui a travaillé ", nh ," heures a comme salaire :" , salaire)
else :
    print("Impossible, c'est un grade qui n'existe pas !!")