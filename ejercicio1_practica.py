""" Ejercicio 1

Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso 
si la divisa no está en el diccionario. 

"""

def mostrar_diccionario():
    mi_diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input('Ingrese una divisa: ')
    print(mi_diccionario.get(str.title(divisa), 'La divisa no existe'))

if __name__ == '__main__':
    mostrar_diccionario()