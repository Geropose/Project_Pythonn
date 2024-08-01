from pathlib import Path

path = Path("Directorio")
# path.exists()
# path.mkdir() #Crear el directorio/carpeta
# path.rmdir() #Remove directory, eliminar el directorio/carpeta. Debe tener la condicion de encontrarse vacio dentro de el mismo
# path.rename() #Renombra el directorio, dentro de los () debo poner el nombre como string

# for p in path.iterdir():
#     print(p)

# archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("01-x.py")]
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
