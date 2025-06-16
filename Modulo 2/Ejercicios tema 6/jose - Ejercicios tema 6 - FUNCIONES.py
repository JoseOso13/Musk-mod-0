# 1. Haz un programa que cree una función en Python que dada una secuencia devuelva únicamente los números pares.

def secuencia_pares (secuencia):
    pares = []
    for x in secuencia:
        if x %2 == 0:
            pares.append(x)
    return pares

lista = [10,12,24,31,28,7,15, 16]
pares = secuencia_pares(lista)
print(pares)
print ("-------------------")


# 2. Haz un programa que cree una función con longitud variable de argumentos.

def funcion(*args):
    for x in args:
        print(x)
funcion(29,32,18)
print ("-------------------")


# 3. Haz un programa que devuelva múltiples valores desde una función.
# Crea la función calculation() de modo que pueda aceptar dos variables y calcular sumas y restas. 
Además, debe devolver tanto la suma como la resta en una sola llamada.

def calculation(num1:int, num2:int):
    suma = f"la suma es: {num1 + num2}"
    resta= f"su resta es: {num1 - num2}"
    return suma, resta
x = int(input("Por favor, escribe un numero: "))
x2 = int(input("Por favor, escribe otro numero: "))
solution = calculation(x,x2)
print(solution)
print ("-------------------")


# 4. Haz un programa que cree una función con un argumento por defecto.
# Crea una función show_employee() usando las siguientes condiciones.
# -Debe aceptar el nombre y el salario del empleado y mostrar ambos.
# -Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.

def show_employee(nombre:str, salario:int=9000):
    print(f"nombre: {nombre} y salario: {salario}.")
show_employee("antonio")
show_employee("maria", 5000)
print ("-------------------")


# 5. Haz un programa que cree una función interna para calcular la suma de la siguiente manera: 
# Crea una función externa que acepte dos parámetros, a y b. 
# Crea una función interna dentro de una función externa que calculará la suma de a y b. 
# Por último, una función externa que sumará 5 en la suma y la devolverá.

def funcion_ext (num1, num2):
    def funcion_int(num1, num2):
        return num1 + num2
    suma = funcion_int(num1, num2)
    return suma + 5

resultado = funcion_ext(10, 15)
print(f"El resultado de la función externa es: {resultado}")
print ("-------------------")


# 6. Haz un que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.

import math
def cuadrado_y_raiz(nums):
    c=[x**2 for x in nums]
    r= [math.sqrt(x) for x in nums]
    return c, r

nat = [10, 8, 17, 34, 12]
c, r = cuadrado_y_raiz (nat)
print(f"numeros originales:{nat}.")
print(f"los cuadrados son: {c}.")
print(f"las raices cuadrados son: {r}.")
print ("-------------------")


# 7. Haz un programa que cree una función que deje a, b y c ordenados de pequeño a grande. 
# Por ejemplo, si a =7, b = −3 y c = 1, los valores después de la llamada deben ser a =−3, b = 1 y c = 7.

a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))
c = int(input("Introduce el tercer numero: "))
def ordenar(a, b, c):
    lista = [a,b,c]
    lista.sort()
    return lista
result = ordenar(a,b,c)
print (f"ordenados son: {result}.")
print ("-------------------")