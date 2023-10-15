t = int(input("Veillez saisir  le temps en seconde : "))
h = int(t / 3600)
m = int((t - h*3600) / 60)
s = t - (h*3600 + m*60)

print(t , " secondes= " , h , "h" , m , "min" , s , "sec")