from .conteudo_ministrado import ConteudoMinistrado

class Disciplina: # Disciplinas devem ter nome, carga horária e professor
    def __init__(self, nome, carga_horaria = 60, professor = None):
        self.__nome = nome
        if carga_horaria > 0: # Carga deve ser positiva
            self.__carga_horaria = carga_horaria
        else:
            self.__carga_horaria = -1 #Carga inválida
        self.__professor = professor
        self.__conteudos_ministrados = []

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