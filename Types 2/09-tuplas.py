numeros = (1, 2, 3) + (4, 5, 6)

punto = tuple([1, 2])

menosNumeros = numeros[:2]

primero, segundo, *otros = numeros

for n in numeros:
    print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
