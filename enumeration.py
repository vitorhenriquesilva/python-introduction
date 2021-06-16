#Função enumerate
#Imprimindo uma lista com seus índices e valores de forma comum
lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])

#Utilizando a função enumerate
for i, nome in enumerate(lista):
    print(i, nome)