"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 

Exemplo: Se vou cadastrar clientes, monto um molde - um cliente precisa se encaixar no molde x
         para isto preciso de um método construtor.
         Para ser cliente ele precisa ser nome, cpf, rg (isto tudo é molde)
"""

# Criar uma classe cliente   
class Cliente:
    # métodos sao criados dentro da classe
    # o primeiro é o principal
    # primeiro INIT /  self (posso acessar o dado em qq. lugar da classe) / após o self sao os atributos
    # para ser um cliente obrigatoriamente precisa ter estes 3 atributos
    # atributo privado (_xxx) padrao nomenclatura
    def __init__(self, nome, cpf, email): # isto é um método pois está dentro da função, se estivesse 
                                          # fora da classe seria uma função def xxxxx
        self._nome = nome
        self._cpf = cpf
        self._email = email

    def getNome(self): # novo método getNome
        return self._nome

class Produto:
    
    def __init__(self, codigo, nome, codcategoria): # isto é um método pois está dentro da função, se estivesse 
                                          # fora da classe seria uma função def xxxxx
        self._codigo = codigo
        self._nome= nome
        self._categoria = codcategoria

    def getNome(self): # novo método getNome
        return self._nome

# Classe que retorna dicionário
class Funcionario:
    def __init__(self, nome, cpf, matricula):
        
        self._nome = nome
        self._cpf = cpf
        self._matricula = matricula
    
    def getTudo(self): 
        return dict(
            nome = self._nome,
            cpf = self._cpf,
            email = self._matricula
        )

print(' ***** CLIENTE ' )

# recebe a classe cliente
cliente1 = Cliente('michelle',28135798822,'mic@gmail.com')
print(cliente1.getNome())

print(' ***** FUNCIONARIO DICIONARIO' )

# recebe a classe Funcionario
func1 = Funcionario('teste func',28135798822,5555)
c = func1.getTudo()
print(c['nome'])

print(' ***** PRODUTO: ' )
# recebe a classe produto
produto1 = Produto('notebook max ccc',1244,2)
print(produto1.getNome())

