#Clase 1
def contar_letras(palabra):
    palabra_sin_espacio=palabra.replace(' ','')
    n=len(palabra_sin_espacio)
    return n

x=contar_letras("Hola mundo")
print(x)