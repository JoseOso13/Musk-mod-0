# Ejercicios de python de JoseManuelGonzalezGil. Modulo 4

# 1) Crea una clase Staff con los atributos role, dept y salary.
# crea una clase profesor que herede de la clase anterior y que ademas tenga como atributos nombre y edad.
# haz que sea posible instanciar un profesor dandole valor a todos los atributos.
print("\nEjercicio 1:\n")
class staff: # clase Staff con los atributos role, dept y salary
    def __init__(self, role: str, dept: str, salary: float):
        self.role = role
        self.dept = dept
        self.salary = salary

# clase Profesor heredada +  nombre y edad
class profesor(staff):
    def __init__(self, role: str, dept: str, salary: float, nombre: str, edad: int):
        super().__init__(role, dept, salary)  
        self.nombre = nombre
        self.edad = edad

# ejemplo
profe1 = profesor("Docente", "TIC", 3000, "Anotnio Gonzalez", 43) # ojala cobrar eso algun dia jaja

# Imprime los atributos del profesor
print(f"Nombre: {profe1.nombre}")
print(f"Edad: {profe1.edad}")
print(f"Rol: {profe1.role}")
print(f"Departamento: {profe1.dept}")
print(f"Salario: {profe1.salary}€")  
print("\n....................")



# 2) Representa el diagrama del pdf de ejercicios con sus clases, atributos y mmetodos correspondientes.
# cada metodo display debe imprimir el nombre de la clase, atributos y valores de la instancia en ese momento.
# ejemplo: in displaymethodofParent1x=10
print("\nEjercicio 2:\n")
# clase Padre
class parent1:
    def __init__(self, x: int):
        self.x = x

    def display(self):
        print(f"In display method of Parent1 x={self.x}")

# clase padre 2
class parent2:
    def __init__(self, y: int):
        self.y = y

    def display(self):
        print(f"In display method of Parent2 y={self.y}")

# clase child heredada
class Child(parent1, parent2):
    def __init__(self, x: int, y: int, z: int):
        parent1.__init__(self, x)  
        parent2.__init__(self, y)  
        self.z = z

    def display(self):
        parent1.display(self)
        parent2.display(self)
        print(f"In display method of Child x={self.x}, y={self.y}, z={self.z}")

# ejemplo
child_instance = Child(15, 16, 31)
child_instance.display() 
print("\n....................")



# 3) Crea una clase Car que herede de Vehicle (del ejemplo del pdf) y que sobreeescriba los metodos 
# max_speed() y change_gear().
# instancia dos objetos de cada clase y comprueba que la salida de cada metodo es distinta.
print("\nEjercicio 3:\n")
# clase vehicle
class vehicle:
    def __init__(self, name: str, color: str, price: float):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print(f"Details: Name={self.name}, Color={self.color}, Price={self.price}")

    def max_speed(self):
        print("Vehicle max speed is 150 km/h")
    def change_gear(self):
        print("Vehicle can change up to 6 gears")

vehicle1 = vehicle("tractor", "rojo", 50000)
vehicle2 = vehicle("bus", "azul", 75000)

class car(vehicle): # clase car que hereda de Vehicle
    def max_speed(self):
        print("Car max speed is 200 km/h")
    def change_gear(self):
        print("Car can change up to 8 gears")

car1 = car("sedan", "Black", 30000)
car2 = car("bmw", "White", 45000)


print("vehicle 1:")
vehicle1.show()
vehicle1.max_speed()
vehicle1.change_gear()

print("\nvehicle 2:")
vehicle2.show()
vehicle2.max_speed()
vehicle2.change_gear()

print("\ncar 1:")
car1.show()
car1.max_speed()
car1.change_gear()

print("\ncar 2:")
car2.show()
car2.max_speed()
car2.change_gear()

print("\n....................")



# 4) Dadas las siguientes clases con el output de sus respectivos metodos (mirar pdf),
# crea una interfaz formal que las implemente.
print("\nEjercicio 4:\n")

from abc import ABC, abstractmethod
from zoneinfo import ZoneInfo

class Plantilla(ABC): #interfaz formal
    @abstractmethod
    def preprocess_data(self, data=None, y=None):
        pass
    @abstractmethod
    def fit(self):
        pass
    @abstractmethod
    def predict(self):
        pass

class SVM(Plantilla): #clase svm heredada
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")
    def fit(self):
        print("Training at SVM")
    def predict(self):
        print("Evaluating at SVM")

class DecisionTree(Plantilla): #clase DT heredada
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")
    def fit(self):
        print("Training at DecisionTree")
    def predict(self):
        print("Evaluating at DecisionTree")

# ejemplo
svm = SVM()
svm.preprocess_data()
svm.fit()
svm.predict()
print("\n")
dt = DecisionTree()
dt.preprocess_data()
dt.fit()
dt.predict()
print("\n....................")



