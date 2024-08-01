lista = [1, 2, 3, 4]
print()

lista2 = [5, 6]

combinada = ["Hola", *lista, "Mundo", *lista2]
print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
