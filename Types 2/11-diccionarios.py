punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

# Le puedo agregar mas valores al diccionario despues
punto["z"] = 45

if "lala" in punto:
    print("encontre lala", punto["lala"])

# Los diccionarios tienen el metodo GET
print(punto.get("x"))
print(punto.get("lala", 97))

del punto["x"]

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "nicolas"},
    {"id": 4, "nombre": "felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
