L = [-12,-10,-5,-2,-1,0,2,3,5,6,8,17,87,100]
val = int(input("Veillez une valeur a inserer dans la liste L: "))

i , j = 0 , len(L) - 1

while i <= j :
    n = int((i + j)/2)

    if L[n] == val :
        L.insert(n , val)
    elif L[n] < val :
        i = n + 1
    else :
        j = n - 1

L.insert(i , val)

print(L)

