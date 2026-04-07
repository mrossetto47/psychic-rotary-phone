"""EX. 9: Jogo da Adivinhação
Conceitos: Random, loops, condicionais
# Gere um número aleatório entre 1 e 100
# Peça para o usuário adivinhar, dando dicas de "maior" ou "menor"
# O jogo acaba quando o usuário acertar
"""
import random

# Mensagem inicial ao usuario
print("Olá! Este programa irá gerar um número inteiro aleatório (1 a 100) e você vai tentar adivinhar, conforme as dicas.\n"
    "\nPressione Enter para continuar..." )
input()  # Espera o usuário pressionar Enter

# Gerando as varíaveis
num = random.randint(1,100)
entrada=0
tentativas=0

# Loop para receber entrada do usuário
while True:
    try:
        entrada=int(input("Digite um número:\n"))
        tentativas += 1
        if entrada == num:
            print(f"Você acertou! O número é {num}. Você precisou de {tentativas} tentativas!\n")
            break
        elif entrada < num:
            print ("O número que você digitou é MENOR que o alvo!\n")
        elif entrada > num:
            print ("O número que você digitou é MAIOR que o alvo!\n")

    except:
        print ("Algo deu errado!\n")