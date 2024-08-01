from pprint import pprint

# Eliminar los espacios en blanco de un string
string = "Hola mundo este es mi string"


def quitaEspacios(texto):
    return [char for char in texto if char != " "]


# Cuantas veces se repite una letra en un string
def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


# Ordenar las llaves de un diccionario por el valor que tienen y devolver un valor de lista que contiene tuplas
def ordenar(dict):
    return sorted(dict.items(), key=lambda key: key[1], reverse=True)


# Devolver los que tienen el mayor valor
def mayoresTuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


# Crea mensaje
def creaMensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = quitaEspacios(string)
print(string)
print(sin_espacios)
# Primero saco los espacios para poder contar los caracteres de forma correcta y evitar cualquier error
contados = cuenta_caracteres(sin_espacios)
ordenados = ordenar(contados)
mayores = mayoresTuplas(ordenados)
mensaje = creaMensaje(mayores)
pprint(contados, width=1)
print(ordenados)
print(mayores)
print(mensaje)
