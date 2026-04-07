"""EX. 7: Números Primos
Conceitos: Loops "while", lógica matemática
# Peça um número e diga se ele é primo ou não
# Um número primo só é divisível por 1 e por ele mesmo"""

# Mensagem inicial ao usuario
print("Olá! Este programa irá pedir um número e verificar se ele é primo ou não.")

# Solicitando o número ao usuário
while True:
    try:
        entrada = int(input("\nPor Favor digite um número inteiro...\n"))
        break
        
    except:
        print ("\nNúmero digitado inválido.")

# Checando se o número é primo

# Variáveis necessárias para a checagem
divisivel = 0
indice = 1

# Ver por quais números ele é divisível
while indice <= entrada:
    if entrada % indice == 0:
        divisivel += 1
    indice += 1

if divisivel <= 2:
    print(f"\nO número {entrada} é primo!\n")
else:
    print(f"\nO número {entrada} não é primo!\n")