#introduccion a python
"""
Esto es un comentario
de muchas lineas
"""

print("Hola mundo")

print("Ejemplo: ")
x = 5
y = "Jhon"
print(x, y)

print(type(x))
print(type(y))

a = 4
A = "sally"
# A no sobreescribira a

x, y ,z = "Hola", "Como", "estas"

print(x)
print(y)
print(z)

x = y = z = "Hola naranja"

print(x)
print(y)
print(z)

frutas = ["manzana", "platano", "cereza"]

x, y, z = frutas
print(x)
print(y)
print(z)

x = "python"
y = "es"
z = "asombroso"

print(x + " " + y + " " + z)

x = 1 #int
y = 2.81 # float
z = 1j # complejo

# convertir de int a float
a = float(x)
# convertir de float a int
b = int(y)
# convertir de int a complejo
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
# importar al modulo random y mostrar un numero aleatorio del 1 al 10
n = random.randrange(1, 10)
print(n)

while n < 5:
    n = n + 1
    print("hola mundo")

for i in (0,1,2,3,4,5,6,7,8,9,10):
    print(i, end=" ")

print("\n")
for i in range(10):
    print(i, end=" ")

print("\n")
for i in range(0, 10):
    print(i, end=" ")

print("\n")
for i in range(-1, 10):
    print(i, end=" ")

print("\n")
# con incremento de 2
for i in range(0,10,2):
    print(i, end=" ")

print("\n")

x = input("Captura un numero: ")
num = int(x)
if num > 0:
    print("Es positivo")
else:
    print("Es negativo")

x = 5
y = 6

if x < y:
    print("X es menor que y")
elif x > y:
    print("X es mayor que y")
else:
    print("X y Y son iguales")