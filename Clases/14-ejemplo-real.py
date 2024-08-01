class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"guardando {self.tabla} en BBDD")

    @classmethod
    def buscarPorId(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "usuario"


usuario = Usuario()

usuario.guardar()
usuario.buscarPorId(123)
