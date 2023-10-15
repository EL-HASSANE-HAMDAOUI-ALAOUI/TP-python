n1 = int(input("Veillez saisir le premier nombre : "))
n2 = int(input("Veillez saisir le deuxieme nombre : "))
o = input("Veillez saisir l’opération à effectuer (+, -, *, /) :")

if (o == "*"):
    print("— Le produit de ces deux nombres est :" , n1 , o , n2 , " = " , n1*n2)
elif (o == "+") :
    print("— La somme de ces deux nombres est :" , n1 , o , n2 , " = " , n1+n2)
elif (o == "-") :
    print("— La soustraction de ces deux nombres est :" , n1 , o , n2 , " = " , n1-n2)    
elif (o == "/") :
    if ( n2 != 0) :
        print("— La division de ces deux nombres est :" , n1 , o , n2 , " = " , n1/n2)
    else :
        print("La division par 0 est impossible !!")
else :
    print("c'est une operation invalide !!")