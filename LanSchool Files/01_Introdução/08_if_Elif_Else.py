"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
"""

if 10 > 40: 
    print('Ok, é maior ')

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''
# Condição simples
# nota = 9.5

# if nota >= 7: 
#     print('Aluno Aprovado.')
# else: 
#     print('Aluno Reprovado.')

# Condição composta
# nota = float(input('Nota: '))

# if nota >= 5 and nota < 7:
#     print('Aluno em recuperação.')

# elif nota >= 7 and nota <= 10:
#     print('Aluno aprovado.')

# elif nota >= 0 and nota < 5:
#     print('Aluno reprovado.')

# else:
#     print('Nota inválida')

# Condição aninhada

#  Vamos criar um sistema para validadar se o cliente
# pode ou não ter uma Habilitação de acordo com a idade 
# que irá informar.

idade = int(input('Idade: '))

if idade <= 17:
    # print('Tem autorização ')
    resp = str(input('Tem autorizacao? [s | n]: ')).lower()
    if resp == 's':
         print('Vamos continuar...')
    elif resp =='n':
         print('Não vamos continuar...')
    else:
          print('Resposta inválida')

elif idade >= 18 and idade <= 130:
     print('Vamos continuar...')

else:
    print('Idade informada é inválida.')



# Operadores unitários >>> Dependem de um único valor >>> not, is
# Operadores binários >>> Dependem de mais que 1 valor >>> and, or



