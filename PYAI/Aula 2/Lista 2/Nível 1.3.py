"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: DICIONÁRIOS)
=================================================

NÍVEL 1 - INICIANTE
-------------------

3. NOTAS DOS ALUNOS
   Crie um dicionário com nomes de 4 alunos e suas respectivas notas (valor inteiro de 0 a 10).
   Depois, calcule e mostre:
   - A média da turma
   - O aluno com a maior nota
   - Quantos alunos foram aprovados (nota >= 7)"""

# Mensagem inicial ao usuario
print("Olá! Este programa tem nomes de 4 alunos e suas notas.\n"
      "Com ele, você poderá ver a média da turma, o melhor aluno e os aprovados.\n"
      "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando o dicionário com os alunos e notas
notas={'Edson Arantes do Nascimento':'10','Antônio Carlos Souza':'7.47','Maria da Silva':'8.12','João Oliveira':'6.52'}

# Printando a lista para o usuário
print("Os alunos que constam no cadastro e suas respectivas notas são:\n")
for aluno, nota in notas.items():
    print("Aluno:", aluno, "- Nota:", nota,"\n")
print("Pressione Enter para mostrar os cálculos...")
input()  # Espera o usuário pressionar Enter

# Calculando a média da turma e o número de aprovados
soma_notas=0
aprovados=0
for nota in notas.values():
   soma_notas+=float(nota)
   if float(nota) >= 7:
      aprovados+=1

media=float(soma_notas/4)
# Arredondando para duas casas decimais
media=round(media,2)

# Encontrando o aluno com a maior nota
melhor = max(notas,key=notas.get)

print("\nA média da turma é: ", media,"\n")
print("O aluno com a maior nota é", melhor, "com nota", notas[melhor],"\n")
print("A turma teve", aprovados,"alunos aprovados por média!\n")

#################################################################################################