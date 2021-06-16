#Comandos b�sicos
#Teste acento �����
print("Ol� mundo")

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

#Testes matem�ticos
x = 2
y = 3
z = 4

#Verificando se s�o iguais
print(x == y)

#Qualquer outro tipo de compara��o pode ser feito dentro do "print"
#Opera��es com AND, OR e NOT podem ser utilizados dentro do "print"
#Ex:

print(x == y or x == z and x == y)

#Exemplo o "if" e o else

if y > x:
    print(y, " � maior que ", x)
if y < z:
    print (z, " � maior que ", y)
if x > y:
    print("x � maior que y")
else:
    print("x � menor que y")

#Exemplo "elif"

x = 1
y = 2

if x == y:
    print("N�mero iguais")
elif y > x:
    print("y maior que x")
else:
    print("N�mero diferentes")

#Estruturas de repeti��o

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

#Imprimindo os primeiros itens da lista nas posi��es 
#passadas como par�metro

for i in range(10,20):
    print(i)

#Imprimindo a cada 2 elementos
for i in range(10,20, 2):
    print(i)

#Em python, tudo � Objeto ou seja � poss�vel utilizar 
#m�todos e atributos em cima de uma vari�vel

#Concatenando strings

a = "Vitor"
b = "Silva"

concatenar = a + " " + b
print(concatenar)

#Pegando o tamanho de uma string

tamanho = len(concatenar)
print(tamanho)

#Navegando pela posi��o da String
print(a[0])
print(a[2])
print(a[4])

#Imprimindo partes da string ou do primero �ndice passado at� o 
#segundo �ndice passado

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
#Exemplo remo��o de letra espec�fica
#minha_lista = minha_string.split("r")
print(minha_lista)

#Buscando uma substring
#Retorna o �ndice onde a palavra � encontrada
#Caso a string n�o seja encontrada � retornado "-1"
busca = minha_string.find("rei")
print(busca)

#Caso queira imprimir da palavra encontrada at� o final
print(minha_string[busca:])

#Substituindo palavras

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

#Para criar fun��es, utilizar a palavra reservada "def"
def soma (x, y):
    print(x + y)

soma(2,4)

#Outro exemplo
def multiplicacao(x, y):
    return x * y
print(multiplicacao(3, 4))