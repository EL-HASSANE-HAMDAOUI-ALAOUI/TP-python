def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s


def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(distance, temps):
    distance_m = conversion_distance(*distance)
    temps_s = conversion_temps(*temps)
    if temps_s == 0:
        return "Division par zéro impossible"
    else:
        return distance_m / temps_s


distance = (2, 500, 30)
temps = (0, 45, 15)
vitesse_result = vitesse(distance, temps)
print("Vitesse en m/s:", vitesse_result)







