BASE_QUADRILATERO = float(input("Qual o valor da base do quadrilatero em questão?"))
ALTURA_QUADRILATERO = float(input("Qual a altura do quadrilátero em questão? "))

AREA = BASE_QUADRILATERO * ALTURA_QUADRILATERO

ELEVADO = (AREA)**2

if BASE_QUADRILATERO == ALTURA_QUADRILATERO:
    print ("O quadrilatéro é um quadrado!")
    print ("A area do mesmo será: ", AREA)
    print ("O dobro da area do mesmo é: ", ELEVADO)

else:
    print ("O quadrilatéro é um retangulo de lados diferentes!")
    print ("A area do mesmo será: ", AREA)
    print ("O dobro da area do mesmo é: ", ELEVADO)