#Listas pt. 1
#Criando e navegando pelas listas
minha_lista = [abacaxi, melancia, abacate]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = [abacaxi, 2, 9.89, True]
#Imprimindo o �ndice desejado
print(minha_lista[2])

#Pegando o tamanho da lista
tamanho = len(minha_lista)

#Imprimindo item por item da lista
for item in minha_lista
    print(item)

#Adicionando elementos a lista
minha_lista.append(limao)
print(minha_lista)

#Verificando se o item existe na minha lista
if 3 in minha_lista2
    print(3 esta na lista)
else
    print(N�o existe na lista)

#Removendos do indice 2 at� o final da lista
del minha_lista[2]
print(minha_lista)

#Adicionando item a uma lista vazia
minha_lista_4 = []
minha_lista_4.append(57)
print(minha_lista_4)

#Listas pt. 2
lista = [124,345,5,72,46,6,7,3,1,7,0]
#O m�todo sort retorna a pr�pria lista ordenada
lista.sort()

#Lista em ordem decrescente
lista.sort(reverse=True)

#J� o met�do sorted requer que uma nova lista receba a lista anterior
#lista = sorted(lista)
print(lista)

#Invertendo a lista
lista.reverse()