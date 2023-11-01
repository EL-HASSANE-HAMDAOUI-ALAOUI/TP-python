L = [1,-30,0,-2,500,4,2,100]
M = []

for n in L:
    if n < 0 :
        M.append(n)

for n in L:
    if n >= 0 :
        M.append(n)

print(M)