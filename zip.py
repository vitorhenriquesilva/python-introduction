#Fun��o .zip
#Essa fun��o � utilizada para a concatena��o de duas ou mais listas
lista1 = [1, 2, 3, 4 ,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00", "R$5,00", "N�o tem pre�o", "N�o tem pre�o", "N�o tem pre�o"]
for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)