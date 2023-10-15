n1 = int(input("Veillez saisir le premier nombre : "))
n2 = int(input("Veillez saisir le deuxieme nombre : "))
if (n1 != 0 and n2 != 0):
    if ((n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0)):
        print("— Le produit de ces deux nombres est positif")
    else:
        print("— Le produit de ces deux nombres est negatif")
else :
    print("— Le produit de ces deux nombres est nul")
    
