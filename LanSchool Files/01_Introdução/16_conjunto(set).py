# Sets
# numeros = {1 , 2, 6, 9,'leo', 4,5,6}
# conjunto2 = set()

# Algumas das principais características dos conjuntos incluem:

# Armazena apenas itens não-duplicados (únicos)
# Suporta operações matemáticas sobre conjuntos (união, intersecção, etc)
# Não é possível modificar os itens existentes, mas podemos adicionar novos elementos (sets são mutáveis).
# Suporta elementos de qualquer tipo, não-ordenados e não-indexados.
# Podem conter apenas objetos imutáveis, como strings, ints, floats e tuplas de objetos também imutáveis.
# São escritos com chaves.

# numeros.add(200)
# numeros.pop()
# numeros.discard(4)

# quando quero inserir novo item EM LISTA    .APPEND
#                                EM CONJUNTO .ADD
#                                EM DICIONÁRIO DIRETO OU UPDATE

# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
# cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
#           'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
#           'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
#           'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
#           'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
#           'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
#           'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
#           'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
#           'São Paulo', 'Rio de Janeiro', 'São Paulo']

# # total de itens da lista
# print(f'Total de Pessoas: {len(cidade)}')

# # total cidade rio de janeiro
# print(f'Total de Pessoas do RJ: {cidade.count("Rio de Janeiro")}')

# # cidades distintas - transforma lista em conjunto - automaticamente faz 
# print(f'Total de Pessoas do RJ: {set(cidade)}')

# # count distinct - transforma lista em conjunto - automaticamente faz um distinct count
# print(f'Total de Pessoas do RJ: {len(set(cidade))}')


# ***************************************************************************
# tenho o mesmo aluno nos dois cursos
curso_python = {'Leo A','Maria','Juca','Paulo','Ana','Beto','Beto'}
curso_sql = {'Leo A','Pedro','Juca','Cris','Claudia','Roberta'}

# descobrir quais alunos que estão nos dois
print(f'Total de Pessoas do Python: {len(set(curso_python))}')
print(f'Total de Pessoas do Python: {len(set(curso_sql))}')
#união de conjuntos curso_python.union(curso_sql).union().union() etc...
total_alunos1 = curso_python.union(curso_sql)
#total sem repetição dos dois conjuntos
print(total_alunos1)
print()
total_alunos2 = curso_python | curso_sql
print(total_alunos2)
print()

# alunos matriculados nos 2 cursos
ambos_curso1 = curso_python.intersection(curso_sql)
ambos_curso2 = curso_python & curso_sql 
print(ambos_curso1)
print()
print(ambos_curso2)
print()

# alunos matriculados apenas em um curso
so_python = curso_python.difference(curso_sql) 
so_sql = curso_sql.difference(curso_python) 

print('so python',so_python)
print()

print('so sql',so_sql)
print()



