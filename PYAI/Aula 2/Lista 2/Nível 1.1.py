"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: DICIONÁRIOS)
=================================================

NÍVEL 1 - INICIANTE
-------------------

1. AGENDA TELEFÔNICA SIMPLES
   Crie um dicionário vazio e adicione 5 contatos com nome como chave e telefone como valor.
   Depois, permita que o usuário:
   - Consulte o telefone de um contato pelo nome
   - Exiba todos os contatos cadastrados
   - Verifique se um contato específico existe na agenda
"""
# Mensagem inicial ao usuario
print("Olá! Este programa tem uma agenda telefônica simples, onde você poderá consultar contatos e seus telefones.\n"
      "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando o dicionário para armazenar os contatos
agenda={'Pedro':'992669870','Ana':'87745660','Gertrudes':'994470122'}

#Criando a variável para armazenar a opção do usuário
opt=int()

# Criando a Variável para ler o nome do contato
nome=str()

# Instruções para o usuário
opt=input("O que deseja fazer?\n"
"Caso queira consultar um contato pelo nome, digite 1 e Enter;\n"
"Caso queira exibir todos os contatos na agenda, digite 2 e Enter;\n" \
"Caso queira procurar se um contato específico existe na agenda, digite 3 e Enter;\n" \
"Para sair, digite 4 e pressione Enter.")

# Verificando a entrada do usuário

# Se a entrada for 1, ler o nome informado pelo usuário
if opt ==1:
    nome=input ("\nDigite o nome do contato que deseja encontrar (inicial maiúscula):")
    