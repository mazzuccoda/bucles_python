# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0
cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

for x in notas:
    if x > 0: 
        sumatoria += x
        cantidad_notas += 1
    else:
        cantidad_ausentes += 1
# Terminado el bucle calcule el promedio como
promedio = sumatoria / cantidad_notas

for y in range(len(notas)):
    if notas[y] >= 90: 
        notas[y] = "A"
    elif notas[y] >= 80 and notas[y] < 90:
        notas[y] = "B"
    elif notas[y] >= 70 and notas[y] < 80:
        notas[y] = "C"
    elif notas[y] >= 60 and notas[y] < 70:
        notas[y] = "D"
    elif notas[y] < 60 and notas[y] >= 0:
        notas[y] = "F"
    else:
        notas[y] = "Ausente"

nota_final = None

if promedio >= 90: 
    nota_final = "A"
elif promedio >= 80 and promedio < 90:
    nota_final = "B"
elif promedio >= 70 and promedio < 80:
    nota_final = "C"
elif promedio >= 60 and promedio < 70:
    nota_final = "D"
elif promedio < 60 and promedio >= 0:
    nota_final = "F"


print(notas)
print("La cantidad de ausentes es:", cantidad_ausentes)
print("El promedio de las notas es", promedio)
print("El resultado final de la clase es:", nota_final)

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

# Imprima en pantalla al cantidad de ausentes
