class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigoError):
        self.mensaje = mensaje
        self.codigoError = codigoError

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigoError}"


def division(n=0):
    if n == 0:
        # luego del raise va el nombre de la excepcion, el nombre de las excepciones estan documentadas y ya declaradas!
        raise MiError("No se puede dividir por 0", 805)
    return 5 / n


try:
    division()
except MiError as e:
    print(e)
    # print("El error es: " f"{e.codigoError}")
    # print(e.mensaje)
