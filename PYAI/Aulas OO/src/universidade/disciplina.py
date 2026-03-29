from .conteudo_ministrado import ConteudoMinistrado
from .professor import Professor

class Disciplina: # Disciplinas devem ter nome, carga horária e professor
    def __init__(self, nome, carga_horaria = 60, professor = None):
        self.__nome = nome
        #Boa prática. Para evitar redundâncias na verificação, vamos chamar os setters aqui.
        # A verificação é feita neles, nos setters da classe Professor
        self.carga_horaria = carga_horaria
        self.professor = professor
        self.__conteudos_ministrados = []

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor):
        #Caso o objeto sendo passado não seja um professor, ou algo que derive (seja um tipo de) professor, não vamos aceitar.
        if professor is not None and not issubclass(type(professor), Professor): # Para isso usa issubclass()
            raise TypeError("parâmetro professor deve derivar da classe Professor")
        self.__professor = professor


    @property
    def conteudo_ministrado(self):
        return self.__conteudos_ministrados
    
    def adicionar_conteudo_ministrado(self, conteudo, carga):
        self.__conteudos_ministrados.append(ConteudoMinistrado(conteudo, carga))


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


# Métodos são funções adicionadas dentro das classes. São como os comportamentos da classe (Nesse caso,o que a disciplina "faz")
    def exibir_informacoes(self):
        print("Disciplina:", self.__nome)
        print("Carga Horária:", self.__carga_horaria)
        if self.__professor is not None:
            print("Professor Responsável:", self.__professor.nome)
        else:
            print("Disciplina sem professor alocado")
        
        print("Conteúdos Ministrados:")
        for cont in self.__conteudos_ministrados:
           print(f"\t->id: {cont.id} {cont.descricao} ({cont.carga_horaria} hora)")