"""EX. 3: Par ou Ímpar
Conceitos: Operador "%" (módulo), condicionais "if/else"
# Peça um número ao usuário e diga se ele é par ou ímpar"""

# Mensagem inicial ao usuario
print("Olá! Este programa irá pedir um número e dizer se ele é par ou ímpar.\n"
      "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Recebendo o número do usuário
num = int(input("Por favor, digite um número inteiro:\n"))

# Para verificar se é par, a divisão dele por 2 deve ser exata (resto zero)

if num % 2 == 0:
    print(f"\nO número {num} é par.")
else:
    print(f"\nO número {num} é ímpar.")

#########################################################################################