#5) Repetir el ejercicio anterior creando una interfaz informal.
print("\nEjercicio 5:\n")

class Plantilla: # interfaz informal
    def preprocess_data(self, data=None, y=None):
        pass
    def fit(self):
        pass
    def predict(self):
        pass

class SVM(Plantilla):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")
    def fit(self):
        print("Training at SVM")
    def predict(self):
        print("Evaluating at SVM")

class DecisionTree(Plantilla):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")
    def fit(self):
        print("Training at DecisionTree")
    def predict(self):
        print("Evaluating at DecisionTree")

# ejemplo
svm = SVM()
svm.preprocess_data()
svm.fit()
svm.predict()

print("\n")

dt = DecisionTree()
dt.preprocess_data()
dt.fit()
dt.predict()
print("\n....................")



# 6) Crea una clase virtual llamada Algoritmo con los atributos nombre, tarea y aprendizaje,
# que sea superclase de la clase BaseClassifier del problema anterior
# Comprueba con el metodo issubclass que algoritmo es padre de BaseClassifier.
print("\nEjercicio 6:\n")

class Algoritmo(ABC): #clase virtual algoritmo
    def __init__(self, nombre: str, tarea: str, aprendizaje: str):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje

Algoritmo.register(Plantilla)

# ejemplo con instance
plantilla_instance = Plantilla()
plantilla_instance.preprocess_data()
plantilla_instance.fit()
plantilla_instance.predict()

# comprobación con issubclass
print("\n¿Es Plantilla una subclase de Algoritmo?")
print(issubclass(Plantilla, Algoritmo))  # True

# comprobación con isinstance
print("\n¿Es una instancia de Algoritmo?")
print(isinstance(plantilla_instance, Algoritmo))  # True
print("\n....................")



# 7) Escribe un script en python para mostrar distintos formatos de fecha y hora.
# a) fecha y hora actuales.
# b) año actual.
# c) mes del año. 
# d) numero de la semana del año.
# e) dia de la semana.
# f) dia del año.
# g) dia del mes.
# h) dia de la semana.
print("\nEjercicio 7:\n")

from datetime import datetime, timedelta, date

fecha_hora_actual = datetime.now() 

# a) fecha y hora 
print("a) fecha/hora actuales:", fecha_hora_actual)
# b) año actual
print("b) año actual:", fecha_hora_actual.year)
# c) mes del año
print("c) mes del año:", fecha_hora_actual.month)
# d) número de la semana del año
print("d) numero de la semana del año:", fecha_hora_actual.strftime("%W"))
# e) día de la semana
print("e) dia de la semana:", fecha_hora_actual.strftime("%A"))
# f) día del año
print("f) dia del año:", fecha_hora_actual.strftime("%j"))
# g) día del mes
print("g) dia del mes:", fecha_hora_actual.day)
# h) día de la semana (número, donde lunes es 0 y domingo es 6)
print("h) dia de la semana:", fecha_hora_actual.weekday())
# En este ejemplo utilizamos las actuales, si quisieramos usar fechas concretas utilizariamos fromisoformat.
print("\n....................")



# 8) Escribe un programa en Python para convertir una cadena a datetime.
print("\nEjercicio 8:\n")

fecha_cadena = "01-01-2014 02:43:00 PM"
fecha_datetime = datetime.strptime(fecha_cadena, "%d-%m-%Y %I:%M:%S %p")

print("cadena original:", fecha_cadena)
print("convertido a datetime:", fecha_datetime)
print("año:", fecha_datetime.year)
print("mes:", fecha_datetime.month)
print("dia:", fecha_datetime.day)
print("hoora:", fecha_datetime.hour)
print("minuto:", fecha_datetime.minute)
print("segundo:", fecha_datetime.second)
print("\n....................")



# 9) Escribe un programa en python para obtener la hora actual.
print("\nEjercicio 9:\n")

hora_actual = datetime.now().time()

print("Hora actual:", hora_actual)
print("\n....................")



# 10) Escribe un programa en python para restar cinco dias a la fecha actual.
print("\nEjercicio 10:\n")

fecha_requerida = datetime.now() - timedelta(days=5)

print(f"fecha actual: {datetime.now()}")
print(f"fecha actual - 5 dias: {fecha_requerida}")
print("\n....................")


#11) Escribe un programa en python para convertir una cadena de marcas de tiempo unix en una fecha legible.
print("\nEjercicio 11:\n")

timestamp_unix = "1284105682" #cadena unix

fecha_legible = datetime.fromtimestamp(int(timestamp_unix))

print("INPUT Unix timestamp string:", timestamp_unix)
print("OUTPUT:", fecha_legible.strftime("%Y-%m-%d %H:%M:%S"))
print("\n....................")



