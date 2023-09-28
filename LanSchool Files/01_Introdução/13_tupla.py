"""
Tuplas >>> Tuple

Tuplas não são mutáveis, uma vez criada, permanecerá tal qual durante do o código.
- Aceita assim como as listas, quaisquer tipos de dados.

Sintaxe's
variável = ()
variável = tuple()

Tuplas são definidas por , e não por uso de parenteses.

Métodos de adição, remoção, alteração, ordenação em tuplas não existem.

Utilizamos em coleções que não sofrem alterações.
"""

# Criando uma tupla
tupla = ()
tupla2 = tuple()
tupla3 = ('Mi',30,1,0)

meses_anos = ('Janeiro','Fevereiro','março')
usuarios = 'Mic','Maria','Joao'
numeros = (10,9,8,7,6,5,5,5,2,1,4,3)

print(sum(numeros))
print(max(numeros))
print(min(numeros))

for pessoa in usuarios:
     print(f'Boa Tarde {pessoa}')
for pessoa in usuarios[0:2]: #fatiando
     print(f'Boa Tarde {pessoa}')
# print(type(usuarios))
# o que define uma dupla é ter mais de um elemento
# tuplas não podem ser alteradas, listas sim. 
# posso ter valores repetidos em tuplas
# sem limite de tamanho



