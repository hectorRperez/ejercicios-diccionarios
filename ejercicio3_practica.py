""" 
Ejercicio 3

Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70 

"""

def cesta_frutas():

    mis_frutas = {
        'Platano' : 1.35,
        'Manzana' : 0.80,
        'Pera'    : 0.85,
        'Naranja' : 0.70
    }

    print('Lista de frutas y precios ')
    print('--------------')
    for i,j in mis_frutas.items():
        print('Fruta: ',i)
        print('Precio: ',j,'$')
        print('--------------')
    
    nombre_fruta = input('Ingrese el nombre de la fruta: ').title()
    precio_fruta = float(input('Ingrese los kilos que desea: '))

    if nombre_fruta in mis_frutas:
        print('Su monto final por {} kg de {} = {}'.format(precio_fruta,nombre_fruta,mis_frutas[nombre_fruta]*precio_fruta))
    else:
        print('La fruta no existe')

if __name__ == '__main__':
    cesta_frutas()