def reverse(texto):
    texto_al_reves = " "
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def eliminar_espacios(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def es_palindromo(texto):
    texto = eliminar_espacios(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("abba"))
print(es_palindromo("dado"))
