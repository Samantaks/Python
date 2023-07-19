""" 
Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
caso.
"""
TURNO = input("Olá! Em qual turno você estuda? 'M' pra matutino, 'V' para Vespertino ou 'N'para Noturno. ")

while ( TURNO != "M") and (TURNO != "V") and ( TURNO != "N"):
    print("O nome do turno está errado, poderia me informar novamente?")
    TURNO = input("Em qual turno você estuda? 'M' pra matutino, 'V' para Vespertino ou 'N'para Noturno. ")
    
if TURNO == "M" :
    print ("Bom dia!")
    
if TURNO == "N":
    print("Boa Noite!")
    
if TURNO == "V":
    print("Boa Tarde!")