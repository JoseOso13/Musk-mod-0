# Estos son los ejercicios del modulo 3 para la escuela Musk.

# 1) Se ha definido una clase relativa al inventario de un jet imaginario. Tambien se ha creado una instancia de esta clase Jet.
# Imprime el primer atributo de la instancia.

class Jet:
    def __init__(self, name:str, country:str):
        self.name = name
        self.origin = country


first_item = Jet("F16", "USA")

print(first_item.name)
print("....................")


#2) Usando la clase Jet, crea nuevas instancias con los siguientes nombres y orígenes:
# SU33: Russia
# AJS37: Sweden
# Mirage2000: France
# F14:USA
# Mig29: USSR
# A10: USA

class Jet:
    def __init__(self, name:str, country:str):
        self.name = name
        self.origin = country

jet_1 = Jet("SU33", "Russia")
jet_2 = Jet("AJS37", "Sweden")
jet_3 = Jet("Mirage2000", "France")
jet_4 = Jet("F14", "USA")
jet_5 = Jet("Mig29", "USSR")
jet_6 = Jet("A10", "USA")
print("....................")


# 3) Añade otro atributo llamado "cantidad" a la clase. 
# El usuario le dará valor pasando un nuevo parametro por el constructor.
# A continuacion, crea 2 instancias para: F14 y Mirage2000 con las cantidades 87 y 35.

class Jet:
    def __init__(self, name:str, country:str, cantidad:int):
        self.name = name
        self.origin = country
        self.cantidad = cantidad

jet_1 = Jet("SU33", "Russia", 13)
jet_2 = Jet("AJS37", "Sweden", 27)
jet_3 = Jet("Mirage2000", "France", 35)
jet_4 = Jet("F14", "USA", 87)
jet_5 = Jet("Mig29", "USSR", 16)
jet_6 = Jet("A10", "USA", 69)

print(jet_1.name, jet_1.origin, jet_1.cantidad)
print(jet_2.name, jet_2.origin, jet_2.cantidad)
print(jet_3.name, jet_3.origin, jet_3.cantidad)
print(jet_4.name, jet_4.origin, jet_4.cantidad)
print(jet_5.name, jet_5.origin, jet_5.cantidad)
print(jet_6.name, jet_6.origin, jet_6.cantidad)
print("....................")



# 4) Dada la siguiente instancia y sus atributos, crea una clase que la instancie.

# np2005 = Nobel("Peace", 2005, "Myhamad Tunus")
# print(np2005.category,np2005.year, np2005.winner)

class Nobel:
    def __init__(self, category:str, year:int, winner:str):
        self.category = category
        self.year = year
        self.winner = winner
np2005 = Nobel("Peace", 2005, "Myhamad Tunus")

print(np2005.category,np2005.year, np2005.winner)
print("....................")


# 5) Crea una clase con el nombre de Estudiante, e incicialice atributos como el nombre, la edad y el grado mientras crea un objeto.

class Estudiante:
    def __init__(self, nombre:str, edad:int, grado:int):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

Pedro = Estudiante("Pedro", 15, 5)
print(Pedro.edad, Pedro.grado, Pedro.nombre)
print("....................")



# 6) Escribe un programa para crear una clase vacia valida con el nombre de Estudiante, sin propiedades.

class Estudiante:
    pass

Pedro = Estudiante()

print(type(Pedro))
print("....................")



# 7) Añade un metodo publico en la clase Estudiante que calcule la media de una lista de notas y actualice el valor del atributo grade.
# A continuacion llama a la funcion en tu programa principal e imprime el valor de grade.

class Estudiante:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
        self.grade = 0
    def media(self, notas:int):
        if len(notas) > 0:
            self.grade = sum(notas) / len(notas)
        else:
            self.grade = 0
alumno1 = Estudiante("Antonio Gonzalez", 13)
notasA1 = [8,7,9,10]

