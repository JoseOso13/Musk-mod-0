# Hola, esto son los ejercicios del tema 3 de JoseManuel Gonzalez para el curso de Python de la escuela Musk.


# 1. Haz un programa que lea un número decimal por pantalla, lo convierta a entero y lo imprima.

a = float (input("Porfavor, indicame un numero decimal:  "))

print (int(a))


# 2. Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma línea.

a = float (input("porfavor, digame un numero decimal:  "))
print (f"tipo: {type (a)}, redondeado a {round (a)}" )


# 3. Haz un programa que lea dos números por pantalla e imprima su diferencia en valor absoluto.
a = float (input("porfavor indicame un numero: "))
b =  float (input("otro numero porfavor: "))
diferencia = abs(a - b)

print (f"la diferencia entre {a} y {b} es {diferencia}")
