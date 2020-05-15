""" Ejercicio 4

Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
y muestre por pantalla la misma fecha 
en formato dd de <mes> de aaaa donde <mes> es el nombre del mes. """

def mostrar_fecha():

    mis_meses = {

        1 : 'Enero',
        2 : 'Febrero',
        3 : 'Marzo',
        4 : 'Abril',
        5 : 'Mayo',
        6 : 'Junio',
        7 : 'Julio',
        8 : 'Agosto',
        9 : 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'  
    }

    fecha = input('Ingrese una fecha con el formato dd/mm/aaaa: ')

    fecha = fecha.split('/')

    print('La fecha es {} de {} del año {}'.format(fecha[0], mis_meses[int(fecha[1])], fecha[2]))

if __name__ == '__main__':
    mostrar_fecha()