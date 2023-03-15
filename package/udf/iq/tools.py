def indice_mayor_cercano(dato, lista):
    """Devuelve el indice del dato mayor mas cercano de 
    una lista ordenada
    """
    mayores = filter(lambda x: x > dato, lista)
    if mayores:
        return lista.index(next(mayores))
    else:
        return len(lista) - 1
