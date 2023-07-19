PRIMEIRO_PRODUTO = float(input("Qual o preço do primeiro produto que você olhou?"))
SEGUNDO_PRODUTO = float(input("Qual o preço do segundo produto que você viu?"))
TERCEIRO_PRODUTO = float(input("Qual o preço do terceiro produto que você olhou?"))

if PRIMEIRO_PRODUTO == SEGUNDO_PRODUTO and SEGUNDO_PRODUTO == TERCEIRO_PRODUTO:
    print ("Todos os produtos possuem o mesmo preço, podes escolher qualquer um.")
    
if PRIMEIRO_PRODUTO == SEGUNDO_PRODUTO and SEGUNDO_PRODUTO != TERCEIRO_PRODUTO: 
    if PRIMEIRO_PRODUTO > TERCEIRO_PRODUTO :
        print ("Os dois primeiros produtos informados tem um valor maior. Então compre o terceiro, o qual possui valor de:  ", TERCEIRO_PRODUTO)
    else:
        print ("Os dois primeiros produtos informados tem o valor igual, e são mais baratos que o terceiro. Podes comprar qualquer um dos que possui o valor de: ", SEGUNDO_PRODUTO)     
if PRIMEIRO_PRODUTO == TERCEIRO_PRODUTO and PRIMEIRO_PRODUTO != SEGUNDO_PRODUTO:
    if PRIMEIRO_PRODUTO > SEGUNDO_PRODUTO :
        print ("Os dois primeiros produtos informados tem um valor maior. Então compre o segundo, o qual possui valor de:  ", SEGUNDO_PRODUTO)
    else:
        print ("O primeiro e o terceiro produtos informados tem o valor igual, e são mais baratos que o segundo. Podes comprar qualquer um dos que possui o valor de: ", PRIMEIRO_PRODUTO)
if SEGUNDO_PRODUTO == TERCEIRO_PRODUTO and TERCEIRO_PRODUTO != PRIMEIRO_PRODUTO:
    if TERCEIRO_PRODUTO > PRIMEIRO_PRODUTO :
        print ("O segundo e o terceiro produto informados tem valor maior. Então compre o primeiro produto, vide valor de : ", PRIMEIRO_PRODUTO)
    else:
        print ("O primeiro produto é mais caro que os outros, os quais tem valor igual, por isso pode comprar qualquer um dos dois ultimos, os quais tem valor de: ", SEGUNDO_PRODUTO)      
        
if PRIMEIRO_PRODUTO != SEGUNDO_PRODUTO and PRIMEIRO_PRODUTO != TERCEIRO_PRODUTO and SEGUNDO_PRODUTO != TERCEIRO_PRODUTO:
    if PRIMEIRO_PRODUTO < SEGUNDO_PRODUTO and PRIMEIRO_PRODUTO < TERCEIRO_PRODUTO:
        print ("O produto mais barato é o primeiro, o qual tem valor de: ", PRIMEIRO_PRODUTO)
    if SEGUNDO_PRODUTO < PRIMEIRO_PRODUTO and SEGUNDO_PRODUTO < TERCEIRO_PRODUTO:
        print ("O produto mais barato é o segundo, o qual tem valor de: ", SEGUNDO_PRODUTO)
    if TERCEIRO_PRODUTO < SEGUNDO_PRODUTO and TERCEIRO_PRODUTO < PRIMEIRO_PRODUTO:
        print (" O produto mais barato é o terceiro, o qual tem valor de: ", TERCEIRO_PRODUTO)
