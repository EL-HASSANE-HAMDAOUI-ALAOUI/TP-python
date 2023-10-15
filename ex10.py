login = input("Veillez saisir votre login : ")
mot_de_pass = input("Veillez saisir votre mot de passe : ")

if (login == "admin" and mot_de_pass == "admin"):
    print("Bienvenue monsieur l'admin.")
else :
    print("Votre login ou votre mot de passe est incorrect. Veuillez réessayer.")