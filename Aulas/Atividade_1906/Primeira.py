def tabuada ():
    PRIMEIRO = float(input("Digite um número para realizar as 4 operações: "))
    SEGUNDO = float(input("Digite um outro número para realizar as 4 operações: "))
    
    SOMA = PRIMEIRO + SEGUNDO
    SUBTRACAO = PRIMEIRO - SEGUNDO
    MULTIPLICACAO = PRIMEIRO * SEGUNDO
    DIVICAO = PRIMEIRO / SEGUNDO
    
    print("Resultado da soma dos dois números informados: ", SOMA)
    print("Resultado da subtração do primeiro pelo segundo número: ", SUBTRACAO)
    print("Resultado da multiplicação dos dois números:", MULTIPLICACAO)
    print("Resultado da divisão do primeiro número pelo segundo: ", DIVICAO)
    
    return PRIMEIRO, SEGUNDO
    
    
tabuada()