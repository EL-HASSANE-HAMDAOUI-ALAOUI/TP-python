def conversion_temps(h, min, s):
    return h * 3600 + min * 60 + s


def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(h,min,s,km,m,cm):
    distance_m = conversion_distance(h,min,s)
    temps_s = conversion_temps(km,m,cm)
    if temps_s == 0:
        return "Division par zéro impossible"
    else:
        return distance_m / temps_s



vitesse_result = vitesse(2, 500, 30, 0, 45, 15)
print("Vitesse en m/s:", vitesse_result)







