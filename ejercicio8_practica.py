""" Ejercicio 8

Escribir un programa que cree un diccionario de traducción español-inglés. 

El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. 

El programa debe crear un diccionario con las palabras y sus traducciones.

Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir. """


def traducir_ingles_espanol(frase):

    ingles_espanol = {
        'house': 'casa',
        'dog': 'perro',
        'man': 'hombre',
        'car': 'carro'
    }

    frase = frase.split(' ')
    frase_nueva = ''
    for i in frase:
        if i in ingles_espanol:
            frase_nueva += ' ' +ingles_espanol[i]

    print(frase_nueva)

def traducir_espanol_ingles(frase):

    espanol_ingles = {
        'del' : 'of the',
        'los' : 'the',
        'casa': 'house',
        'perro': 'dog',
        'perros': 'dogs',
        'hombre': 'man',
        'carro': 'car',
        'estan': 'are',
        'abajo': 'down'
    }

    frase = frase.split(' ')
    frase_nueva = ''
    for i in frase:
        if i in espanol_ingles:
            frase_nueva += ' ' +espanol_ingles[i]

    print(frase_nueva)

if __name__ == '__main__':

    opcion = int(input('1) Traduccir de ingles a español \n2)Traduccir de español a ingles \nOpcion: '))

    if opcion == 1:
        frase = input('Ingrese la frase a traduccir: ')
        traducir_ingles_espanol(frase)
    elif opcion == 2:
        frase = input('Ingrese la frase a traduccir: ')
        traducir_espanol_ingles(frase)
    else:
        print('La opcion es invalida')