def division(n=0):
    if n == 0:
        # luego del raise va el nombre de la excepcion, el nombre de las excepciones estan documentadas y ya declaradas!
        raise ZeroDivisionError("No se puede dividir por 0", f"{n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)
