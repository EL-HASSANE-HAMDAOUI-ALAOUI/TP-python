notes = []
coefficients = []
s = 0
sc = 0
i = 0
for i in range(4) :
    n = float(input(f"Veillez saisir la note Nº {i+1} : "))
    c = int(input(f"Veillez saisir le coefficient qui correspond à la note Nº {i+1} : "))
    notes.append(n)
    coefficients.append(c)

for i in range(4) :
    s += notes [i] * coefficients [i]
    sc += coefficients [i]

moyenne = s/sc
print("La moyenne des notes de ce semestre est : ", moyenne ," ; ")

if (moyenne >= 0 and moyenne < 7) :
    print("Semetre non validé!!")
elif (moyenne >= 7 and moyenne < 10) :
    print("Session rattrapage!!")
elif (moyenne >= 10 and moyenne <= 20) :
    print("Semetre validé!!")
else :
    print("il y a une erreur au niveau des notes!!")