from pathlib import Path
from zipfile import ZipFile

# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     # PYTHON_UDEMY
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)


with ZipFile("archivos/comprimidos.zip", "w") as zip:
    print(ZipFile.namelist)
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(info.file_size, info.compress_size)
    zip.extractall("archivos/descomprimidos")
