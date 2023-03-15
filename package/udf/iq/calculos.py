from tools import indice_mayor_cercano

def ordenar_datos(X, Y, ascendente=True):
    """Ordena de forma ascendente o descendente:
    Ordena el vector X de forma ascendente o descendente y al mismo tiempo
    reordena el vector Y de acuerdo a la nueva posición de los datos del vector
    'X'
    
    Args:
    X (list): Vector de datos x
    Y (list): Vector de datos y
    ascendente (bool, optional): Si es True, los datos serán ordenados de forma
    ascendente.  Si es False, los datos serán ordenados de forma
    descendente. Por defecto es True.
    
    Returns:
    X_ordenado (list): Vector X ordenado
    Y_ordenado (list): Vector Y ordenado
    """
    # Creamos una lista de tuplas
    datos = list(zip(X,Y))

    # Ordenamos la lista por el valor de x
    datos_ordenados = sorted(datos, key=lambda t: t[0], reverse=not ascendente)
    
    # separamos los datos ordenados en dos vectores X_ordenado e Y_ordenado
    X_ordenado = list(map(lambda t: t[0], datos_ordenados))
    Y_ordenado = list(map(lambda t: t[1], datos_ordenados))
    
    return X_ordenado, Y_ordenado

def inter_lineal(x, X, Y):
    """Interporlación lineal para hallar el punto x con dos vectores X y Y

    El vector 'X' contiene los datos de la variable independiente y el vector
    'Y' contiene los datos de la variable dependiente

    """
    
    # ORdenamos los datos
    X_ordenado, Y_ordenado = ordenar_ascendente(X,Y)
    
    def eq_int_lineal(x, x_0, y_0, x_1, y_1):
        """Ecuación de la interpolación lineal simple
        """
        return y_0 + (y_1-y_0)/(x_1-x_0) * (x-x_0)
    
    # Vemos si "x" esta en el vector X
    if (lambda x, X: x in X)(x, X):
        i = X.index(x)
        return Y[i]
    
    else:
        # Si no esta sacamos el indice mayor cercano
        i = indice_mayor_cercano(x, X)
        # con el indice utilizamos la ecución
        y = eq_int_lineal(x, X[i-1], Y[i-1], X[i], Y[i])
        return y
