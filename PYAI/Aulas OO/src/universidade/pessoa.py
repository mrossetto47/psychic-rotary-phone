class Pessoa:
    def __init__(self, nome=None, cpf=-1):
        self.__nome = nome
        if cpf != -1 and self.__validar_cpf(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = -1

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
        if self.__validar_cpf(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = -1 #Indica CPF inválido



    def __validar_cpf(self,cpf_teste):
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
        
        return True # CPF válido

# O duplo underscore torna o atributo privado (pode ser acessado apenas dentro da classe)
# Com isso, vamos precisar criar funções para que os atributos possam ser modificados "de fora"
# Essas funções são os "setters" e "getters (@property)"
# Eles criam um atributo "virtual" que pode ser acessado de fora, mas que na verdade é um método (função) da classe
# Podemos utilizar os setters para validação (por exemplo a função validar cpf)