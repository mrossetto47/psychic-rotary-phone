"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 2 - INTERMEDIÁRIO
-----------------------

7. LISTAS DENTRO DE LISTAS
   Faça um programa que crie uma matriz 3x3 (3 linhas e 3 colunas) preenchida com números 
   fornecidos pelo usuário. No final, exiba a matriz na tela e mostre:
   - A soma de todos os elementos
   - A soma da primeira linha
   - A soma da diagonal principal
   """

# Mensagem inicial ao usuario
print("Olá! Este programa irá ler uma matriz 3x3 informada por você e realizar alguns cálculos com ela.\n" \
"Para isso, você inserirá linha por linha.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando as listas necessárias
linha1 = []
linha2 = []
linha3 = []
matriz = []

#Pedindo ao usuário a primeira linha separada por espaços
linha1 = [int(x) for x in input("Digite a primeira linha separada por espaços:").split()]
#Pedindo ao usuário a segunda linha separada por espaços
linha2 = [int(x) for x in input("Agora, digite a segunda linha separada por espaços:").split()]
#Pedindo ao usuário a segunda linha separada por espaços
linha3 = [int(x) for x in input("Agora, digite a terceira linha separada por espaços:").split()]

# Criando a matriz
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)

# Mensagem ao Usuário
print("A matriz digitada é:\n", matriz[0],"\n",matriz[1],"\n",matriz[2])
print("Agora, faremos os cálculos.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Calculando a soma de todos os elementos
sum_1 = sum(linha1)
sum_all = sum_1+sum(linha2)+sum(linha3)

print(sum_all)