from functools import reduce

# funciones anexas
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

def inter_polinewton(x, X, Y):
    """Interporlación mediante el polinomio de Newton por diferencias
    divididas
    """
    # ordenando datos
    X, Y = ordenar_ascendente(X,Y)
    
    # Tamaño del vector
    n = len(X)
    
    # Función de diferencia divididas
    def diff_div(i, j):
        if i == j:
            return Y[i]
        elif j - i == 1:
            return (Y[j] - Y[i]) / (X[j] - X[i])
        else:
            return (diff_div(i+1, j) - diff_div(i, j-1)) / (X[j] - X[i])

    # Calcular las diferencias divididas 
    diferencias_divididas = list(map(lambda i: diff_div(i, n-1, X, Y), range(n)))

    
    # Calcular el polinomio de interpolación
    def polinomio(i):
        
        # funciones lambda adicionales para separar los cálculos
        x_minus_X = lambda k: x - X[k]
        multiplicacion_terminos = lambda lista: reduce(lambda a, b: a*b, lista)
        
        #terminos = [
        #    (diferencias_divididas[j] if j == 0 else
        #     reduce(lambda a, b: a*b, list(map(lambda k: x_minus_X(k), range(j)))) * diferencias_divididas[j])
        #    for j in range(i+1)
        #]
        
        terminos = list(
            map(lambda j: diferencias_divididas[j] if j == 0 else
                multiplicacion_terminos(list(map(x_minus_X, range(j)))) * diferencias_divididas[j],
                range(i+1))
        )
        
        return reduce(lambda a, b: a+b, terminos)
    
    return polinomio(n-1)
