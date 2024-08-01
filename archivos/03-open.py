from io import open

# # Escritura
# texto = "Hola mundo"

# archivo = open("archivos/hola-mundo.txt", "w")

# # Si el archivo no existe, entonces lo crea

# archivo.write(texto)
# archivo.close()

# # Lectura

# archivo = open("archivos/hola-mundo.txt", "r")

# texto = archivo.read()
# archivo.close()
# print(texto)

# Lectura como lista

# archivo = open("archivos/hola-mundo.txt", "r")

# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek()
#     for linea in archivo:
#         print(linea)

# Agregar

# archivo = open("archivos/hola-mundo.py", "a+")
# archivo.write("Chau mundo")
# archivo.close()

# Lectura y escritura

with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "chanchito feliz la"
    archivo.writelines(texto)
