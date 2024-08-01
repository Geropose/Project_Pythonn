from pathlib import Path

Path(r"C:\Archivos de programa\lugar")  # Para windows
Path("/usr/bin")  # Para linux, esto es una ruta ABSOLUTA
Path()
Path.home()  # Crea un path al inicio o el home del usuario.
Path("one/__init__.py")  # Esto es una ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file  # Es un archivo
path.is_dir  # Es un directorio
path.exists  # Si existe

print(
    path.name,  # Nombre de archivo completo con extension
    path.stem,  # Nombre de archivo sin extension
    path.suffix,  # Extension del archivo
    path.parent,  # Directorio padre de donde nosotros estamos generando nuestro directorio
    path.absolute(),
)

p = path.with_name("chanchito.py")
p = path.with_suffix(".bat")
p = path.with_stem("feliz")
