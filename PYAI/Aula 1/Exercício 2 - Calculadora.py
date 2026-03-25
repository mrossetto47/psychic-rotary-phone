"""EX. 2: Calculadora de Soma
Conceitos: Tipos numéricos, conversão de tipos
# Peça dois números ao usuário e mostre a soma deles
# Desafio: Mostre também a subtração, multiplicação e divisão"""

# Mensagem inicial ao usuario
print("Olá! Este programa é uma calculadora simples que irá pedir dois números e mostrar a"
"soma, subtração, multiplicação e divisão deles.\n"
"Pressione Enter para continuar...\n")  
input()  # Espera o usuário pressionar Enter

# Recebendo os números do usuário
num1 = input("Por favor, digite o primeiro número:\n")
num2 = input("Por favor, digite o segundo número:\n")

# Convertendo as entradas para números (float)
# É necessário fazer isso porque input() semp re retorna uma string
# Para realizar operações matemáticas precisamos de tipos numéricos (int ou float)
num1 = float(num1)
num2 = float(num2)

# Mensagem ao usuário
print("\n Calculando...\n")

# Realizando as operações
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div = num1 / num2

# Printando os valores calculados
print(f"Você digitou os números {num1} e {num2}.\n"
f"\nA soma deles é {soma}.\n"
f"A subtração entre eles (na ordem informada) é {subt}.\n"
f"A multiplicação entre eles é {mult}.\n"
f"A divisão entre eles é {div}.\n")

#######################################################################################