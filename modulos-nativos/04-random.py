import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lista)
print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=3),
    random.choices("abcdefghijk.-,51235", k=4),
)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
print(seleccion)


contrasena = "".join(seleccion)
print(contrasena)
