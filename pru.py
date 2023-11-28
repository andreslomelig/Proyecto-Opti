import random

# Definir el rango de números deseados
rango_inferior = 1
rango_superior = 10

# Número de elementos deseados
num_elementos = 5

# Generar números aleatorios no repetitivos
numeros_unicos = set()

while len(numeros_unicos) < num_elementos:
    numero_aleatorio = random.uniform(rango_inferior, rango_superior)
    numeros_unicos.add(numero_aleatorio)

# Imprimir los números aleatorios no repetitivos
print(numeros_unicos)
