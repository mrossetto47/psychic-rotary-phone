from .conteudo_ministrado import ConteudoMinistrado
from .professor import Professor

class Disciplina:
    def __init__(self, nome, carga_horaria = 60, professor=None):
        self.__nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor
        self.__conteudo_ministrado = []

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor):
        if professor is not None and not issubclass(type(professor), Professor):
            raise TypeError("parâmetro professor deve derivar da classe Professor")
        self.__professor = professor