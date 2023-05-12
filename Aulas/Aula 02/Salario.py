"""
    As Organizações Tabajara resolveram dar um aumento de salário aos seus 
    colaboradores e lhe contraram para desenvolver o programa que calculará 
    os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste 
    segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% 
    
    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""
    
SALARIO_ATUAL = float(input("Qual o seu salário atual? "))

if SALARIO_ATUAL < 280:
    ADITIVO = (SALARIO_ATUAL)*(20/100)
    REAJUSTE = SALARIO_ATUAL + ADITIVO
    
    print("O seu salário é: ", SALARIO_ATUAL)
    print("Você receberá um aumento de 20% !")
    print("Mais exatamente, o valor do aumento será: ", ADITIVO)
    print("O seu novo salário com o aumento será: ", REAJUSTE)
    
if SALARIO_ATUAL >= 280 and SALARIO_ATUAL < 700:
    ADITIVO = (SALARIO_ATUAL)*(15/100)
    REAJUSTE = SALARIO_ATUAL + ADITIVO
    
    print("O seu salário é: ", SALARIO_ATUAL)
    print("Você receberá um aumento de 15% !")
    print("Mais exatamente, o valor do aumento será: ", ADITIVO)
    print("O seu novo salário com o aumento será: ", REAJUSTE)
    
if SALARIO_ATUAL > 700 and SALARIO_ATUAL < 1500:
    ADITIVO = (SALARIO_ATUAL)*(10/100)
    REAJUSTE = SALARIO_ATUAL + ADITIVO
    
    print("O seu salário é: ", SALARIO_ATUAL)
    print("Você receberá um aumento de 10% !")
    print("Mais exatamente, o valor do aumento será: ", ADITIVO)
    print("O seu novo salário com o aumento será: ", REAJUSTE)
    
if SALARIO_ATUAL>= 1500:
    ADITIVO = (SALARIO_ATUAL)*(5/100)
    REAJUSTE = SALARIO_ATUAL + ADITIVO
    
    print("O seu salário é: ", SALARIO_ATUAL)
    print("Você receberá um aumento de 5% !")
    print("Mais exatamente, o valor do aumento será: ", ADITIVO)
    print("O seu novo salário com o aumento será: ", REAJUSTE)