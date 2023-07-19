PRIMEIRO_VALOR = int(input("Olá, poderia me informar um valor aleatório? "))
SEGUNDO_VALOR = int(input("Olá, poderia me informar um outro valor aleatório? "))


if(PRIMEIRO_VALOR != SEGUNDO_VALOR):
    if(PRIMEIRO_VALOR > SEGUNDO_VALOR):
        print("O número maior entre os dois será: ", PRIMEIRO_VALOR)
        
    else:
        print ("O número maior entre os dois será: ", SEGUNDO_VALOR)
        
else:
    print("Os dois número informados são iguais.")