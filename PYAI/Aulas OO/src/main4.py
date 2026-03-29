from universidade.professor import Professor
from universidade.pessoa import Pessoa

try:
    p1 = Pessoa("Maria", 11111111111)
    t1 = Professor("João", 22222222222)

    print(p1.nome)
    print(p1.cpf)

    print(t1.nome)
    print(t1.cpf)
    print(t1.salario)

except ValueError as e:
    print(e)

#Professor é um tipo de Pessoa. Possui tudo o que uma pessoa possui (nome, cpf, …).
# Relações tipo de não são reflexivas!
    # Todo Professor é uma Pessoa (é um tipo de pessoa, ou uma especialização de pessoa).
    # Nem toda Pessoa é um tipo de Professor (nem toda pessoa é professor).