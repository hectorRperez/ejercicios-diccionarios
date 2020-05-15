""" Ejercicio 9

Escribir un programa que gestione las facturas pendientes de cobro de una empresa.

Las facturas se almacenarán en un diccionario donde la clave de cada factura será el 
número de factura y el valor el coste de la factura. 

El programa debe preguntar al usuario si quiere 

1) añadir una nueva factura

    Si desea añadir una nueva factura se preguntará por el número de factura y su coste y 
    se añadirá al diccionario.

2) pagar una existente o terminar.

    Si se desea pagar una factura se preguntará por el número de factura y 
    se eliminará del diccionario.

Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta 
el momento y la cantidad pendiente de cobro.
"""


def agregar_factura():
    '''
    Función que agrega facturas a un diccionario
    parametros:
        No recibe nada
    Devuelve:
        No devuelve nada
    '''
    global mis_facturas

    print('====================================')
    print('AGREGAR FACTURA')
    print('====================================')

    numero_factura = int(input('Ingrese el número de factura: '))
    monto_factura = float(input('Ingrese el monto de la factura: '))

    mis_facturas[numero_factura] = monto_factura

    print('Agregada correctamente')
    print('--------------------------------------')

#TODO DOCUMENTAR LA FUNCION
def pagar_factura():
    '''
    Función que se encarga de pagar las facturas existente en un diccionario
    parametros:
        No recibe nada
    Devuelve:
        No devuelve nada
    '''

    print('====================================')
    print('PAGAR FACTURA')
    print('Numero factura \tMonto')
    for i,j in mis_facturas.items():
        print('°',i,'\t\t',j,'$')
    print('====================================')

    numero_factura = int(input('Ingrese el número de la factura: '))
    if numero_factura in mis_facturas:
        print('Factura pagada correctamente')
        del mis_facturas[numero_factura]
    else:
        print('No existe')

if __name__ == '__main__':    
    mis_facturas = {}

    while True:

        opcion = int(input('1) Añadir nueva factura \n2) Pagar factura existente \n3)Salir \nOpcion: '))
    
        if opcion == 1:
            agregar_factura()

        elif opcion == 2:
            pagar_factura()

        elif opcion == 3:
            print('Saliendo...')
            break
        else:
            print('Opcion invalida')