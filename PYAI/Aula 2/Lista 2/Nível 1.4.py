"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: DICIONÁRIOS)
=================================================

NÍVEL 1 - INICIANTE
-------------------

4. DICIONÁRIO DE TRADUÇÃO
   Faça um mini-dicionário Português-Inglês com pelo menos 10 palavras.
   O programa deve permitir que o usuário digite uma palavra em português
   e mostre sua tradução para inglês (ou mensagem de não encontrado)."""

# Mensagem inicial ao usuario
print("Olá! Este programa é um mini-dicionário Português-Inglês.\n"
      "Você poderá digitar uma palavra em português e ver sua tradução para inglês.\n"
      "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando dicionário com as traduções (chave em PT-BR e valor como a tradução em inglês)
dicionario = {'chá':"tea",'pedra':'rock','casa':'house','carro':'car','livro':'book','gato':'cat','cachorro':'dog','sol':'sun','lua':'moon','árvore':'tree'}

# Recebendo a palavra do usuário
verbete = input("Por favor, digite a palavra cuja tradução em inglês deseja saber (somente minúsculas):\n")

# Verificar se o verbete existe no dicionário
if verbete in dicionario.keys():
    tradução = dicionario[verbete]
    print("\nA palavra",verbete,"é",tradução,"em inglês.")
else:
    print("\nInfelizmente, a palavra", verbete, "não está no dicionário ainda!")

#############################################################################################