#12) Escribe un programa en puthon para sumar 5 segundos con la hora actual.
print("\nEjercicio 12:\n")

hora_act = datetime.now()
hora_mas_5_segundos = hora_act + timedelta(seconds=5)

print("Hora actual:", hora_act.strftime("%Y-%m-%d %H:%M:%S %p"))
print("Hora actual + 5 segundos:", hora_mas_5_segundos.strftime("%Y-%m-%d %H:%M:%S %p"))
print("\n....................")



#13) Escribe un programa en python para selecciionar todos los domingos de un año determinado.
print("\nEjercicio 13:\n")

def obtener_domingos(year):
    fecha = date(year, 1, 1)
    while fecha.weekday() != 6: # 6 es domingo
        fecha += timedelta(days=1)

    domingos = []
    while fecha.year == year:
        domingos.append(fecha)
        fecha += timedelta(days=7)
    return domingos

año_pregunta = int(input("porfavor, indicame un año:  "))
año_determinado = año_pregunta
domingos = obtener_domingos(año_determinado)
print(f"todos los domingos del año {año_determinado}:") 
for domingo in domingos:
    print(domingo.strftime("%Y-%m-%d"))
print("\n....................")



#14) Escribe un programa en python para contar el numero de lunes desde el primer dia
# del mes desde 2015 hasta 2016.
print("\nEjercicio 14:\n")

año_inicio = 2015
año_fin = 2016

def contar_lunes(año_inicio, año_fin):
    contador_lunes = 0
    lunes_mes = [] #lista para lunes en fechas
    
    for año in range(año_inicio, año_fin + 1):  # itera por año
        for mes in range(1, 13):  # iterar por  mes
            primer_dia_mes = date(año, mes, 1)  # Primer día del mes
            if primer_dia_mes.weekday() == 0:  # 0 es lunes
                contador_lunes += 1
                lunes_mes.append(primer_dia_mes)  # guarda la fecha

    return contador_lunes, lunes_mes

lunes_tot, lunes_fechas = contar_lunes(año_inicio, año_fin)

print(f"los lunes del primer día del mes entre {año_inicio} y {año_fin} son: {lunes_tot}")
print("fechas especificas:")
for fecha in lunes_fechas:
    print(fecha.strftime("%Y-%m-%d")) 
print("\n....................")



 #15) Escribe un programa en python para crear 12 fechas fijas a partir de 
# una fecha especificada en un periodo determinado.
# la diferencia entre dos fechas sera de 20.
print("\nEjercicio 15:\n")

def generar_fechas_iniciales(fecha_inicial, intervalo_dias, cantidad_fechas): # Función para generar 12 fechas fijas
    fechas = []
    for days in range(cantidad_fechas):
        fechas.append(fecha_inicial + timedelta(days=days * intervalo_dias))
    return fechas

fecha_inicial = datetime.strptime("2025-01-01", "%Y-%m-%d")  # cambia esta fecha si quieres

intervalo_dias = 20  # difeerencia entre fechas
cantidad_fechas = 12  # numero de fechas a generar

fechas_generadas = generar_fechas_iniciales(fecha_inicial, intervalo_dias, cantidad_fechas)

print(f"fechas generadas a partir de {fecha_inicial.strftime('%Y-%m-%d')} con un intervalo de {intervalo_dias} dias:")
for fecha in fechas_generadas:
    print(fecha.strftime("%Y-%m-%d"))
print("\n....................")



# 16) implementa una funcion generadora que dadas dos listas del mismo tamaño,
# devuelva la multiplicacion entre los elementos de cada una,
# el primer elemento de la lista 1 por el  primero de la lista 2,
# el segundo con el segundo y asi sucesivamente.
# sigue la estructura del pdf (pag 18)
# añadiendo el bloque except capturamos la excepcion de Stop Iteration que se produce al acabar de ller los elementos.
print("\nEjercicio 16:\n")

def listas_ex_16(l1, l2):
    try:
        for a, b in zip(l1, l2): #zip es paara iterar las 2 a la vez.
            yield a * b  
    except StopIteration:
        pass  

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

resultado = listas_ex_16(lista1, lista2)

print("resultados de la multiplicacion:")
for valor in resultado:
    print(valor)
# Si las listas no tienen el mismo tamaño, zip detendrá la iteración cuando alcance el final de la lista más corta.
# Esto asegura que no se produzcan errores por intentar acceder a índices fuera de rango.
print("\n....................")



# 17) implementa un generador, que dado un entero n, genere n numeros aleatorios.
# puedes usar el metodo random de la libreria random para generar numeros aleatorios.
print("\nEjercicio 17:\n")
import random

def generador_aleatorios(n):
    for x in range(n):
        yield random.randint(1, 100)  # generara un numero aleatorio entre 1 y 100

