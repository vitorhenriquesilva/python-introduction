#Fun��o enumerate
#Imprimindo uma lista com seus �ndices e valores de forma comum
lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])

#Utilizando a fun��o enumerate
for i, nome in enumerate(lista):
    print(i, nome)