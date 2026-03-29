from .pessoa import Pessoa

# Professor é um tipo de pessoa. Como todas as pessoas, tem nome e CPF.
# Mas o professor também pode ter seus próprios atributos, como carga horária que leciona ou o valor hora-aula que recebe.

class Professor(Pessoa): #A classe Professor herda da classe Pessoa. Ou seja, Professor é um tipo de Pessoa. 
    def __init__(self, nome, cpf, valor_hora = 60, carga_horaria = 40): # Herdou algumas coisas da classe Pessoa mas tem suas próprias
        super().__init__(nome, cpf) #No Python use super() para invocar algo da classe Pai. Aqui, estamos invocando o inicializador passando o nome e cpf.
        self.__valor_hora = valor_hora # Estamos considerando valor inteiro (sem centavos)
        self.__carga_horaria = carga_horaria

# Como Professor herda de Pessoa, ele consegue fazer tudo o que uma Pessoa faz.
# Note que ele possui um nome, mesmo isso não sendo definido diretamente na classe Professor.

    @property
    def valor_hora(self):
        return self.__valor_hora
    
    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    @property
    def salario(self):
    #Carga semanal * custo * 4,5 semanas no mês
        return int(self.__valor_hora * self.__carga_horaria * 4.5)
    # Mais uma boa ideia. Não existe o atributo salário. 
    # Mas podemos fazer um get que simula esse atributo, calculando-o automaticamente.
    
# É uma má ideia representar valores monetários e afins com números “depois da vírgula” devido a erros numéricos 
# da máquina causados pela representação em ponto flutuante.
# Veja em:
    # prlalmeida.com.br/2021/10/29/digital-circuits
    # prlalmeida.com.br/2022/08/29/computer-architecture