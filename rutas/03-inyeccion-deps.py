# from pathlib import Path
# from db import db
# import graphql
# import api


# path = Path()

# paths = [p for p in path.iterdir() if p.is_dir()]

# dependencias = {
#     "db": db,
#     "api": api,
#     "graphql": graphql,
# }


# def load(p):
#     paquete = __import__(str(p).replace("/", "."))
#     try:
#         paquete.init(**dependencias)
#     except:
#         print("el paquete no tiene funcion")


# list(map(load, paths))
