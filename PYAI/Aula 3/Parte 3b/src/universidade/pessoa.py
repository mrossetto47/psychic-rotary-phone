# Criando a classe Pessoa dentro do 'pacote' universidade
# Isso serve para dizer 'como uma pessoa funciona', ou seja, quais são os atributos e métodos que uma pessoa tem
# Atributos são as características de uma pessoa, como nome, cpf, idade, etc.
# Métodos são as ações que uma pessoa pode realizar, como falar, andar, comer, etc.
# Isto ainda não está 'criando' uma pessoa, mas sim dizendo 'como uma pessoa funciona'

class Pessoa: # Criando a classe Pessoa 
    def __init__(self, nome=None, cpf=-1):# O método __init__ é o método construtor da classe, ou seja, é o método que é chamado quando uma pessoa é criada.
        self.nome = nome # O atributo nome é uma string que armazena o nome da pessoa, e é inicializado como None (vazio)
        self.cpf = cpf    # O atributo cpf é uma string que armazena o cpf da pessoa, e é inicializado como -1 (valor inválido)

# Utilizamos (self) para referenciar os atributos e métodos da própria classe, ou seja, para dizer 'esta pessoa tem um nome' ou 'esta pessoa tem um cpf'
# O duplo underscore (__) antes do nome do atributo é uma convenção para indicar que o atributo é privado, ou seja, que ele não deve ser acessado diretamente de fora da classe, mas sim através de métodos públicos (getters e setters) que serão criados posteriormente.
# Isso é uma forma de encapsulamento, ou seja, de proteger os dados da pessoa e garantir que eles sejam acessados e modificados de forma controlada.
# Por exemplo, se quisermos acessar o nome de uma pessoa, devemos criar um método público (getter) que retorne o valor do atributo nome, e se quisermos modificar o nome de uma pessoa, devemos criar um método público (setter) que receba um novo valor para o atributo nome e o atribua ao mesmo.
# Isso é importante para garantir que o nome da pessoa seja sempre uma string válida, e não um valor inválido como None ou um número, por exemplo.
# Na prática, isso significa que não devemos acessar o atributo nome diretamente, como p1.__nome, mas sim através de um método público, como p1.get_nome(), que retornará o valor do atributo nome de forma segura e controlada.

# Vamos utilizar o @property para criar os getters e setters de forma mais simples e elegante, sem precisar criar métodos separados para cada atributo. 
# O @property é um decorador que transforma um método em uma propriedade, ou seja, em um atributo que pode ser acessado e modificado como se fosse um atributo normal, mas que na verdade é um método que executa uma lógica de validação ou processamento antes de retornar ou modificar o valor do atributo.

@property
def nome(self):
    return self.__nome
@nome.setter
def nome(self, nome):
    self.__nome = nome

@property
def cpf(self):
    return self.__cpf
@cpf.setter
def cpf(self, cpf):
    self.__cpf = cpf

# Por que fizemos tudo isso? Para garantir que o nome e o cpf da pessoa sejam sempre válidos, ou seja, que o nome seja uma string e o cpf seja um número ou uma string no formato correto.
# Isso é importante para evitar erros e inconsistências no nosso programa, e para garantir que os dados da pessoa sejam sempre confiáveis e utilizáveis.
# Além disso, isso é uma boa prática de programação orientada a objetos, que nos ajuda a organizar e estruturar nosso código de forma mais clara e eficiente, e a proteger os dados da pessoa de acessos e modificações indevidas.
# Isso permite fazer validações e tratamentos de erros de forma mais fácil e centralizada, e a garantir que o nosso programa funcione de forma correta e robusta.
# Exemplo, estou criando uma classe numa empresa, e quero garantir que o nome do funcionário seja sempre uma string, e o cpf seja sempre um número ou uma string no formato correto, para evitar erros e inconsistências no meu programa, e para garantir que os dados do funcionário sejam sempre confiáveis e utilizáveis.
# Para isso, eu posso criar uma classe Funcionario com os atributos nome e cpf, e utilizar o @property para criar os getters e setters de forma mais simples e elegante, garantindo que o nome e o cpf do funcionário sejam sempre válidos.

# Agora, vamos criar um método privado (com duplo underscore) para validar o cpf, ou seja, para verificar se o cpf é um número ou uma string no formato correto, e se ele é válido de acordo com as regras de validação do cpf.
# O método privado é um método que não deve ser acessado diretamente de fora da classe, mas sim através de métodos públicos que o utilizem para validar o cpf antes de atribuir um novo valor para o atributo cpf.

def __validar_cpf(self, cpf_teste):
    somatorio_valida_ultimo = 0
    somatorio_valida_penultimo = 0
    ultimo = cpf_teste % 10
    cpf_teste //= 10
    penultimo = cpf_teste % 10
    cpf_teste //= 10
    somatorio_valida_ultimo = penultimo * 2
    for i in range(2, 12):
        modulo = cpf_teste % 10
        cpf_teste //= 10
        somatorio_valida_penultimo += modulo * i
        somatorio_valida_ultimo += modulo * (i + 1)
    modulo = somatorio_valida_penultimo % 11
    if modulo < 2:
        if penultimo != 0:
            return False # CPF inválido
    else:
        if penultimo != 11 - modulo:
            return False # CPF inválido
    modulo = somatorio_valida_ultimo % 11
    if modulo < 2:
        if ultimo != 0:
            return False # CPF inválido
    else:
        if ultimo != 11 - modulo:
            return False # CPF inválido
    return False # CPF inválido
    return True # CPF válido