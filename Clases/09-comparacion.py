class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        # Otro hace referencia a otra instancia de objeto que queremos comparar
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):
        # Basicamente ne significa not equal
        return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self, otro):
        # Basicamente ne significa not equal
        return self.lat + self.lon < otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
print(coords == coords2)
