#Exercícios
#Exercício 1
#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 
idade = int(input("Qual a sua idade?"))

if idade < 18:
    print("Usuário menor de idade")
else:
    print("Usuário maior de idade")

#Exercício 2
#Faça um programa que receba duas notas digitadas pelo usuário. 
#Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
nota = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota + nota2)/2

if media >= 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

print(media)
#Exercício 3
#Escreva um programa que resolva uma equação de segundo grau.
import math
print("Equacao do 2° grau da forma: ax² + bx + c")
a = 0
raiz = 0
raiz1 = 0
raiz2 = 0
while a == 0:
    print("a não pode ser igual a 0")
    a = int(input("Coeficiente 'a'"))

b = int(input("Coeficiente 'b'"))
c = int(input("Coeficiente 'c'"))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Delta possui uma raíz imaginária")
elif delta == 0:
    raiz = -b / (2 * a)
    print("Delta = 0, e raiz = " + raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta))/ (2 * a)

print(raiz1)
print(raiz2)

#Exercício 4
#Escreva um programa que ordene uma lista numérica com três elementos.
lista = [6,2,4]
lista.sort()
print(lista)

#Exercício 5
#Escreva um programa que receba dois números e um sinal, 
#e faça a operação matemática definida pelo sinal.   
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
        print("Sinal inválido")
switch()

