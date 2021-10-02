# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''


from typing import final


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_1 = int(input('Ingrese el primer número a operar\n'))
numero_2 = int(input('Ingrese el segundo numero a operar\n'))

while True:
    
    numero_3 = str(input("""Ingrese la operación a realizar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
- fin \n"""))

    if numero_3.upper() == "FIN":
        break 
    elif numero_3 == "+":
        print("########################################################")
        print("Usted eligio SUMA")
        print("El resultado de la suma es:", numero_1+numero_2)
        print("########################################################")
    elif numero_3 == "-":
        print("########################################################")
        print("Usted eligio RESTA")
        print("El resultado de la RESTA es:", numero_1 - numero_2) 
        print("########################################################")
    elif numero_3 == "*":
        print("########################################################")
        print("Usted eligio PRODUCTO")
        print("El resultado del preducto es:", numero_1 * numero_2)
        print("########################################################")
    elif numero_3 == "/":
        print("########################################################")
        print("Usted eligio DIVICIÓN")
        print("El resultado del preducto es:", numero_1 / numero_2)
        print("########################################################")
    elif numero_3 == "**":
        print("########################################################")
        print("Usted eligio POTENCIA")
        print("El resultado de potencia es:", numero_1 ** numero_2)
        print("########################################################")
    else:
        print("Ingrese un operador valido")
