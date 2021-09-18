

"""Ejercicio 3
Genenerar su propia funcion reduce, que tome como parametro 
una funcion y una coleccion, devolviendo el acumulador resultante.
Luego imprimirlo.

  Ej: 
    acumulador = myReduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

    print(acumulador)
    
    >>> 30
"""
lista = [3, 1, 10, 8, 6, 2]
# print(functools.reduce(lambda x, b: x + b, lista))

# Sin reduce
def funcion(primer_parametro, segundo_parametro, acumulador = 0):
  for i in segundo_parametro:
      acumulador = primer_parametro(acumulador, i)
  return acumulador

resultado =  funcion(lambda x, b: x + b, lista)
print(resultado)
