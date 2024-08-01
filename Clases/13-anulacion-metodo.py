class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()  # De esta manera ejecuto el constructor de la clase padre
        self.nada = True

    def vuela(self):
        print("vuela pato")
        super().vuela()


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
