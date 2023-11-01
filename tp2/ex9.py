Dc = input("Veuillez Choisir la direction de conversion (euro en mad ou mad en euro) : ")

if Dc == "euro en mad":
    valeurs = []
    while True:
        euro_valeur = float(input("Veuillez saisir une valeur en euros (ou bien une saisie négative pour arrêter) : "))
        if euro_valeur < 0:
            break
        mad_valeur = euro_valeur * 10.86
        valeurs.append((euro_valeur, mad_valeur))

    print("Les valeurs que vous avez saisit converties en dirhams (MAD) :")
    for euro, mad in valeurs:
        print(f"{euro} EUR = {mad} MAD")

elif Dc == "mad en euro":
    valeurs = []
    while True:
        mad_valeur = float(input("Veuillez saisir une valeur en dirhams (ou bien une saisie négative pour arrêter) : "))
        if mad_valeur < 0:
            break
        euro_valeur = mad_valeur * 0.092
        valeurs.append((mad_valeur, euro_valeur))

    print("Les valeurs que vous avez saisit converties en euros (euro) :")
    for mad, euro in valeurs:
        print(f"{mad} mad = {euro} euro")

else :
    print("direction de conversion impossible!!")