# Ejercicios del modulo 5 de Python (escuela MUSK) de JoseManuel Gonzalez Gil.

# 1) Escribe una funcion en python para leer el contenido de un archivo de texto "poema.txt" 
# linea por linea y mostrar el resultado en pantalla.
print("\nEjercicio 1:\n")
def leer_poema():
    try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.rstrip())  
    except FileNotFoundError:
        print("el archivo 'poema.txt' no existe.")

leer_poema()
print("\n....................")



# 2) Escribe una funcion para contar el numero de lineas de un archivo de texto "historia.txt":
# Ejemplo: Si el archivo "story.txt" contiene las siguientes lineas:
# Un niño esta jugando alli.
# hay un parque infantiil.
# Un avion esta en el cielo
# El cielo es rosa
# La contraseña puede contener letras y numeros
# el resultado debe ser 5.
print("\nEjercicio 2:\n")
def contar_lineas():
    try:
        with open("historia.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            print(f"el número de líneas es: {len(lineas)}")
    except FileNotFoundError:
        print("el archivo 'historia.txt' no existe.")

contar_lineas()
print("\n....................")



#3) Escribe una funcion en python para contar y mostrar el numero total de palabras en un archivo de texto.
print("\nEjercicio 3:\n")
def contar_palabras(nombre_archivo): 
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            print(f"el número total de palabras es: {len(palabras)}")
    except FileNotFoundError:
        print(f"el archivo '{nombre_archivo}' no existe.")


contar_palabras("historia.txt") #debes escribir el nombre del archivo que quieres contar.
print("\n....................")



# 4) Escribe una funcion en python para leer llineas de un archivo de texto "notas.txt". 
# su funcion debe encontrar y mostrar la aparicion de la palabra "el".
print("\nEjercicio 4:\n")
def buscar_el():
    try:
        with open("notas.txt", "r", encoding="utf-8") as archivo: #poner nombre del archivo para buscar.
            for numero_linea, linea in enumerate(archivo, start=1):
                if "el" in linea:
                    print(f"linea {numero_linea}: {linea.rstrip()}")
    except FileNotFoundError:
        print("el archivo 'notas.txt' no existe.")

buscar_el()
print("\n....................")



# 5)Escriba una fincion display_words() en python para leer las lineas de un archivo de texto "story.txt",
# y mostrar aquellas palabras que tengan menos de 4 caracteres.
print("\nEjercicio 5:\n")
def display_words():
    try:
        with open("story.txt", "r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                palabras = linea.split()
                for palabra in palabras:
                    if len(palabra) < 4:
                        print(f"linea {numero_linea}: {palabra}")
    except FileNotFoundError:
        print("el archivo 'story.txt' no existe.")

display_words()
print("\n....................")



# Un archivo de texto llamado "materia.txt" cotiene algun texto,
# que necesita ser mostrado de manera que cada caracter siguiente este separado por un simbolo "#".
# Escriba una definicion de funcion para hash_display() en python 
# que muestre todo el contenido del archivo "materia.txt" de esta manera.
# en el formato deseado.
# Ejemplo: si el archivo "materia.txt" tiene el siguiente contenido almacenado: 
# EL MUJNDO ES REDONDO
# la funciion hash_display() deberia mostrar el siguiente contenido:
# E#L# #M#U#N#D#O# #E#S# #R#E#D#O#N#D#O#
print("\nEjercicio 6:\n")
def hash_display():
    try:
        with open("materia.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read().rstrip('\n')
            resultado = "#".join(contenido)
            print(resultado)
    except FileNotFoundError:
        print("el archivo 'materia.txt' no existe.")

hash_display()
print("\n....................")


 #7) escribe un programa en python para generar 26 archivios de texto llamados A.txt, B.txt,
 # y asi sucesivamente hasta z.
print("\nEjercicio 7:\n")
import string
import os
def gen_archivos_alfabeto():
    archivos_existentes = all(os.path.exists(f"{letra}.txt") for letra in string.ascii_uppercase)
    if archivos_existentes:
        print("ya existen los archivos solicitadaos")
    else:
        for letra in string.ascii_uppercase:
            nombre_archivo = f"{letra}.txt"
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(f"este es el archivo {nombre_archivo}\n")
        print("ya se crearon todos los archivos")

gen_archivos_alfabeto()
print("\n....................")



# 8) escribe un programa en python para añadir texto a un archivo y mostrar el texto en python.txt
print("\nEjercicio 8:\n")
def añadir_texto():
    try:
        texto = input("introduce el texto que deseas añadir al archivo: ")
        with open("python.txt", "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
        print("\ncontenido actual de 'python.txt':")
        with open("python.txt", "r", encoding="utf-8") as archivo:
            print(archivo.read())
    except Exception as e:
        print(f"ocurrio un error: {e}")

añadir_texto()
print("\n....................")



# 9) Escribe un programa en python para calcular la frecuencia de todas las palabras de un archivo de texto
print("\nEjercicio 9:\n")
def frecuencia_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().lower()
            palabras = contenido.split()
            frecuencia = {}
            for palabra in palabras:
                if palabra in frecuencia:
                    frecuencia[palabra] += 1
                else:
                    frecuencia[palabra] = 1
            print("frecuencia de palabras:")
            for palabra, conteo in frecuencia.items():
                print(f"{palabra}: {conteo}")
    except FileNotFoundError:
        print(f"el archivo '{nombre_archivo}' no existe.")


frecuencia_palabras("python.txt")
print("\n....................")



# 10) escribe un programa en python para comprobar si un archivo especificado existe.
print("\nEjercicio 10:\n")

def comprobar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print(f"el archivo '{nombre_archivo}' existe.")
    else:
        print(f"el archivo '{nombre_archivo}' no existe.")

archivo = input("introduce el nombre del archivo que buscas: ")
comprobar_archivo(archivo)
print("\n....................")



#LOS SIGUIENTES EJERCICIOS SON A PARTIR DE LA PAGINA 13 DEL PDF DE EJERCICIOS.

# 11) Para realizar los ejercicios usar el archivo CSVAutomobile_data.csv.
# a partir del conjunto de datos dado, imprime las cinco primeras y ultimas filas.
print("\nEjercicio 11:\n")
import pandas as pd

def mostrar_5_primeras_y_ult_filas(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        print("cinco primeras filas:")
        print(df.head(5))
        print("\ncinco últimas filas:")
        print(df.tail(5))
    except FileNotFoundError:
        print(f"el archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"ocurrio un error: {e}")
#parece ser que solo encuentra el archivo si esta en la carpeta base del proyecto. 
mostrar_5_primeras_y_ult_filas("CSVAutomobile_data.csv")
print("\n....................")



# 12) Limmpia el conjunto de datos y actualiza el archivo CSV.
# Reemplaza todos los valores de las columnas que contenga ?, n.a o NaN.
print("\nEjercicio 12:\n")
import numpy as np

def limpiar_y_actualizar(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo) # leer el archivo CSV
        df.replace(['?', 'n.a', 'NaN'], np.nan, inplace=True) # reemplaza
        df.to_csv(nombre_archivo, index=False)
        print("el archivo ha sido limpiado y actualizado correctamente.")
    except FileNotFoundError:
        print(f"el archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"ocurrio un error: {e}")

# cambia el nombre del archivo por el que estés usando realmente
limpiar_y_actualizar("CSVAutomobile_data.csv")
print("\n....................")



# 13) escribe un codigo que encuentra el nombre de la empresa del coche mas caro,
# imprime el nombre de la empresa del coche dcaro y su precio usando el archivo csv
print("\nEjercicio 13:\n")
def empresa_mas_cara(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['price']) # Elimina filas con precios no válidos
        idx_max = df['price'].idxmax()
        empresa = df.loc[idx_max, 'company']
        precio = df.loc[idx_max, 'price']
        print(f"La empresa del coche más caro es: {empresa}")
        print(f"El precio del coche más caro es: {precio}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

empresa_mas_cara("CSVAutomobile_data.csv") # Cambia el nombre del archivo por el que estés usando realmente
print("\n....................")



# 14) imprime todos los datos de los cochces Toyota.
print("\nEjercicio 14:\n")
def only_toyota(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        # Filtra las filas donde la columna 'company' sea 'toyota'
        toyota_df = df[df['company'].str.lower() == 'toyota']
        if not toyota_df.empty:
            print("datos de los coches Toyota:")
            print(toyota_df)
        else:
            print("no se encontraron coches Toyota en el archivo.")
    except FileNotFoundError:
        print(f"el archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"ocurrio un error: {e}")

only_toyota("CSVAutomobile_data.csv")
print("\n....................")



# 15) cuenta el total de coches por empresa.    
print("\nEjercicio 15:\n")
def total_num_empresa(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        conteo = df['company'].value_counts()
        print("Total de coches por empresa:")
        print(conteo)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

total_num_empresa("CSVAutomobile_data.csv")
print("\n....................")



#16) Encuentra el coche con el precio mas alto de cada empresa
print("\nEjercicio 16:\n")
def coche_mas_caro_por_empresa(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['price'])
        idx = df.groupby('company')['price'].idxmax()
        coches_mas_caros = df.loc[idx, ['company', 'price']]
        print("Coche más caro de cada empresa:")
        print(coches_mas_caros)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

coche_mas_caro_por_empresa("CSVAutomobile_data.csv")
print("\n....................")



#17) encuentra el kilometraje medio de cada empresa fabricante de automoviles.
print("\nEjercicio 17:\n")
def kilometraje_empresa(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        # Asegúrate de que la columna 'average-mileage' sea numérica
        df['average-mileage'] = pd.to_numeric(df['average-mileage'], errors='coerce')
        # Agrupa por empresa y calcula el promedio
        promedio = df.groupby('company')['average-mileage'].mean()
        print("Kilometraje medio por empresa:")
        print(promedio)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

kilometraje_empresa("CSVAutomobile_data.csv")
print("\n....................")



# 18) ordena todos los coches por columna de precio
print("\nEjercicio 18:\n")
def ordenar_precio(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df_ordenado = df.sort_values(by='price')
        print("Coches ordenados por precio:")
        print(df_ordenado)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

ordenar_precio("CSVAutomobile_data.csv")
print("\n....................")



# 19) concatena dos dataframes uytiilizando las condiciones de la pagina 21 del pdf de ejercicios.
print("\nEjercicio 19:\n")  
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}

df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(japaneseCars)

print("German Cars:")
print(df_german)
print("\nJapanese Cars:")
print(df_japanese)
print("\n....................")



# 20) combina dos dataframe utilizando la condicion de la pagina 22. 
# Crea dos dataframes utilizando los siguientes dos Dicts, fusionalos y 
# añade el seguyndo dataframe como una nueva columna al primer dataframe.
print("\nEjercicio 20:\n") 
Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]}

df_price = pd.DataFrame(Car_Price)
df_hp = pd.DataFrame(car_Horsepower)

df_combinado = pd.merge(df_price, df_hp, on='Company') #los fusiona usando company

print("DataFrame combinado:")
print(df_combinado)
print("\n....................")



#LOS SIGUIENTES EJERCICIOS SON A PARTIR DE LA PAGINA 23 DEL PDF DE EJERCICIOS.

# 21) Crea un array de enteros 4x2 e imprime sus atributos.
# nota: El eelemento debe ser de tipo unsignedint16.
# imprime los siguientes atributos:
# La shape del array.
# Las dimensiones del array.
# El tamaño de cada elemento del array en bytes.
print("\nEjercicio 21:\n")
# Crear un array de enteros 4x2 de tipo unsigned int16
array = np.zeros((4, 2), dtype=np.uint16) #array 4x2 de tipo unsignet int16

print("array:")
print(array)
print("shape del array:", array.shape)
print("dimensiones del array:", array.ndim)
print("tamaño en bytes:", array.itemsize)
print("\n....................")



# 22) crea una matriz de enteros 5x2 de un rango entre 100 y 200 tal que la diferencia entre cada elemento sea 10.
print("\nEjercicio 22:\n")  

array = np.arange(100, 200, 10) #array de 10 elementos desde 100 hasta 190 con paso 10
matriz = array.reshape(5, 2) # redimensionar a 5x2

print("Matriz 5x2:")
print(matriz)
print("\n....................")



#23) A continuacion se muestra el array Numpy proporcionado (pag25). 
# Devuelver un array de elementos tomando la tercera columna de todas las filas.
print("\nEjercicio 23:\n")
Array_ejemplo = np.array([[11, 22, 33],
                        [44, 55, 66],
                        [77, 88, 99]])

tercera_columna = Array_ejemplo[:, 2] #tercera columna (indice2) de las filas.

print("Tercera columna de todas las filas:")
print(tercera_columna)
print("\n....................")



# 24) Devuelve un array de filas impares y columnas parees dado por el siguiente array (pag26).
print("\nEjercicio 24:\n")

Array_ejemplo = np.array([
    [3, 6, 9, 12],
    [15, 18, 21, 24],
    [27, 30, 33, 36],
    [39, 42, 45, 48],
    [51, 54, 57, 60]
])
resultado = Array_ejemplo[1::2, ::2]

print("array de filas impares y columnas pares:")
print(resultado)



#25) Crea una matriz de resultados sumando las siguientees dos matrices de NumPy. 
# A continuacion, modifica la matriz de resultados calculando el cuadrado de cada elemento.
print("\nEjercicio 25:\n")   

array_1 = np.array([[5, 6, 9], [21, 18, 27]])
array_2 = np.array([[15, 33, 24], [4, 7, 1]])

resultado = array_1 + array_2 #las sumamos

print("Matriz suma:")
print(resultado)


resultado_cuadrado = resultado ** 2   #lo elevamos al cuadrado.

print("Matriz suma al cuadrado:")
print(resultado_cuadrado)
print("\n....................")



# 26) Divide la matriz en cuatro submatriices de igual tamaños.
# Nota: Crea una matriz de enteros 8x3 de un ragon entre 10 y 34
# de tal manera que la diferencia entre cada elemento sea 1
# y luego divide la matriiz en cuatro submatrices de igual tamaño
print("\nEjercicio 26:\n")

# Crear la matriz 8x3
matriz = np.arange(10, 34).reshape(8, 3)
print("Matriz original 8x3:")
print(matriz)

# Dividir en 4 submatrices de 2x3 usando np.vsplit
submatrices = np.vsplit(matriz, 4)

for i, sub in enumerate(submatrices, 1):
    print(f"\nSubmatriz {i}:")
    print(sub)

print("\n....................")



#27) Ordena el array de numpy (pag29):
# caso1: ordenar el array por la segunda fila.
# caso2: ordenar el array por la segunda columna.
print("\nEjercicio 27:\n")

Array_ejemplo = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

# Caso 1: Ordenar el array por la segunda fila (índice 1)
orden_col = np.argsort(Array_ejemplo[1, :])
ordenado_x_seg_fila = Array_ejemplo[:, orden_col]

print("Array ordenado por la segunda fila:")
print(ordenado_x_seg_fila)

# Caso 2: Ordenar el array por la segunda columna (índice 1)
orden_fil = np.argsort(Array_ejemplo[:, 1])
ordenado_x_seg_columna = Array_ejemplo[orden_fil, :]

print("\nArray ordenado por la segunda columna:")
print(ordenado_x_seg_columna)
print("\n....................")



#28) Imprime el maximo del eje 0 y el minimmo del eje 1 de la matriz bidimensional (pag30).
print("\nEjercicio 28:\n")
Array_ejemplo = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
max_eje_0 = np.max(Array_ejemplo, axis=0)  # Máximo por columnas (eje 0)
min_eje_1 = np.min(Array_ejemplo, axis=1)  # Mínimo por filas (eje 1)

print("Máximo del eje 0 (columnas):")
print(max_eje_0)
print("\nMínimo del eje 1 (filas):")
print(min_eje_1)
print("\n....................")



# 29) Elimina la segunda columna de una matriz dada e inserta la siguiente columna nueva en su lugar.
print("\nEjercicio 29:\n")
sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
newColumn = np.array([[10]]).T  # Transponer para que sea columna

# Eliminar la segunda columna (índice 1)
sin_segunda_col = np.delete(sampleArray, 1, axis=1)

# Insertar la nueva columna en la posición 1
resultado = np.insert(sin_segunda_col, 1, newColumn, axis=1)

print("Matriz original:")
print(sampleArray)
print("Matriz resultante:")
print(resultado)
print("\n....................")



#LOS SIGUIENTES EJERCICIOS SON A PARTIR DE LA PAGINA 32 DEL PDF DE EJERCICIOS.
# PARA RESOLVER LOS SIGUIENTES EJERCICIOS SE DEBE USAR EL FICHERO CSVCompany_sales_data.csv.
# 30) Lee el beneficio total de todos los meses y muestralo con un grafico de lineas.
# Se proporcionan los datos del beneficio total de cada mes.
# El grafico de lineas generado debe incluir las siguiieintes propiedades:
# Nombre de la etiqueta X = numero de mes.
# Nombre de la etiqueta Y = beneficio total.
print("\nEjercicio 30:\n") 
import matplotlib.pyplot as plt

df = pd.read_csv("CSVCompany_sales_data.csv") #ajusta el nombre del archivo a leer.

# Supongamos que la columna de beneficio total se llama 'total_profit'
# Si tiene otro nombre, cámbialo por el correcto
beneficio_total = df['total_profit']

# Crear el gráfico de líneas
plt.plot(range(1, len(beneficio_total) + 1), beneficio_total)
plt.title("Beneficios por mes")
plt.xlabel("Número del mes")
plt.ylabel("Beneficio total")
plt.grid(True)
plt.show()
print("\n....................")



# 31) Obtenga el beneficio total de todos los meses y muestre un grafico de lineas con las siguientes propiedades:
# Estilo dee linea punteada y de color rojo.
# Mostrar la leyenda en la parte inferior derecha.
# Nombre de etiqueta X = numero de mes.
# Nombre de etiqueta Y = numero de unidades vendidas.
# Añadir un marcador de circulo.
# El ancho de la linea debe ser 3.
print("\nEjercicio 31:\n")

df = pd.read_csv("CSVCompany_sales_data.csv")
beneficio_total = df['total_profit']

plt.plot(
    range(1, len(beneficio_total) + 1),
    beneficio_total,
    color='red',
    linestyle='--',
    linewidth=3,
    marker='o',
    markerfacecolor='black',
    label='Profit data of last year'
)
plt.title("Beneficios por mes")
plt.xlabel("Número del mes")
plt.ylabel("Beneficio total")
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
print("\n....................")



# 32) Lee todos los datos de ventas de productos y
# muestralos mediante un grafico muiltilinea.
# Muestra el numero de unidades vendidas por mes para cad aproducto utiliiizando graficos multilinea.
print("\nEjercicio 32:\n")

df = pd.read_csv("CSVCompany_sales_data.csv")

productos = [
    'facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'
]

for producto in productos: #lineas para cada producto.
    plt.plot(
        df['month_number'], 
        df[producto], 
        marker='o',
        markerfacecolor='black', 
        label=f"{producto.capitalize()} Sales Data"
    )

plt.title("Ventas")
plt.xlabel("Numero mes")
plt.ylabel("Unidad de ventas en numero")
plt.legend()
plt.grid(True)
plt.show()
print("\n....................")



# 33) Lee los datos de las ventas de pasta de dientes de cada mes 
# y muestralos mediante un grafico de dispersion (scatter).
# Ademas, añade una cuadricula en el grafico.
# El estilo de la cuadricula debe ser "-"
print("\nEjercicio 33:\n")
df = pd.read_csv("CSVCompany_sales_data.csv")

plt.scatter(
    df['month_number'],
    df['toothpaste'],
    color='blue',
    label='Ventas de pasta de dientes'
)

plt.title("Ventas pasta de dientes")
plt.xlabel("Numero del mes")
plt.ylabel("Numero de unidades vendidas")
plt.legend()
plt.grid(True, linestyle='--')  # Cuadrícula con estilo de línea '-'
plt.show()
print("\n....................")



# 34) Lee los datos de ventas de los productos crema facial y lavado de cara y muestralos mediante el grafico barras.
# el grafico de barras debe mostrar el numero de unidades vendidas por mes para cada producto.
# añade una barra distnta para cada producto en el mismo grafico.
print("\nEjercicio 34:\n")
df = pd.read_csv("CSVCompany_sales_data.csv")

meses = df['month_number']
facecream = df['facecream']
facewash = df['facewash']

# Posición de las barras
ancho = 0.35
r1 = meses - ancho/2
r2 = meses + ancho/2

plt.bar(r1, facecream, width=ancho, label='Ventas crema facial')
plt.bar(r2, facewash, width=ancho, label='Ventas lavado de cara')

plt.title("Facewash and facecream sales data")
plt.xlabel("Numero del mes")
plt.ylabel("Unidades de ventas en numero")
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
print("\n....................")



#35) Lee los datos de ventas del jabon de baño de todos los mesesy muestrado con grafico de barras.
# guarda este grafico en tu disco duro.
print("\nEjercicio 35:\n")
df = pd.read_csv("CSVCompany_sales_data.csv")

plt.bar(df['month_number'], df['bathingsoap'], color='steelblue')
plt.title("Ventas jabon de baño")
plt.xlabel("Numero del mes")
plt.ylabel("Unidades de ventas en numero")
plt.grid(True, linestyle='--')
plt.savefig("ventas_jabon_bano.png")  # Guarda el gráfico en tu disco duro
print("Ya se guardó el gráfico en el PC") 
plt.show()
print("\n....................")



#36) Lee el beneficio total de cada mes 
# y muestralo utilizando el historigrama para ver los rangos de beneficio mas comunes.
print("\nEjercicio 36:\n")
df = pd.read_csv("CSVCompany_sales_data.csv")
beneficio_total = df['total_profit']

plt.hist(beneficio_total, bins=5, color='steelblue', label='Profit')
plt.title("Profit")
plt.xlabel("profit en dolares")
plt.ylabel("Actual Profit en dolares")
plt.legend(loc='upper left')
plt.show()
print("\n....................")



# 37) Calcula los datos de ventas totales del ultimo año para cada producto.
# muestralos mediante un gracifo circular.
# nota: En el grafico circular muestra el numero de uniidades vendidas por año en porcentaje.
print("\nEjercicio 37:\n")
df = pd.read_csv("CSVCompany_sales_data.csv")

ventas = [  # Suma total de ventas por producto
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = [
    'Crema facial',
    'Lavado de cara',
    'Pasta de dientes',
    'Gel de baño',
    'Shampoo',
    'Moisturizer'
]

plt.pie(ventas, labels=labels, autopct='%1.1f%%')
plt.title("Sales data")
plt.legend(labels, loc='lower right')
plt.show()
print("\n....................")



# 38)  Lee el jabon de baño dee todos los meses y visualizalo utiilizando el Subplot.
print("\nEjercicio 38:\n")  
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSVCompany_sales_data.csv")

meses = df['month_number']
bathingsoap = df['bathingsoap']
facewash = df['facewash']

plt.figure(figsize=(8, 6))

# Primer subplot: Ventas gel de baño
plt.subplot(2, 1, 1)
plt.plot(meses, bathingsoap, color='black', marker='o')
plt.title("Ventas gel de baño")
plt.ylabel("Unidades de ventas en numero")

# Segundo subplot: Ventas lavado de cara
plt.subplot(2, 1, 2)
plt.plot(meses, facewash, color='red', marker='o')
plt.title("Ventas lavado de cara")
plt.xlabel("Numero del mes")
plt.ylabel("Unidades de ventas en numero")

plt.tight_layout()
plt.show()
print("\n....................")



#39) Lee todos los datos de ventas de produtocs y muestrelos mediante un diagrama de pila.
print("\nEjercicio 39:\n")
df = pd.read_csv("CSVCompany_sales_data.csv")

meses = df['month_number']
facecream = df['facecream']
facewash = df['facewash']
toothpaste = df['toothpaste']
bathingsoap = df['bathingsoap']
shampoo = df['shampoo']
moisturizer = df['moisturizer']

plt.figure(figsize=(10, 6))
plt.stackplot(
    meses,
    facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer,
    labels=[
        'Crema facial', 'Lavado de cara', 'Pasta de dientes',
        'Gel de baño', 'Shampoo', 'Moisturizer'
    ],
    colors=['magenta', 'cyan', 'red', 'black', 'green', 'yellow']
)
plt.title("Todas las ventas de productos en un stack plot")
plt.xlabel("Numero del mes")
plt.ylabel("Unidades de ventas en numero")
plt.legend(loc='upper left')
plt.show()
print("\n....................")
print("Fin de los ejercicios del modulo 5 de Python (escuela MUSK) de JoseManuel Gonzalez Gil.")
# FIN DE LOS EJERCICIOS DEL MODULO 5 DE PYTHON (ESCUELA MUSK) DE JOSEMANUEL GONZALEZ GIL.