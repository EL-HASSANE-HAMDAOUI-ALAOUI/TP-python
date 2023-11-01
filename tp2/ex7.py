L = [1, 2, 5, 8, 6, 2, 5, 9, 7, 4, 3 , 3, 1, 8, 8]

i = 0
while i < len(L):
    n = L[i]
    j = i + 1
    while j < len(L):
        if L[j] == n:
            L.pop(j) 
        else:
            j += 1
    i += 1

print("La liste après suppression des doublons est :\nL =", L)