alumno1.media(notasA1)
print(alumno1.nombre, alumno1.edad, "sus notas son: ", notasA1, "Y su media es: ", alumno1.grade)
print("....................")


# 8) Añade a la clase anterior, un metodo estatico que dada una lista de notas,
# y sus asignaturas asociadas, como diccionario,
# imprima aquellas asignaturas que han recibido una nota inferior a 5.

class Estudiante:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
        self.grade = 0
    def media(self, notas:int):
        if len(notas) > 0:
            self.grade = sum(notas) / len(notas)
        else:
            self.grade = 0

    @staticmethod
    def suspensas(diccionario_notas):
        print("Asignaturas con nota inferior a 5: ")
        for asignatura, nota in diccionario_notas.items():
            if nota < 5:
                print(f"- {asignatura}: {nota}")

alumno1 = Estudiante("Antonio Gonzalez", 13)
notasA1 = {
    "Matematicas": 7,
    "Historia": 4,
    "Fisica": 6,
    "Lengua": 3,
    "Quimica": 5
}
alumno1.media(list(notasA1.values()))
print(f"Media general: {alumno1.grade}")
Estudiante.suspensas(notasA1)
print("....................")



#9) Añade un atributo de clase llamado escuela a la clase Estudiante y dale unb valor predeterminado.
#A continuacion, añade un metodo de clase que dado el nombre de otra escuela
#actualice el valor de ese atributo.
#llama a tu metodo en el programa principal y asegurate de que funciona.

class Estudiante:
    escuela = "Instituto Principal"
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
        self.grade = 0
    def media(self, notas:int):
        if len(notas) > 0:
            self.grade = sum(notas) / len(notas)
        else:
            self.grade = 0

    @staticmethod
    def suspensas(diccionario_notas):
        print("Asignaturas con nota inferior a 5: ")
        for asignatura, nota in diccionario_notas.items():
            if nota < 5:
                print(f"- {asignatura}: {nota}")
    @classmethod
    def actualizar_escuela(cls, nuevo_nombre):
        cls.escuela = nuevo_nombre

alumno1 = Estudiante("Antonio Gonzalez", 13)

print("Escuela origen:", Estudiante.escuela)
Estudiante.actualizar_escuela("Colegio BellasArtes")
print("escuela actual:", Estudiante.escuela)
print("....................")



#10) Añade un metodo privado en la clase anterior, 
# que dado un diccionario mes.numero de asistancias, 
# devuelva 1 si algun mes tiene una asistencia <4,
# devuelva 2 si algun mes tiene alguna asistencia entre [4, 8]
# o devuelva 3 en caso contrario.
# para probar el metodo privado, encapsulalo con una funcion publica que devuelva su resultado.

class Estudiante:
    escuela = "Instituto Principal"
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
        self.grade = 0
    def media(self, notas:int):
        if len(notas) > 0:
            self.grade = sum(notas) / len(notas)
        else:
            self.grade = 0
    @staticmethod
    def suspensas(diccionario_notas):
        print("Asignaturas con nota inferior a 5: ")
        for asignatura, nota in diccionario_notas.items():
            if nota < 5:
                print(f"- {asignatura}: {nota}")    
    @classmethod
    def actualizar_escuela(cls, nuevo_nombre):
        cls.escuela = nuevo_nombre

    def __asistencia(self, asistencias):
        for asistencia in asistencias.values():
            if asistencia < 4:
                return 1
        for asistencia in asistencias.values():
            if 4 <= asistencia <=8:
                return 2
        return 3
    def resultado_asistencia(self, asistencias):
        return self.__asistencia(asistencias)

alumno1 = Estudiante("Antonio Gonzalez", 13)
asistencia_meses = {
    "Enero": 6,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 10,
    "Mayo": 20
}
resultado = alumno1.resultado_asistencia(asistencia_meses)
print("Resultado de evalucacion de asistencia: ", resultado)
print("....................")

