class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = (
            nombre  # tener self. __name significa que la variable es privada
        )
        self.edad = edad

    def get_nombre(self):
        return self.__nombre  # Puedo leer el nombre pero no puedo cambiar su valor.

    def set_nombre(self, variable):
        self.__nombre = variable

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)  # Metodo de clase.


perro1 = Perro.factory()
perro1.habla()
