"""
While com Break
while True: >>> este laço será executado enquanto 
não encontrar o Break pelo caminho.
Break >>> Condição de parada de um loop. (FLAG)
"""
# sintaxe
# Validando tipo de dado com break
result = 0
sinal = ""
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 1: '))

while True:
    menu = int(input('[1]SOMAR \n[2]SUBTRAIR\n[3]SAIR\nOpção: '))
    if menu > 0:
        if menu == 1:
            result = numero1+numero2
            break
        if menu == 2:
            result = numero1-numero2
            break
        else: #Opção digitada é sair-3
            break
    
    else:
        menu = int(input('[1]SOMAR \n[2]SUBTRAIR\n[3]SAIR\nOpção: '))

if menu ==1:
        sinal = "+"
if menu ==2:
        sinal = "-"


# print("A soma de", a, "+", b, "eh igual a", soma)
print("Resultado do cálculo: ",numero1, sinal, numero2, "é igual a: ", result)

print(result)
