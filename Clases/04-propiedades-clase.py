class perro:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.edad = edad

    def habla(self):
        print("Guau!")


mi_perro = perro("Chanchito", 1)
mi_perro.habla()
