""" 

Ejercicio 10

Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que 
la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente

nombre
dirección 
teléfono 
correo
preferente 

donde preferente tendrá el valor True si se trata de un cliente preferente. 

El programa debe preguntar al usuario por una opción del siguiente menú: 

(1) Añadir cliente, 
(2) Eliminar cliente, 
(3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes preferentes, 
(6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente
crear un diccionario con los datos
añadirlo a la base de datos.
Preguntar por el NIF del cliente
eliminar sus datos de la base de datos.

Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa. 

"""


def agregar_cliente():
    '''
    Función que se encarga de agregar cliente a un diccionario
    tiene dos diccionarios
        - persona que tiene como valor otro diccionario datos_persona
    parametros:
        No recibe nada
    Devuelve:
        No devuelve nada, solo muestra un mensaje de agregado el cliente al diccionario
    '''
    print('====================================')
    print('AGREGAR CLIENTE')
    print('====================================')
    nif_persona = int(input('Ingrese el NIF de la persona: '))
    nombre = input('Ingrese el nombre de la persona: ')
    direccion = input('Ingrese la dirección: ')
    telefono = input('Ingrese el telefono: ')
    correo = input('Ingrese el correo: ')
    preferente = input('Ingrese el preferente (V/F): ').title()

    datos_persona = {

        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferente': preferente
    }

    persona[nif_persona] = datos_persona
    print('El cliente ',nombre,' ha sido agregado correctamente')
    print(' --------------------------------------------------------- ')


def eliminar_cliente():
    print('====================================')
    print('ELIMINAR CLIENTE')
    print('====================================')

    print('NIF\tNombre')
    print('-------------------------------------------------------- ')
    for i,j in persona.items():
        print(i,'\t', j['nombre'])
    print(' --------------------------------------------------------- ')
    
    numero_cliente = int(input('Ingrese el NIF del cliente: '))

    if numero_cliente in persona:
        respuesta = input('¿Esta seguro de eliminar el cliente? (Y/N): ').title()
        if respuesta == 'Y':
            del persona[numero_cliente]
            print('Cliente eliminado correctamente')
            print('-------------------------------------------------------- ')
    else:
        print('No existe')

def mostrar_cliente():
    print('====================================')
    print('MOSTRAR CLIENTE')
    print('====================================')

    numero_cliente = int(input('Ingrese el NIF del cliente: '))

    if numero_cliente in persona:

        print(' --------------------------------------------------------- ')
        print('DATOS DEL CLIENTE')
        print(' --------------------------------------------------------- ')
        for i,j in persona[numero_cliente].items():
            print(i,' ',j)
        print(' --------------------------------------------------------- ')
    else:
        print('No existe')

def lista_clientes():
    print('====================================')
    print('MOSTRAR TODOS LOS CLIENTES')
    print('====================================')

    print('NIF\tNombre')
    print('-------------------------------------------------------- ')
    for i,j in persona.items():
        print(i,'\t', j['nombre'])
    print(' --------------------------------------------------------- ')

def lista_clientes_vip():
    print('====================================')
    print('MOSTRAR TODOS LOS CLIENTES VIP')
    print('====================================')

    for i,j in persona.items():
        if j['preferente'] == 'V':
            print(i,' ',j['nombre'])
    
    print(' --------------------------------------------------------- ')


if __name__ == '__main__':

    persona = {}
    datos_persona = {}

    while True:
        opcion = int(input('1) Agregar cliente \n2) Eliminar cliente \n3) Mostrar cliente'
                           '\n4) Listar todos los clientes \n5) Listar cliente preferentes'
                           '\n6) Terminar \nOpciones: '))
        #TODO faltan agregar funciones
        if opcion == 1:
            agregar_cliente()
        elif opcion == 2:
            eliminar_cliente()
        elif opcion == 3:
            mostrar_cliente()
        elif opcion == 4:
            lista_clientes()
        elif opcion == 5:
            lista_clientes_vip()
        elif opcion == 6:
            print('Saliendo...')
            break
        else:
            print(' --------------------------------------------------------- ')
            print('Opcion ingresada invalida')
            print(' --------------------------------------------------------- ')