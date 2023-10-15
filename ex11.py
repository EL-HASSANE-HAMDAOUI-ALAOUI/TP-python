poids = float(input("Veillez saisir votre poids en kilogrammes : "))
taille = float(input("Veillez saisir votre taille en mètres : "))

imc = poids / (taille ** 2)

print("Votre IMC est : ", imc)
print("Votre interpretation qui correspond à votre IMC est : ")

if ( imc > 40 ):
    print("obésité morbide ou massive.")
elif ( imc > 35 and imc <= 40 ):
    print("obésité sévère.")
elif ( imc > 30 and imc <= 35 ):
    print("obésité modérée.")
elif ( imc > 25 and imc <= 30 ):
    print("Surpoids.")
elif ( imc > 18.5 and imc <= 25 ):
    print("corpulence normale.")
elif ( imc > 16.5 and imc <= 18.5 ):
    print("Maigreur.")
else :
    print("Famine.")