def somme(m, n):
    total = 0
    if n>m:
        for i in range(m, n + 1):
            total += i
        return total
    else:
        for i in range(n, m + 1):
            total += i
        return total

somme_resultat = somme(5, 8)
print("Somme :", somme_resultat)