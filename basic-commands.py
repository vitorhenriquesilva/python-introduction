#Comandos básicos
#Teste acento ááááâ
print("Olá mundo")

#Outros testes
#Para elevar um numero ao quadrado, utilizar **
#Para que o python leia acentos, utilizar -*- coding: uft-8 -*-
var1 = 1
var2 = 1.1
var3 = "Uma string qualquer"
var4 = True
var5 = False

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)

#Testes matemáticos
x = 2
y = 3
z = 4

#Verificando se são iguais
print(x == y)

#Qualquer outro tipo de comparação pode ser feito dentro do "print"
#Operações com AND, OR e NOT podem ser utilizados dentro do "print"
#Ex:

print(x == y or x == z and x == y)

#Exemplo o "if" e o else

if y > x:
    print(y, " é maior que ", x)
if y < z:
    print (z, " é maior que ", y)
if x > y:
    print("x é maior que y")
else:
    print("x é menor que y")

#Exemplo "elif"

x = 1
y = 2

if x == y:
    print("Número iguais")
elif y > x:
    print("y maior que x")
else:
    print("Número diferentes")

#Estruturas de repetição

x = 1

while x < 10:
    print(x)
    x = x + 1
    #ou x += 1 que equivale a x++ em outras linguagens

#Listas

lista = [1,2,3,4,5]
lista2 = ["vitor", "henrique", "silva"]
lista3 = [1, "teste", 9.99, True]

#Percorrendo todos os itens da lista
for i in lista:
    print(i)

#Imprimindo os primeiros itens da lista nas posições 
#passadas como parâmetro

for i in range(10,20):
    print(i)

#Imprimindo a cada 2 elementos
for i in range(10,20, 2):
    print(i)

#Em python, tudo é Objeto ou seja é possível utilizar 
#métodos e atributos em cima de uma variável

#Concatenando strings

a = "Vitor"
b = "Silva"

concatenar = a + " " + b
print(concatenar)

#Pegando o tamanho de uma string

tamanho = len(concatenar)
print(tamanho)

#Navegando pela posição da String
print(a[0])
print(a[2])
print(a[4])

#Imprimindo partes da string ou do primero índice passado até o 
#segundo índice passado

print(concatenar[0:3])

#Utilizando lower case

print(concatenar.lower())

#Utilizando upper case

print(concatenar.upper())

#\n para quebra de linhas
#.strip() remove quebras de linhas

#Utilizando .split()

minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split(" ")
#Exemplo remoção de letra específica
#minha_lista = minha_string.split("r")
print(minha_lista)

#Buscando uma substring
#Retorna o índice onde a palavra é encontrada
#Caso a string não seja encontrada é retornado "-1"
busca = minha_string.find("rei")
print(busca)

#Caso queira imprimir da palavra encontrada até o final
print(minha_string[busca:])

#Substituindo palavras

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

#Para criar funções, utilizar a palavra reservada "def"
def soma (x, y):
    print(x + y)

soma(2,4)

#Outro exemplo
def multiplicacao(x, y):
    return x * y
print(multiplicacao(3, 4))