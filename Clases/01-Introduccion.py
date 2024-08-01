mensaje = "Hola mundo"
print(type(mensaje))


class MiPerro:
    def habla(self):
        print("guau")


mi_perro = MiPerro()
print(type(mi_perro))

mi_perro.habla()
print(isinstance(mi_perro, MiPerro))
