"""EX. 1: Hello World Personalizado
# Peça o nome do usuário e imprima uma mensagem de boas-vindas personalizada
# Exemplo: 'Olá, André! Seja bem-vinda à Especialização em IA Generativa!'"""

# Mensagem inicial ao usuario
print("Olá! Este programa irá pedir seu nome e dar uma mensagem de boas-vindas personalizada.\n"
      "Pressione Enter para continuar...") 
input()  # Espera o usuário pressionar Enter

# Recebendo o nome do usuário
nome = input("Por favor, digite seu nome:\n")

# Imprimindo a mensagem de boas-vindas personalizada
print(f"\nOlá, {nome}! Seja bem-vindo à Especialização em IA Generativa!")

########################################################################################