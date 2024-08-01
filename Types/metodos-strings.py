animal = "chanchito feliz"
print(animal.upper())  # Pone el string en mayuscula
print(animal.lower())  # Pone el string en minuscula
print(
    animal.capitalize()
)  # Toma el primer caracter de nuestro string y le pone una mayuscula y el resto todo a minuscula.
print(
    animal.title()
)  # Toma la primer letra de cada palabra que se encuentre dentro de nuestro string y las pone en mayusculas.
print(
    animal.strip()
)  # Lo que hace es remover todos los espacios que se encuentren en blanco a la derecha y a la izquierda de nuestro string. "   Chanchito feliz    ", en este caso juntaria el string
print(animal.strip().capitalize())  # Se pueden concatenar los metodos
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("CH"))  # Busco una cadena de caracteres
print(
    animal.replace("nCH", "j")
)  # debe recibir dos argumentos, y deben ir separados por coma, primero va el valor que debe "buscar" y segundo por el cual va a reemplazar
print(
    "nCH" in animal
)  # La diferencia con find es que FIND devuelve el indice donde se encuentra la cadena de caracteres y el metodo IN va a devolver un boolean.
