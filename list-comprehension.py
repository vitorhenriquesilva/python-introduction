#List comprehension
x = [1, 2 ,3 ,4 ,5]
y = []
#Inserindo o � dos n�meros lista x na lista y
for i in x:
    y.append(i**2)
print(x)
print(y)
#O exemplo abaixo equivale a tod0 c�digo acima
a = [1, 2 ,3 ,4 ,5]
b = [i**2 for i in a]
print("Usando list comprehension")
print(a)
print(b)
#Outro exemplo com uma condi��o
f = [1, 2, 3, 4, 5]
g = [i**2 for i in f]
h = [i for i in f if i%2==1] #

print(h)