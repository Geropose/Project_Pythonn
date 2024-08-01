class Perro:

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chau perro{self.nombre}")

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} Dice: Guau!")


perro = Perro("Chanchito", 7)
print(perro)
texto = str(perro)
print(texto)  # basicamente con el metodo str vuelve el nombre del perro a String
# Los famosos "metodos magicos" son todos aquellos que ya estan definidos por dentro del lenguaje. Magic Method Python
