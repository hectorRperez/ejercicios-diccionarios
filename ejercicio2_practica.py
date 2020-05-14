""" Ejercicio 2

Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
y lo guarde en un diccionario. 
Después debe mostrar 
por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>. """


def mostrar_usuario():
    
    mi_diccionario = {}

    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese la edad: ')
    direccion = input('Direccion: ')
    telefono = input('Telefono: ')

    mi_diccionario['nombre'] = nombre
    mi_diccionario['edad'] = edad
    mi_diccionario['direccion'] = direccion
    mi_diccionario['telefono'] = telefono

    print('{} tiene {} años, vive en la dirección {} y su numero de telefono es {}'.format(mi_diccionario['nombre'], mi_diccionario['edad'], mi_diccionario['direccion'], mi_diccionario['telefono']))

if __name__ == '__main__':
    mostrar_usuario()