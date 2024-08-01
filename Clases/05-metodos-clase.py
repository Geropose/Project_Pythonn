class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.name = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
# La manera corta es creando un metodo de clase que nos sirva, se denomina como un Factory Method. Nos crea instancias de perros
