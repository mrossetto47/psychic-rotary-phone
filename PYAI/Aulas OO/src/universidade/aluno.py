from .pessoa import Pessoa

class Aluno(Pessoa): # Aluno é um tipo de pessoa
    def __init__(self, nome=None, cpf=-1):
        super().__init__(nome, cpf)