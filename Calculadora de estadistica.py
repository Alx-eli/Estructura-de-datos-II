# Primero, pedimos al usuario que ingrese varios numeros
numeros_texto = input("Escribe tus numeros separados por un espacio: ")

# Separamos los numeros que el usuario escribio
numeros_separados = numeros_texto.split()

# Convertimos esos numeros de texto a numeros reales (decimales)
numeros = []
for num in numeros_separados:
    numeros.append(float(num))  # Convertimos el texto a numero y lo guardamos en la lista 'numeros'

# Ahora sumamos todos los numeros
suma = 0
for num in numeros:
    suma += num  # Vamos sumando cada numero en la variable 'suma'

# Luego, contamos cuantos numeros ingresaste
cantidad = len(numeros)

# Finalmente, calculamos el promedio como numero entero
if cantidad > 0:
    promedio = suma / cantidad
    promedio_redondeado = round(promedio)  # Redondeamos al numero entero más cercano
    print("El promedio es:", promedio_redondeado)
else:
    print("No ingresaste ningun numero.")
