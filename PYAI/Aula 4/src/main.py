from universidade.professor import Professor
from universidade.professor_adjunto import ProfessorAdjunto
from universidade.professor_substituto import ProfessorSubstituto
from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina

# Exemplo de CPF válido: 25549802171
# Exemplo de CPF inválido: 11111111111

try:
    ts = ProfessorSubstituto("João", 11111111111)
    ta = ProfessorAdjunto("Maria", 22222222222)
    disc1 = Disciplina("Orientação a Objetos", 60, ta)
    disc2 = Disciplina("Algoritmos",60,ts)

    #print(disc1.nome)
    print(disc1.professor.nome)
    print(disc1.professor._calcular_bonus())

    #print(disc2.nome)
    print(disc2.professor.nome)
    print(disc2.professor._calcular_bonus())

except ValueError as e:
    print("Erro de valor:", e)
except TypeError as e:
    print("Erro de tipo:", e)
except Exception as e:
    print("Erro genérico:", e)

