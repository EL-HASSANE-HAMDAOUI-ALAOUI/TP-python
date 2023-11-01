import random

na = random.randint(1 , 100)
ne = 7
print("On va jouer un petit jeu, je vais generer un nombre entre 1 et 100 et vous devez le deviner en 7 essais maximum.")

i=1
while ne != 0 :
    nd = int(input("Essai {}, Veuillez deviner un nombre :".format(8 - ne)))
    if nd < 1 or nd > 100 :
        print("Veillez respecter les normes du jeu et saisir un nombre entre 1 et 100 !")
    else :
        if nd < na :
            print("Oh non; je vais vous aider, veillez saisir un nombre plus grand !!")
        if nd > na :
            print("Oh non; je vais vous aider, veillez saisir un nombre plus petit !!")
        if nd == na :
            print("WoW!! Felicitations a vous.\n Vous avez devine le nombre correctement en ", i ,"essai")
            break
    i+=1
    ne-=1

if ne == 0 :
    print("Malheureusement pour vous, j'ai gagne.. \n Le nombre a deviner etait: ", na)
   
