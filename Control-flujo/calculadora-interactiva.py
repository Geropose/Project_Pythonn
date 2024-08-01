import sys


def print_python_version():
    print(sys.version)


# va a ser una calculadora interactiva
# debe verificar si ya ingrese un numero antes
# en el caso de que no haya sido ingresado un numero
# debo indicarle que el numero no fue ingresado
# si el numero fue ingresado, luego le pido que ingrese una operacion
# una vez que ingrese la operacion, debe ingresar otro numero
# una vez que esta todo, debo mostrar el resultado
# el resultado lo guardo como el primero numero
# en segundo termino le debo pedir que me ingrese la operacion nuevamente

# print("Bienvenidos a la calculadora")
# print("Para salir debe escribir Salir")
# print("Las operaciones que puede utilizar son suma, multi, div y resta")

# n1 = input("Ingresar primer numero")

# while len(n1) == 0:
#     print("Ingreso un numero incorrecto, ingreselo nuevamente")
#     n1 = input("Ingresar primer numero")

# operacion = input("Ingresar una operacion")
# while operacion.lower() != "salir":
#     n2 = input("Ingresar segundo numero")
#     while len(n2) == 0:
#         print("Ingreso un numero incorrecto, ingreselo nuevamente")
#         n2 = input("Ingresar segundo numero")
#     if operacion.lower() == "suma":
#         resultado = n1 + n2
#     if operacion.lower() == "multi":
#         resultado = n1 * n2
#     if operacion.lower() == "div":
#         resultado = n1 // n2
#     if operacion.lower() == "resta":
#         resultado = n1 - n2

#     n1 = resultado
#     print("El resultado es:", n1)
#     operacion = input("Ingresar una operacion")

# print("Hasta luego!")

print("Bienvenidos a la calculadora")
print("Para salir debe escribir Salir")
print("Las operaciones que puede utilizar son suma, multi, div y resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower == "salir":
            break
        resultado = int(resultado)
    print("loop infinito")
    op = input("Ingresa una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado /= n2
    elif op.lower() == "div":
        resultado *= n2
    else:
        print("Operacion no valida")
        break

print(f"El resultado es: {resultado}")
