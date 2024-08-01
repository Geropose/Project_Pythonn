for numero in range(5):  # range 5 me crea una secuencia de numeros que comienza desde 0
    print(numero, numero * "hola mundo")

buscar = 10
for numero in range(5):
    if numero == buscar:
        print("Encontrado", buscar)
        break  # Detiene la ejecucion del codigo cuando encuentro lo que necesito!!! evita tener que seguir con el ciclo
else:
    print("no encontre el numero  buscado:")

for char in "Ultimate python":
    print(char)
