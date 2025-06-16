# # 1. Haz un programa que convierta dos listas en un diccionario.

# lista1 = ["blanco", "rojo", "negro", "naranja", "amarillo"]
# lista2 = [1, 2, 3, 4, 5] 
# dic = {}
# for a in range(0, len(lista1)):
#     dic[lista1[a]] = lista2[a]
# print( dic)
# print("----------------------")


# # 2. Haz un programa que fusione dos diccionarios de Python en uno solo.

# dic1 = {"blanco": 1, "rojo": 2, "negro": 3}
# dic2 = {"a": 4, "b": 5, "c": 6} 
# dic_all = {}
# for clave, valor in dic1.items():
#     dic_all[clave] = valor
# for clave, valor in dic2.items():
#     dic_all[clave] = valor
# print(dic_all)
# print("----------------------")


# # 3. Haz un programa que imprima el valor de la clave 'history' del siguiente diccionario.

# dic = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(dic['class']['student']['marks']['history'])
# print("----------------------")


# # 4. Haz un programa que inicialice el diccionario con valores por defecto.
# nombre = ["juan", "pedro"]
# a = {"nivel": 0, "clase": "principiante"}
# x = dict.fromkeys(nombre, a)
# print(x)
# print("----------------------")

# # 5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.

# dic = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# clave = ["name", "age"]
# a = dict()
# for x in clave:
#     a.update({x: dic[x]})    
# print(a)
# print("----------------------")


# # 6. Haz un programa que elimine una lista de claves de un diccionario.

# dic = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# clave = ["name", "age"] # las q quiero eliminar
# for x in clave:
#     dic.pop(x)
# print(dic)
# print("----------------------")

# # 7. Haz un programa que compruebe si un valor existe en un diccionario.
# dic = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# print(dic)
# a = input("escribe que valor quieres buscar en el diccionario: ")
# if a in dic.values():
#     print(f"sip! el valor {a} está presente en el diccionario.")
# else:
#     print("Nop! el valor indicado no está presente en el diccionario.")
# print("----------------------")


# # 8. Haz un programa que cambie el nombre de la clave de un diccionario.

# dic = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# print(dic)
# dic["edad"] = dic.pop("age")
# print(dic)
# print("----------------------")

# # 9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.
# dic = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75}
# print(min(dic, key=dic.get))
# print("----------------------")


# # 10. Haz un programa que cambie el valor de una clave en un diccionario anidado.

# dic = {
#     "player1": {"nombre": "jose", "edad": 19, "job": "dps"},
#     "player2": {"nombre": "juan", "edad": 23, "job": "tank"},
#     "player3": {"nombre": "Maria", "edad": 54, "job": "Healer"},
#     "player4": {"nombre": "Carlos", "edad": 32, "job": "support"}
# }
# print(f"este es el diccionario antes del cambio: {dic}")
# dic["player2"]["edad"] = 34
# print(dic)
# print("----------------------")







def holi(nombre):
    saludar = print(f"saludos {nombre}")

holi("koni")