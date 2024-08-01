from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"guardando {self.tabla} en BBDD")

    @classmethod
    def buscarPorId(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "usuario"

    def guardar(self):
        print("guardando usuario")


# model = Model() No la puedo instanciar porque es abstracta. Por lo que no me va a dejar crear un Model.
# Cuando tengo una clase abstracta no necesito un constructor, ya que se supone que no se va a crear nunca, por lo cual debe crearse el constructor en sus hijos/herencia
usuario = Usuario()

usuario.guardar()
usuario.buscarPorId(123)
