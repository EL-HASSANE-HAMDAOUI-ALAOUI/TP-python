def delta(a, b, c):
    return b**2 - 4*a*c

def NombreRacine(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        return 2  
    elif d == 0:
        return 1  
    else:
        return 0  

def AfficheNombreRacine(a, b, c):
    n = NombreRacine(a, b, c)
    if n == 0:
        print("Aucune racine réelle")
    elif n == 1:
        print("Une racine réelle double")
    else:
        print("Deux racines réelles")

def Racine1(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        x1 = (-b + d**0.5) / (2*a)
        return x1

def Racine2(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        x2 = (-b - d**0.5) / (2*a)
        return x2
    

a, b, c = 1, -3, 2
AfficheNombreRacine(a, b, c)
print("Racine 1:", Racine1(a, b, c))
print("Racine 2:", Racine2(a, b, c))