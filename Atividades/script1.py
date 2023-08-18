print(".")
#    Complete o código do exemplo abordado nos slides, desenvolvendo as opções Editar e Sair;
#   Desenvolva três exemplos de códigos em Python (.py), demonstrando diferentes tipos de funções. Crie uma função sem parâmetros e sem retorno, outra função com parâmetros e sem retorno, e uma terceira função com parâmetros e retorno. Seja criativo e explore a versatilidade das funções em Python. Certifique-se de fornecer comentários explicativos em seu código para facilitar a compreensão;


#01
def msg():
    print("(01) Função simples")

msg()
print('//////////////////////////////////////////////////////////////')
#//////////////////////////////////////////////////////////////////////////

#02
def number(numero):
    if numero % 2 == 0:
        print(f"(02) O número {numero} é par.")
    else:
        print(f"(02) O número {numero} é ímpar.")

number(10)
number(7)
print('//////////////////////////////////////////////////////////////')
#//////////////////////////////////////////////////////////////////////////
#03
def calcularTotal(precoUnitario, quantidade):
    total = precoUnitario * quantidade
    return total

preco = 10
quantidade = 7

valorTotal = calcularTotal(preco, quantidade)
print(f"(03) O valor total a ser pago é: R$ {valorTotal:.2f}")
print('//////////////////////////////////////////////////////////////')
#//////////////////////////////////////////////////////////////////////////