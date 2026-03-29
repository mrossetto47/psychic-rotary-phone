from universidade.professor import Professor
from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina

try:
    p1 = Pessoa("Maria", 11111111111)
    t1 = Professor("João", 22222222222)
    disc1 = Disciplina("Orientação a Objetos", 60, t1) 
    # Se colocar p1 aqui, dá erro, porque é uma pessoa, mas não um professor. Tente t1,  que é professor

    print(p1.nome)
    print(p1.cpf)

    print(t1.nome)
    print(t1.cpf)
    print(t1.salario)

    print(disc1.nome)
    print(disc1.professor.nome)

except ValueError as e:
    print("Erro de valor:", e)
except TypeError as e:
    print("Erro de tipo:", e)
except Exception as e:
    print("Erro genérico:", e)