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
agenda={'Pedro':'992669870','Ana':'87745660','Gertrudes':'994470122','Alberto':'98779666','Sr. Miyagi':'444444444','Zé':'98551247'}

#Criando a variável para armazenar a opção do usuário
opt=int()

# Criando a Variável para ler o nome do contato
nome=str()

# Instruções para o usuário
opt=int(input("O que deseja fazer?\n"
"Caso queira consultar um contato pelo nome, digite 1 e Enter;\n"
"Caso queira exibir todos os contatos na agenda, digite 2 e Enter;\n" \
"Caso queira procurar se um contato específico existe na agenda, digite 3 e Enter;\n" \
"Para sair, digite 4 e pressione Enter.\n"))

# Verificando a entrada do usuário

# Se a entrada for 1, ler o nome informado pelo usuário
if opt == 1:
    nome=input ("\nDigite o nome do contato que deseja encontrar (inicial maiúscula):")
    
    # Verificando se o nome existe na agenda (dicionário)
    if nome in agenda:
        print("O telefone do contato", nome,"é: ",agenda[nome])
    else:
        print("Desculpe, contato não encontrado na agenda.")
# Se a entrada for 2, printar toda a agenda (dicionário)
elif opt == 2:
    # Printar toda a agenda (dicionário) de forma organizada
    print("\nAqui estão todos os contatos cadastrados na agenda:")
    for contato, telefone in agenda.items():
        print("Contato:", contato, "- Telefone:", telefone)
# Se a entrada for 3, ler o nome informado pelo usuário
elif opt == 3:
    nome=input ("\nDigite o nome do contato que deseja verificar se existe na agenda (inicial maiúscula):")
    
    # Verificando se o nome existe na agenda (dicionário)
    if nome in agenda:
        print("Sim, o contato", nome,"existe na agenda.")
    else:
        print("Não, o contato", nome,"não existe na agenda.")
# Se a entrada for 4, encerrar o programa
elif opt == 4:
    print("Encerrando o programa. Até mais!")
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

###########################################################################################################################

