"""EX. 8: Contador de Vogais
Conceitos: Strings, loops, condicionais
# Peça uma palavra ou frase e conte quantas vogais (a, e, i, o, u) ela tem
# Desafio: Conte também as consoantes
"""
# Mensagem inicial ao usuario
print("Olá! Este programa irá receber uma palavra ou frase digitada pelo usuário e contar quantas vogais tem nela.\n"
    "\nPressione Enter para continuar..." )
input()  # Espera o usuário pressionar Enter

# Criando tupla para dizer quais são as vogais
vogais=("a","á","à","â","ã","e","é","è","ê","ẽ","i","í","ì","î","ĩ","o","ó","ò","ô","õ","u","ú","ù","û","ũ")

# Criando lista para armazenar a frase do usuário e para as letras
entrada = []
letras = []

# Criando variáveis para contagem
cont_vogais=0
cont_consoante=0

# Solicitando a frase ao usuário
#while True:
entrada = input("\nPor Favor digite uma palavra ou frase...\n").split()

# Usando slicing [i:i+1] para pegar cada letra individualmente:

# Primeiro, percorremos cada palavra da lista original
for palavra in entrada:
    # Depois, usamos o tamanho da palavra para criar os índices
    for i in range(len(palavra)):
        
        # O fatiamento [i:i+1] pega o caractere na posição 'i'
        # e garante que o resultado seja uma string de 1 caractere
        letra_individual = palavra[i:i+1]
        
        # Adicionamos essa letra à nossa lista final
        letras.append(letra_individual)

# Contar quantas vogais estão na lista de letras
for i in range (len(letras)):
    if letras[i] in vogais:
        cont_vogais += 1
    cont_consoante = len(letras) - cont_vogais

print(f"\nA frase digitada possui {cont_vogais} vogais e {cont_consoante} consoantes.")
