class Perro:

    def __init__(self, nombre):
        self.nombre = nombre

    @property  # Solamente se utiliza con las funciones que me devuelven un valor, un getter. El set es la parte opuesta
    def nombre(self):
        print("pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
