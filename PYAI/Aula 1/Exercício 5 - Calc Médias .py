"""EX. 5: Calculadora de Média
Conceitos: Listas, "sum()", "len()"
# Peça 4 notas ao usuário e calcule a média
# Mostre se o aluno foi aprovado (média >= 7) ou reprovado"""

# Mensagem inicial ao usuario
print("Olá! Este programa irá pedir 4 notas e calcular a média delas, além de "
    "dizer se o aluno foi aprovado ou reprovado com base na média.\n"
    "\nPressione Enter para continuar..." )
input()  # Espera o usuário pressionar Enter

# Criando uma lista para armazenar as notas
notas = []

# Criando um índice
i=1

# Pedindo as notas para o usuário
while i <= 4:
    entr=float(input(f"Digite a {i}ª nota:\n"))
    i+=1
    notas.append(entr)

# Calculando a média
media = round(sum(notas)/4,2)

# Printando a média do aluno
print (f"\nA média do aluno foi de {media}.\n")

if media >= 7.0:
    print("Dessa forma, o aluno é considerado aprovado.\n")
else:
    print("Dessa forma, o aluno é considerado reprovado.\n")

############################################################################################