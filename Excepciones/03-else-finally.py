try:
    n1 = int(input("Ingresa primer numero: "))
except ValueError as e:
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrio un error")
else:
    # Se ejecuta siempre y cuando no haya ninguna EXCEPCION!
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")
    # Se ejecuta siempre independientemente si hay errores o no
