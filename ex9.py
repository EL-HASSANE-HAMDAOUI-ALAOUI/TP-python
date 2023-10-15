tva = 0.2

na1 = input("Entrez le nom du premier article : ")
qa1 = int(input("Entrez la quantite du premier article : "))
pu1 = float(input("Entrez le prix unitaire du premier article : "))

na2 = input("Entrez le nom du premier article : ")
qa2 = int(input("Entrez la quantite du premier article : "))
pu2 = float(input("Entrez le prix unitaire du premier article : "))

ht1 = pu1 * qa1
ht2 = pu2 * qa2
ttc = (ht1 + ht2) + (ht1 + ht2) * tva

print("Totale pour l'article ", na1 ," est: ", ht1 ," DH (HT)")
print("Totale pour l'article ", na2 ," est: ", ht2 ," DH (HT)")
print("Totale de la facture est: ", ttc ," DH (TTC)")
