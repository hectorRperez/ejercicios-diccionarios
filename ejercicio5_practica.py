""" Ejercicio 5

Escribir un programa que almacene en un diccionario con los créditos de las asignaturas 
de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de 
cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso. """

def creditos_asignaturas():
    
    mis_cursos = {

        'Matematicas' : 6,
        'Fisica' : 4,
        'Quimica': 5
    }

    total_creditos = 0
    for i,j in mis_cursos.items():
        print('Asignatura',i,'tiene',j,' creditos')
        total_creditos += j

    print('El total de los creditos es: ',total_creditos)

if __name__ == '__main__':
    creditos_asignaturas()