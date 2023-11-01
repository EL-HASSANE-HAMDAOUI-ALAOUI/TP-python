L = [1, 2, 5, 8, 6, 2, 5, 9, 7, 4, 3, 3, 1, 8, 8]
Li = []

n = int(input("Veuillez saisir la valeur du nombre que vous cherchez à trouver ses occurrences dans la liste L :"))

j = 0

for i in range(len(L)):
    if L[i] == n:
        Li.append(i)
        j += 1

print("Le nombre d'occurrences du nombre", n, "dans la liste L est :", j)
print("Les indices de ces occurrences dans la liste sont :", Li)
