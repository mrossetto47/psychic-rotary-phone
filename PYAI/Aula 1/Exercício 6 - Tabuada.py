"""EX. 6: Tabuada
Conceitos: Loops "for", range
# Peça um número e mostre a tabuada dele (1 a 10)
# Exemplo:
# 5 x 1 = 5
# 5 x 2 = 10 ...
"""
# Mensagem inicial ao usuario
print("Olá! Este programa irá pedir um número de 1 a 9 e dar a tabuada dele.\n"
    "\nPressione Enter para continuar..." )
input()  # Espera o usuário pressionar Enter

# Solicitando o número ao usuário
while True:
    try:
        entrada = int(input("\nPor Favor digite um número de 1 a 9...\n"))
        if 1 <= entrada <= 9:
            break
        else:
            print ("\nNúmero digitado inválido.")
    except:
        print ("\nNúmero digitado inválido.")

# Printando uma mensagem:
print(f"\nA tabuada no numero {entrada} é:")

# Criando um loop para a tabuada
for indice in range (1,11):
    resultado = entrada * indice
    print(f"{entrada} x {indice} = {resultado}")