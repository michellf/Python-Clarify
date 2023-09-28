"""  
HERANÇA é um tipo de relacionamento entre classes 
que significa que uma classe é outra.

POLIMORFISMO é a capacidade que uma subclasse tem de 
ter métodos com o mesmo nome de sua superclasse, e o 
programa saber qual método deve ser invocado, 
especificamente (da super ou sub).  
*** um mesmo método com comportamentos diferentes
Quando um método se comporta se forma diferente ele se torna polimórfo.
POLIMORFISMO: O mesmo método tem comportamento diferentes em outras classes
GETNOME É O MÉTODO
"""
# Aplicando herança: 

# classe Pai
class Pessoa:
    def __init__(self, nome, cpf): # atributos que se repetem na classe cliente e funcionário
        self._nome = nome
        self._cpf = cpf

    def getNome(self): # novo método getNome
        return self._nome  
 
 # Classe Filha
class Cliente(Pessoa): # CLASSE CLIENTE HERDA ATRIBUTOS E MÉTODOS DA CLASSE PRINCIPAL PESSOA
    def __init__(self, nome, cpf, email):
        super().__init__(nome,cpf) # o que trago da classe principal? ** USANDO SUPER E NAO O NOME DA CLASSE PRINCIPAL.
        self._email = email 

class Func(Pessoa): # classe funcionario
   
    def __init__(self, nome, cpf, matricula):
        Pessoa.__init__(self,nome,cpf) # o que trago da classe principal? ** posso utilizar o nome da classe direto, neste caso usar o SELF
        self._matricula = matricula

#print(' ***** CLIENTE' )
# recebe a classe cliente
cliente1 = Cliente('michelle',28135798822,'mic@gmail.com')
func1 = Cliente('michelle',28135798822,1551)
# print(cliente1.getNome())
# print(' ***** FUNCIONARIO' )