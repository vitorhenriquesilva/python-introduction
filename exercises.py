#Exerc�cios
#Exerc�cio 1
#Fa�a um programa que receba a idade do usu�rio e diga se ele � maior ou menor de idade. 
idade = int(input("Qual a sua idade?"))

if idade < 18:
    print("Usu�rio menor de idade")
else:
    print("Usu�rio maior de idade")

#Exerc�cio 2
#Fa�a um programa que receba duas notas digitadas pelo usu�rio. 
#Se a nota for maior ou igual a seis, escreva aprovado, sen�o escreva reprovado.   
nota = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota + nota2)/2

if media >= 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

print(media)
#Exerc�cio 3
#Escreva um programa que resolva uma equa��o de segundo grau.
import math
print("Equacao do 2� grau da forma: ax� + bx + c")
a = 0
raiz = 0
raiz1 = 0
raiz2 = 0
while a == 0:
    print("a n�o pode ser igual a 0")
    a = int(input("Coeficiente 'a'"))

b = int(input("Coeficiente 'b'"))
c = int(input("Coeficiente 'c'"))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Delta possui uma ra�z imagin�ria")
elif delta == 0:
    raiz = -b / (2 * a)
    print("Delta = 0, e raiz = " + raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta))/ (2 * a)

print(raiz1)
print(raiz2)

#Exerc�cio 4
#Escreva um programa que ordene uma lista num�rica com tr�s elementos.
lista = [6,2,4]
lista.sort()
print(lista)

#Exerc�cio 5
#Escreva um programa que receba dois n�meros e um sinal, 
#e fa�a a opera��o matem�tica definida pelo sinal.   
n1 = int(input("Primeiro numero"))
n2 = int(input("Segundo numero"))

def switch():
    sinal = input("Selecione um sinal: '-', '+', '*' ou '/'")

    if sinal == "-":
        print(n1 - n2)
    elif sinal == "+":
        print(n1 + n2)
    elif sinal == "*":
        print(n1 * n2)
    elif sinal == "/":
        print(n1 / n2)
    else:
        print("Sinal inv�lido")
switch()

