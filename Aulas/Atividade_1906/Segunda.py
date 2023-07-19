def pares ():
    lista = []
    pares = []
    dimensao = int(input("Quantos numeros desejas que tenha na sua lista? "))
    
    for i in range (dimensao):
        valores = int(input("Digite o termo da lista: "))
        lista.append(valores)
        if valores % 2 == 0 :
            pares.append(valores)
    
    print("Os termos da lista informada é: ", lista)
    print("Dessa lista, os numeros pares são:", pares)

pares() 