"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 1 - INICIANTE
-------------------

4. INVERTENDO A LISTA
   Escreva um programa que leia 6 palavras e as armazene em uma lista. 
   Em seguida, exiba a lista na ordem inversa sem usar o método reverse() ou fatiamento [::-1]"""

# Criando uma lista vazia para armazenar as palavras
lista_palavras = []
# Mensagem inicial ao usuário
print("Olá! Este programa irá ler 6 palavras e armazená-las em uma lista. Em seguida, exibirá a lista na ordem inversa.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Solicitando ao usuário que insira 6 palavras
for indice in range(6):
    palavra = input("Digite a " + str(indice + 1) + "ª palavra: ")
    #Verificar se a palavra é mesmo uma palavra, ou seja, se não é um número ou uma string vazia
    while True:
        if palavra.isalpha():
            break
        else:
            print("Entrada inválida. Por favor, insira uma palavra válida (apenas letras).")
            palavra = input("Digite a " + str(indice + 1) + "ª palavra: ")

    #Appendando a palavra à lista 
    lista_palavras.append(palavra)

# Mostrando ao usuário a lista atual de palavras
print("Palavras registradas:", lista_palavras)

# Mensagem ao usuário sobre a exibição da lista na ordem inversa
print("Agora, vamos exibir a lista de palavras na ordem inversa...")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter    

# Criando uma nova lista para armazenar as palavras na ordem inversa
lista_invertida = []
# Garantindo que o índice comece do último elemento da lista original, ou seja, do índice 5 (já que a lista tem 6 elementos, os índices vão de 0 a 5)
indice = 5
# Temos que pegar os elementos da lista original de trás para frente, ou seja, começando do índice 5 até o 0
while indice >=0:
    lista_invertida.append(lista_palavras[indice])
    indice -= 1

# Exibindo a lista invertida
print("Lista de palavras na ordem inversa:", lista_invertida)
########################################################################################################
