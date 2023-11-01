c = int(input("Veillez saisir un chiffre (de 1 a 9) : "))

while (c < 1 or c > 9):
    c = int(input("Impossible !! Veillez saisir un chiffre (de 1 a 9) : "))
    
s = c + c*11 + c*111 + c*1111
print("Voici le resultat de la somme demande : ", c , "+" , c*11 ,"+", c*111 ,"+", c*1111 ,"=", s)