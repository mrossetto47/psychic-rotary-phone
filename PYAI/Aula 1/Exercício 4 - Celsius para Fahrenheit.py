"""EX. 4: Conversor de Temperatura
Conceitos: Operações matemáticas, formatação de strings
# Converta Celsius para Fahrenheit: (C × 9/5) + 32
# Peça a temperatura em Celsius e mostre em Fahrenheit"""

# Mensagem inicial ao usuario
print("Olá! Este programa irá converter uma temperatura de Celsius para Fahrenheit.\n"
        "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Recebendo a temperatura em Celsius do usuário
celsius = float(input("\nPor favor, digite a temperatura em Celsius que deseja converter para Fahrenheit:\n"))

# Aplicando a fórmula para conversão
fahrenheit = (celsius * 9/5) + 32

# Printando para o usuário
print(f"\nA temperatura de {celsius}° Celsius equivale a {fahrenheit}° Fahrenheit.")

###############################################################################################