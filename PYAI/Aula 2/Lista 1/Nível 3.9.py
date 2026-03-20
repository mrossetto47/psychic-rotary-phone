"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 3 - AVANÇADO
------------------

9. ANÁLISE DE VENDAS
   Uma loja registra suas vendas diárias em uma lista. Cada venda é representada por uma 
   sublista contendo [nome_produto, quantidade, preco_unitario]. 
   Crie um programa que:
   - Calcule o faturamento total
   - Encontre o produto mais vendido (em quantidade)
   - Crie uma lista apenas com os produtos que tiveram faturamento acima de R$100,00
   - Mostre a média de preço dos produtos vendidos
   """

# Mensagem de boas-vindas ao usuário
print("======================================================================\n" 
"Olá! Bem vindo ao programa de análise de vendas.\n"
"======================================================================" 
"\nEste programa irá analisar as vendas diárias de uma loja, que serão inseridas por você.\n"
"Você pode inserir quantas vendas quiser. Para finalizar a inserção, basta digitar 'fim'.\n"
"\nPressione Enter para continuar..." )
input()  # Espera o usuário pressionar Enter

#Criando lista para armazenar dados de entrada
produto_input=[]

#Criando lista de produtos 
lista_prod=[]

#Criando as variáveis necessárias
item=str()
qtde=int()
preco_unit=float()

#Loop para leitura de produtos do usuário
while True:
    item=input("\nDigite o nome do item ou 'fim' para terminar: ")
    # Verificando se o usuario digitou o 'item' como 'fim'
    if item!="fim":
        qtde=input("\nAgora, digite a quantidade deste item vendida: ")
        preco_unit=input("\nDigite agora o preço unitário em reais (utilize ponto como separador decimal): ")
        produto_input.append(item)
        produto_input.append(qtde)
        produto_input.append(preco_unit)
        lista_prod.append(produto_input)
        produto_input.clear
    else: break
print(lista_prod)