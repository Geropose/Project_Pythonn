import json
from pathlib import Path

# escribir json

# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Skate"},
#     {"id": 3, "name": "Bicicleta"},
# ]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)

data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar json

productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))
