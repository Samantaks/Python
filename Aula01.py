NOME = input("Olá, poderia me informar o seu nome?")
PRIMEIRO_NUMERO = int(input("Certo, agora poderia me informar um número?"))
SEGUNDO_NUMERO = int(input("Podes me informar um outro número?"))


SOMA = PRIMEIRO_NUMERO + SEGUNDO_NUMERO 
SUBTRACAO = PRIMEIRO_NUMERO - SEGUNDO_NUMERO
MULTIPLICACAO = PRIMEIRO_NUMERO * SEGUNDO_NUMERO
DIVISAO = PRIMEIRO_NUMERO / SEGUNDO_NUMERO
RESTO = PRIMEIRO_NUMERO % SEGUNDO_NUMERO


print("Com isso, " + NOME + ", o resultado da soma dos dois números será:", SOMA)
print("Com isso, " + NOME + ", o resultado da subtração dos dois números será:", SUBTRACAO)
print("Com isso, " + NOME + ", o resultado da multiplicação dos dois números será:", MULTIPLICACAO)
print("Com isso, " + NOME + ", o resultado da divisão dos dois números será:", DIVISAO)
print("Com isso, " + NOME + ", o resto da divisão dos dois números será:", RESTO)