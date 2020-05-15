""" Ejercicio 7

Escribir un programa que cree un diccionario simulando 
una cesta de la compra. 

El programa debe preguntar el artículo y 
su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. 


Después se debe mostrar por pantalla la lista de la compra y el coste total, 
con el siguiente formato

Lista de la compra	 
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste """

# TODO
def cesta_alimento(nombre, precio=0):
    '''
    Funcion que simula una lista de compras, agregando los articulos a un diccionario
    parametros:
        alimento: El nombre del alimento 
        precio: Precio del alimento

    Devuelve:
        El diccionario con alimentos
    '''

    global mi_alimentos

    mi_alimentos[nombre] = precio
    print('Articulo agregado a la lista')

def costo_total():
    '''
    Función que calcula el costo total de la cesta de compras
    '''

    if len(mi_alimentos):
        
        costo_total = 0
        print('--------------------------')
        print('Lista de compras')
        print('--------------------------')
        for i,j in mi_alimentos.items():
            print(i,'\t\t',j,'$')
            costo_total+=j
        
        print('El costo total: ',round(costo_total,2),'$')
        print('--------------------------')

    else:
        print('No hay nada')

if __name__ == '__main__':

    mi_alimentos = {}

    while True:
        opcion = int(input('1) Ingresar un articulo nuevo \n2)Mostrar coste total \n3)Salir \nOpcion: '))

        if opcion == 1:
            nombre = input('Nombre del articulo: ')
            precio = float(input('Precio del articulo: '))

            cesta_alimento(nombre, precio)

        elif opcion == 2:
            costo_total()

        elif opcion == 3:
            print('Saliendo...')
            break
        
        else:
            print('Opcion ingresada invalida')