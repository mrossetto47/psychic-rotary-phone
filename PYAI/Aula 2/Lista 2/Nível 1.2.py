"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: DICIONÁRIOS)
=================================================

NÍVEL 1 - INICIANTE
-------------------

2. CONTAGEM DE CARACTERES
   Escreva um programa que receba uma palavra ou frase do usuário e crie um dicionário
   onde cada chave é uma letra e cada valor é o número de vezes que essa letra aparece.
   Considere apenas letras (ignore espaços e diferenças entre maiúsculas/minúsculas).
"""
# Mensagem inicial ao usuario
print("Olá! Este programa lerá uma palavra ou frase fornecida por você e contará quantas vezes cada letra aparece.\n"
      "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando dicionário para armazenar a contagem de caracteres
dicionario = {}

# Lendo a palavra ou frase do usuário e transformando em uma lista de caracteres, ignorando espaços
entrada = input("Digite uma palavra ou frase para contar os caracteres: ")

# Vamos processar a entrada do usuário
# Trasnformando a entrada em uma lista
lista_entrada = list(entrada)

# Devemos verificar caractere por caractere, ignorar espaços e case (caps)
# Para isso, vamos precisar de um loop
for indice in range(len(lista_entrada)):
      char = lista_entrada[indice]
      # Transformando o caractere para mínúsculo
      char = char.lower()
      # Verificando se o caractere não é um espaço (se for, ignora)
      if char != " ":
            # Verificando se o caractere já não está no dicionário
            if char not in dicionario:
            # Se não estiver, adicionar char como chave e iniciar a contagem com 1
                  dicionario[char]=1
            else:
             # Se já estiver, incrementar o valor que tem a chave char em +1
                  dicionario[char]+=1

#Mensagem final para o usuário
print("\nContagem de caracteres concluída! Aqui está o resultado:\n")

# Vamos organizar o dicionário em ordem alfabética para facilitar a leitura
dicionario = dict(sorted(dicionario.items()))

print(dicionario,"\n")      

#Poderia printar de forma mais organizada com um loop for, em uma versão mais atualizada.

###########################################################################################                 
      

