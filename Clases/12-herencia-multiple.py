class Animal:
    def comer(self):
        print("Comiendo")


class Perro:
    def pasear(self):
        print("Paseando")


class Chanchito(Perro, Animal):
    def programar(self):
        print("Programando")


# Python aplica herencia de izquierda a derecha, en este caso primero con los metodos de la clase Perro.
