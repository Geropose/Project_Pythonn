usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# nombres = list(map(lambda: usuario: usuario[0], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
# map

# filtrar - filter
