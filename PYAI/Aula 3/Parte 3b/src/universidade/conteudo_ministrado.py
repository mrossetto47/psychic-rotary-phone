class ConteudoMinistrado:
    def __init__(self, descricao, carga_horaria):
        self.__descricao = descricao
        self.__carga_horaria = carga_horaria

    @property
    def descricao(self):
        return self.__descricao

    @property
    def carga_horaria(self):
        return self.__carga_horaria