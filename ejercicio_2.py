"""Ejercicio 2
Genenerar su propia funcion filter, que tome como parametro 
una funcion y una coleccion, devolviendo solo aquellos elementos
que cumplan con la condicion de dicha fn pasada como param.
Luego pasar el objeto resultante por una fn list() e imprimirlo.

  Ej: 
    objeto_resultante = myFilter(lambda x: x > 3, [3, 1, 10, 8, 6, 2])

    print(list(objeto_resultante))
    
    >>> [10, 8, 6]
"""

def filter (primer_parametro,segundo_parametro):
    for i in segundo_parametro:
        if primer_parametro(i):
            yield i


num = [3, 1, 10, 8, 6, 2]

# resultado = filter(lambda x: x > 3, num)
# print(list(resultado))

