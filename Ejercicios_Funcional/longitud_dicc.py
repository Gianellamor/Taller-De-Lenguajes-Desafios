#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud
def medicion(frase):
    palabras = frase.split()
    return {palabra: len(palabra) for palabra in palabras}

texto = input("Ingrese su frase: ")
resultado = medicion(texto)

print(resultado)