# ejemplo
n = int(input("introduce la cantidad de numeros aleatorios a generar: "))
print(f"generando {n} numeros aleatorios:")

for numero in generador_aleatorios(n):
    print(numero)
print("\n....................")



# 18) implementa un generador de fibonacci que genere n numeros de la secuencia de fibonacci, que tiene la forma: 
# 0,1,1,2,3,5,8,13,...
# cuyos dos primeros valores son 0 y 1 por definicion y el resto se calculan sumando los dos ultimos valores.
print("\nEjercicio 18:\n")

def fibonacci(n):
    a, b = 0, 1  # los dos primeros valores de secuencia
    for x in range(n):
        yield a  
        a, b = b, a + b  # calcula el siguiente valor de la secuencia

# ejemplo
n = int(input("introduce cuantos numeros de Fibonacci a generar: "))
print(f"generando {n} numeros de la secuencia de Fibonacci:")

for numero in fibonacci(n):
    print(numero)
print("\n....................")



# 19) Implemente un generador, que dado un entero n, imprima todos los numeros inferiores a n multiplicados por 2.
print("\nEjercicio 19:\n")

def generador_multi(n):
    for x in range(n):
        yield x * 2  # multiplica los número por 2

# ejempl
n = int(input("introduce un numero entero: "))
print(f"generando numeros inferiores a {n} multiplicados por 2:")

for numero in generador_multi(n):
    print(numero)
print("\n....................")



# 20) implementa un generador, que dado un entero n, genera n numero de impares.
print("\nEjercicio 20:\n")

def gen_impares(n): #generador de impares.
    numero = 1  
    for x in range(n):
        yield numero  
        numero += 2  
# ejemplo
n = int(input("introduce cuantos nnmeros impares a generar: "))
print(f"generando {n} numeros impares:")

for numero in gen_impares(n):
    print(numero)
print("\n....................")



# 21) crea una funcion que genere una excepcion e imprima su tipo,
# los argumentos de la excepcion y su mensaje de error.
print("\nEjercicio 21:\n")

def gen_excepcion():
    try:
        resultado = 10/0 # generar una excepción
    except Exception as e:
        print(f"Tipo de excepción: {type(e).__name__}") #tipo
        print(f"Argumentos de la excepción: {e.args}") #argumento
        print(f"Mensaje de error: {str(e)}") #mensaje

gen_excepcion()
print("\n....................")



# 22) crea una funcion que compute la diferencia entre 2 enteros.
# en caso de que la diferencia sea negativa genera una excepcion inventada por ti que informe de ello.
# por ejemplo, la excepcion poria llamarse "NegativeDifferenceException"
print("\nEjercicio 22:\n")

def calcular_dif(a, b): # Función que calcula la diferencia 
    try:
        diferencia = a - b
        if diferencia < 0:
            raise NegativeDifferenceException(f"Diferencia negativa: {diferencia}")
        return diferencia
    except NegativeDifferenceException as e:
        print(f"Excepción capturada: {type(e).__name__}")
        print(f"Mensaje: {e}")
        return None
    
class NegativeDifferenceException(Exception): # excepcion personalizada
    def __init__(self, message="la diferencia es negativa"):
        self.message = message
        super().__init__(self.message)
# ejemplo
num1 = int(input("introduce el primer numero: "))
num2 = int(input("introduce el segundo numero: "))

resultado = calcular_dif(num1, num2)
if resultado is not None:
    print(f"la diferencia entre {num1} y {num2} es: {resultado}")
print("\n....................")



# 23) crea una funcion que calcule la division entre dos numeros.
# debe imprimir el mensaje "los parametros deben ser numeros enteros" cuando se genera una excepcion
# de tipo y "El divisor no puede ser 0" cuando se genera un ZeroDivisionError.
print("\nEjercicio 23:\n")

def calcular_division(a, b): #funcion calculadora
    try:
        resultado = a / b
        return resultado
    except TypeError:
        print("los parámetros deben ser números enteros") #en caso de q no sean enteros.
    except ZeroDivisionError:
        print("el divisor no puede ser 0") #en caso de q sea cero.
    finally:
        print("ejecucion de la función calcular_division finalizada.") #ejercicio 24.

# ejemplo
try:
    num1 = int(input("introduce el primer numero: "))
    num2 = int(input("introduce el segundo numero: "))
    resultado = calcular_division(num1, num2)
    if resultado is not None:
        print(f"el resultado de la division es: {resultado}")
except ValueError:
    print("porfavor, introduce valores validos.")
print("\n....................")



# 24) añade a la funcion anterior, un mensaje que se imprima al final de la ejecicion de la function
# independientemente de si se ha generado excepcion o no.
print("\nEjercicio 24:\n")  
print("\nHECHO\n") 


print("\n....................")
print("\nFIN DE LOS EJERCICIOS.\n")