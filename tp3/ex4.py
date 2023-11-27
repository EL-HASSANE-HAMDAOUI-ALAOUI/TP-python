def conversion_temps(h, min, s):
    return h * 3600 + min * 60 + s

def temps_ecoule(h1, min1, s1, h2, min2, s2):
    temps1 = conversion_temps(h1, min1, s1)
    temps2 = conversion_temps(h2, min2, s2)
    duree = abs(temps2 - temps1)
    return duree


duree = temps_ecoule(1, 30, 0, 2, 15, 45)
print("Temps écoulé en secondes:", duree)