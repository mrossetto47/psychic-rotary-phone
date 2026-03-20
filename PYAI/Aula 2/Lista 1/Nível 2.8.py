"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 2 - INTERMEDIÁRIO
-----------------------

8. INTERCALANDO LISTAS
   Escreva um programa que leia duas listas de 5 elementos cada e gere uma terceira lista 
   com os elementos intercalados (primeiro da lista A, primeiro da lista B, segundo da lista A, etc.)
"""

# Mensagem inicial ao usuario
print("Olá! Este programa irá ler duas  listas de 5 elementos cada, informadas por você e irá intercalar os elementos delas.\n"
"Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando as listas necessárias
lista1=[]
lista2=[]
lista_concat=[]

#Vamos pedir para o usuário inserir a primeira lista, separada por espaços
while True:
    lista1 = input("Digite a primeira lista separada por espaços:").split()
    #Garantindo que a lista tenha 5 elementos
    if len(lista1) < 5:
        print("A lista digitada não tem 5 elementos. Tente novamente.\n")
        lista1.clear()
    elif len(lista1)>5:
        print("A lista digitada tem mais de 5 elementos. Tente novamente.\n")
        lista1.clear()
    else:
        break
    
#Vamos pedir para o usuário inserir a segunda lista, separada por espaços
while True:
    lista2 = input("\n Agora, digite a segunda lista separada por espaços:").split()
    #Garantindo que a lista tenha 5 elementos
    if len(lista2) < 5:
        print("A lista digitada não tem 5 elementos. Tente novamente.\n")
        lista2.clear()
    elif len(lista2)>5:
        print("A lista digitada tem mais de 5 elementos. Tente novamente.\n")
        lista2.clear()
    else:
        break

# Mensagem ao Usuário
print("\n As listas digitadas são:\n", "Lista 1: ",lista1,"\n Lista 2: ",lista2)
print("\n Agora, faremos a manipulação das listas.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

#Fazendo a concatenação das listas
for indice in range(5):
    lista_concat.append(lista1[indice])
    lista_concat.append(lista2[indice])

#Printando a lista intercalada
print("A lista intercalada é:\n", lista_concat)

###################################################################################