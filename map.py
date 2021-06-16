#Função Map
#Tetando pegar o valor dobrado de cada item da lista
def dobro(x):
    return x * 2

valor = [1, 2, 3, 4, 5]
print(dobro(valor))

#Pegando o valor dobrado de cada item da lista de uma forma ineficiente
#map recebe parâmetros da sua função e a sua lista
valor_dobrado = map(dobro, valor)
for v in valor_dobrado:
    print(v)

#Pegando o valor dobrado de cada item da lista de forma eficiente
valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)