from modulos.usuarios.acciones.utilidades import guardar, pagar_impuestos
import usuarios

# La mejor manera de importar, mas precisa y que menos problemas me puede llegar a traer es la de arriba!
# En su defecto, la de abajo tambien sirve.
# from usuarios import acciones

# import usuarios.acciones
# Esta es la peor!!!!!
# Hay varias maneras de importar

# usuarios.acciones.guardar()
# Esto es bastante tedioso, por lo que no se recomienda usar.


guardar()

print(dir(usuarios))  # Me lista todos los paquetes de algun area en especifico.
