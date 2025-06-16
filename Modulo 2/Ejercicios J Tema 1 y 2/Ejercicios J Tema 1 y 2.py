
#Hola, esto son los ejercicios del tema 1 y 2 de JoseManuel Gonzalez para el curso de Python de la escuela Musk.

# 1. Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!”.

print ("Hello everynyan")


# 2. Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.

a = "Buenas tardes"
b = "Mi nombre es Jose"
c = "que tenga buena tarde"

print (c, b, a)


# 3. Haz un programa que declare dos números y que escriba la suma.
a = 115
b = 234

print (a + b)


# 4. Haz un programa que declare dos números y que escriba el máximo.
a = 13
b = 78

print (max (a, b))


# 5. Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.
a = 13
b = 23
c = 69

print (max (a, b, c))


# 6. Hacer un programa que dado un valor calcule su cuadrado y el cubo. 
a = 13
cuadrado = pow (a, 2)
cubo = pow (a, 3)

print (cuadrado)
print (cubo)


# 7. Haz un programa que devuelva el valor absoluto de un número.
a = -13

print (abs(a))


# 8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d y el residuo r de a entre b.
# Recordad que, por definición, d y r tienen que ser los únicos enteros tales que 0 ≤ r < b y d · b + r = a. Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2
a = 15 
b = 6
division_entera = a // b
residuo = a % b

print (a, b, division_entera, residuo)
print (f"dividendo: {a}, divisor: {b}, division entera {division_entera}, residuo {residuo} ")

# 9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.
a = 3600 #segundos
minutos = a / 60
horas = minutos / 60

print (f"{a} minutos son {minutos}, y {horas} horas. ")

# 10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin. (F= 1.8C + 32 y  ºK =°C + 273ºK).
c = 40
f = 1.8 * c + 32
k = c + 273

print (f"Temperatura en Celsius: {c} ")
print (f"Temperatura en Fahrenheit: {f} ")
print (f"Temperatura en Kelvin: {k} ")

