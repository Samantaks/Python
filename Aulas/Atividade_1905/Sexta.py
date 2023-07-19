

# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;


PRIMEIRO_LADO = float(input("Qual o primeiro lado do Triângulo? "))
SEGUNDO_LADO = float(input("Qual o segundo lado do Triângulo? "))
TERCEIRO_LADO = float(input("Qual o terceiro lado do Triângulo? "))

PRIMEIRA_SOMA = PRIMEIRO_LADO + SEGUNDO_LADO  #comparar com o terceiro
SEGUNDA_SOMA = PRIMEIRO_LADO + TERCEIRO_LADO  #Comparar com o segundo
TERCEIRA_SOMA = SEGUNDO_LADO + TERCEIRO_LADO  #Comparar com o primeiro

while (PRIMEIRA_SOMA <= TERCEIRO_LADO) or (SEGUNDA_SOMA <= SEGUNDO_LADO) or (TERCEIRA_SOMA <= PRIMEIRO_LADO):
    print ("Não irá formar um triangulo devido o tamanho dos lados informado. Então pedirei os lados novamente.")
    print ("-----------------------------------")
    PRIMEIRO_LADO = float(input("Qual o primeiro lado do Triângulo? "))
    SEGUNDO_LADO = float(input("Qual o segundo lado do Triângulo? "))
    TERCEIRO_LADO = float(input("Qual o terceiro lado do Triângulo? "))
        
if PRIMEIRO_LADO == SEGUNDO_LADO == TERCEIRO_LADO :
    print ("O triangulo em questão é equilátero, ou seja, possui os três lados iguais")
    
if (PRIMEIRO_LADO == SEGUNDO_LADO != TERCEIRO_LADO) or (PRIMEIRO_LADO == TERCEIRO_LADO != SEGUNDO_LADO) or (SEGUNDO_LADO == TERCEIRO_LADO != PRIMEIRO_LADO):
    print ("O triangulo em questão é isósceles, ou seja, possui dos lados iguais")

if PRIMEIRO_LADO != SEGUNDO_LADO and SEGUNDO_LADO != TERCEIRO_LADO: 
    print ("O triangulo em questão é escaleno, ou seja, os três lados possuem valores diferentes")