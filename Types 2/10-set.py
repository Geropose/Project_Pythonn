import sys


def print_python_version():
    """Function printing python version."""
    print(sys.version)


primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

print(
    primer ^ segundo
)  # Diferencia simetrica, nos devuelve los elementso que se encuentran en el primero y en el segundo pero que no se encuentran en la combinacion de ellos dos, es decir, no ponen los elementos que no estan compartidos entre ellos

if 5 in segundo:
    print("hola mundo")
