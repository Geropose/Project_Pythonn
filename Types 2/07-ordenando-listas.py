numeros = [2, 3, 5, 79, 8, 4, 10, 6, 7]

numeros.sort(
    reverse=True
)  # Para ordenar descendentemente puedo poner reverse=True y lo cambia
numeros2 = sorted(
    numeros,  # reverse=True se puede aplicar como argumento a la func sorted
)  # La diferencia es que sorted devuelve una NUEVA lista, es decir, no afecta el listado anterior

usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]


def ordena(elemento):
    return elemento[1]


# Funcion lambda

usuarios.sort(key=lambda el: el[1])
# usuarios.sort(key=ordena)
print(numeros)
