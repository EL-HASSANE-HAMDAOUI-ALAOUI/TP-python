L = [-12,3,-10,1,10,-5,-2,-1,0,2,3,5,6,8,17,4,87,100]
print("La liste L = ",L)

val = int(input("Veillez choisir la valeur du nombre que vous souhaitez supprimer ses occurrences dans la liste L: "))


while val in L :
     L.remove(val)

print("La liste apres suppression des occurrences du nombre ", val ," est :\n L = ",L)

