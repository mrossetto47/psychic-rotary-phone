#######################################
######     Calculador de IMC    #######
#######################################

# Saudação e explicação do programa
print("Bem-vindo ao Calculador de IMC!")
print("Este programa calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos pelo usuário.")

# Solicitar ao usuário que insira seu peso em kg
peso = float(input("Por favor, insira seu peso em kg (utilize ponto decimal): "))

# Fazer checagem para garantir que o peso seja um número float válido
while True:
    try:
        # Peso deve ser um número positivo e maior que zero, mas deve ter um limite superior razoável para evitar entradas inválidas
        if peso <= 0 or peso > 500:
            print("Por favor, insira um peso válido (maior que 0 e menor ou igual a 500 kg).")
            peso = float(input("Por favor, insira seu peso em kg (utilize ponto decimal): "))
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para o peso.")
        peso = float(input("Por favor, insira seu peso em kg (utilize ponto decimal): "))
print(f"Peso registrado: {peso} kg")
