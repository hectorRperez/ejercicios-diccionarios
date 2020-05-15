""" Ejercicio 6

Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario. """


def mostrar_informacion():
    
    mis_personas = {}

    while True:

        opcion = int(input('1) Agregar persona \n2) Salir \n3)Opcion: '))
        if opcion == 1:

            nombre = input('Ingrese un nombre para la persona: ')
            mis_personas['nombre'] = nombre
            print(mis_personas)

            edad = input('Edad de la persona: ')
            mis_personas['edad'] = edad
            print(mis_personas)

            sexo = input('Sexo de la persona: ')
            mis_personas['sexo'] = sexo
            print(mis_personas)

            telefono = input('Telefono de la persona: ')
            mis_personas['telefono'] = telefono
            print(mis_personas)

            correo_electronico = input('Correo electronico: ')
            mis_personas['correo_electronico'] = correo_electronico
            print(mis_personas)

        elif opcion == 2:
            print('Saliendo...')
            break
        else:
            print('Opcion ingresada incorrecta')

if __name__ == '__main__':
    mostrar_informacion()