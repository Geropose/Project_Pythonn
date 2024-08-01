mascotas = ["Pelusa", "Pulga", "Felipe", "Pulga", "Chanchito feliz", "Wolfgang"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")  # Agrega a la ultima posicion

mascotas.remove(
    "Pulga"
)  # Si esta duplicado, elimina la primer ocurrencia, es decir, el primero que encuentra.
# Para eliminar el segundo, deberia contar

mascotas.pop(1)
del mascotas[0]
mascotas.clear()  # Limpia todo el arreglo, borra todo
print(mascotas)
