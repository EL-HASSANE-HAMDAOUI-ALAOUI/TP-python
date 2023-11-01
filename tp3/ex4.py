def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    duree = abs(temps2 - temps1)
    return duree


duree = temps_ecoule(1, 30, 0, 2, 15, 45)
print("Temps écoulé en secondes:", duree)