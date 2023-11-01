L1 = [1, 3, 6, 78, 35, 88, 55]
L2 = [12, 24, 35, 24, 88, 120, 155]
L3 = []

for n in L1:
    if n in L2 and n not in L3:
        L3.append(n)

print("L'Intersection des deux listes L1 et L2 est la liste L3 = ", L3)
