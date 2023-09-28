"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
* Enumerate -> Permite acesso ao índice
"""

# soma = 0
# for contador in range(5):
#     print(soma)

#     num = (int(input('Digite um número ')))
#     soma += num 

# print(soma)

# sintaxe


'''
Desafio de aula: Crie um sistema que receba 4 notas 
e calcule a média, ao fim apresente a média e situção
do aluno, sendo:
>7 aprovado, >5 em recuperação e <5 reprovado.
# '''

# nota = 0
# qtde = 4
# for contador in range(qtde):
#     print(nota)
#     num = (int(input('Digite um número ')))
#     nota += num 

# print({nota})

# if nota > 1:
#     media = nota / qtde 
#     print(" A média é: " + str(media))
#     if media >= 7:
#         print("Aprovado")
#     if media >= 5 and media < 7:
#         print("Em Recuperação")
#     if media < 5:
#         print("reprovado")
# else:
#     print('Tente novamente')

senha_cadastrada = str(input('Cadastre uma senha: ')).lower()
senha = ''

while senha != senha_cadastrada:
   senha = str(input('Digite sua senha para entrar: ')).lower()
   if senha!= senha_cadastrada:
      print('Senha incorreta')
   else:
        print('\033[32m\n Acesso permitido...\033[m') #cor 40 é uma cor, 41 é outra, 42 é outra, etc...
