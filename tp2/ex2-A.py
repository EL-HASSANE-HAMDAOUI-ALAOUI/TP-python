n = int(input("Veuillez taper une taille entiere pour le triangle des etoiles: "))
i=1
while i <= n:
    j = 1
    while j <= i :
        print("*",end="")
        j+=1
    print()
    i+=1
