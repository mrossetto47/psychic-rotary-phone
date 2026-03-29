from universidade.pessoa import Pessoa

# Para utilizar o sistema de exceção e realizar algo útil com isso, utilizamos a estrutura seguinte

try: #Executa caso não ocorra nenhuma exceção (raise)

    # Aqui executamos o que o programa deve fazer se não houver exceção
   
    p1 = Pessoa("Maria", 11111111111) # CPF Válido
    p1.cpf = 123 # CPF Inválido (comentar para testar válido ou deixar para testar inválido)
    print(p1.nome)
    print(p1.cpf)

except Exception as e:# Se acontecer exceção (qualquer nesse caso) ele detecta, também chamado de "catch"
   
    # Usamos para fazer algo útil aqui, como informar o usuário ou logar o erro
    print(e) # Printa a exceção
