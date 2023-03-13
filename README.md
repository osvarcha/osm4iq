osm4iq singifica "Osvarcha's macros for Iq" que traducido es "Las
macros de osvarcha para IQ" que tiene como objetivo crear UDF's
(Funciones definidas por el Usuario) con [xlwings](https://www.xlwings.org/), una biblioteca que
enlaza python con excel, tanto para hacer macros como UDF's solo para
windows.


# Table de Cotenido     :TOC_3_ORG:

-   [Epilogo](#org3986f8a)
-   [Instalación](#org12344a4)
-   [Macros](#org6df67fe)
-   [UDF's](#org8b66ecf)
    -   [Funciones demo](#orgeb6e6f7)
    -   [Funciones num](#org78c4f54)
    -   [Complemento IQ](#org7887ac3)
        -   [Funciones necesarias para IQ](#org9e2e7af)
        -   [Calculos](#orge417394)
        -   [Coeficientes de actividad](#org8b0a6bf)
        -   [Coeficientes de Fugacidad en Mezcla](#orge29be05)
        -   [Energias de Exceso](#org73d26f2)
        -   [Energia Interna Residual](#org746f9b8)
        -   [Energia  Libre de Gibbs Residual](#org0b20fea)
        -   [Entalpía Residual](#org750c31d)
        -   [Entropía Residual](#org18196a7)
        -   [Factor de Compresibilidad](#org45c9e9e)
        -   [Operaciones Unitarias](#org1b41234)
        -   [Parámetros de EoS](#org988ef3a)
        -   [Presión](#org27ba9af)
        -   [Presión de Vapor](#org3a5f613)
        -   [Propiedades Fisicoquímicas y de Transporte](#org97f27b1)
        -   [Psicrometría](#org85cbd9d)
        -   [Trabajo de Expansión/Comprensión](#org04921c0)
        -   [Volumen Molar](#orgf3ada91)
-   [Archivo final](#org00c1584)


# Epilogo

La documentación y el codigo esta hecho en [org-mode](https://orgmode.org) tanto para
escribir las funciones de python como para autodocumentarlas a medida
que avanzo.

> [org-mode](https://orgmode.org) es una herramientas fantastica de [emacs](https://www.gnu.org/software/emacs/) es mas que un formato
> de texto plano, se usa para crar documentos, notebooks, agenda, notas,
> listas en fin es hackeable, tanto asi que todo el codigo se hara en
> este notebook que sera una autodocumentación.


# TODO Instalación

se puede esar miniconda tanto como anaconda, pero este complemento lo
hice con miniconda porque lo considero mas liviano aunque anaconda
incluye toda la paqueteria completa para el analisis de datos.

1.  Descargar una distribución de que incluya conda.
    Puede elegir [miniconda](https://docs.conda.io/en/latest/miniconda.html) o tambien la distribución completa de
    [anaconda](https://www.anaconda.com/products/distribution)
2.  Clone este repositorio
3.  Crear el entorno conda
    En el repositorio hay un archivo `environment.yml` lo cual creara
    el entorno con sus dependencias.
    
        conda env create -f environment.yml
4.  Añadir el complento a excel
    Abrir el excel, añadir el complemento `osm4iq.yml` y probarlo.


# Macros

Primero una macro basica que viene con Quickstart de xlwings

    import xlwings as xw
    
    def main():
        wb = xw.Book.caller()
        sheet = wb.sheets[0]
        if sheet["A1"].value == "Hello xlwings!":
            sheet["A1"].value = "Bye xlwings!"
        else:
            sheet["A1"].value = "Hello xlwings!"


# UDF's

Vamos a definir las UDF's


## Funciones demo

Son funciones para saludar

    import xlwings as xw
    
    @xw.func
    def hello(name):
        return f"Hello {name}!"


## Funciones num

Funciones numericas

    import xlwings as xw
    
    @xw.func
    def double_sum(x, y):
        """Returns twice the sum of the two arguments"""
        return 2 * (x + y)


## TODO Complemento IQ

Este proyecto inicio porque queria reemplazar el complemento de mi
profesor de termodinamica pero sin VBA.

> Talvez nunca complete esta lista porque solo utilizare algunas
> funciones que utilice en el curso, pero mi objetivo de este
> complemento es que sea mas utilice las bondades de python con sus 
> paqueterias como añadir [SymPy](https://www.sympy.org/es/) para calculo simbolico ejecutados desde
> la cinta de opciones, asi como [numpy](https://numpy.org/) para calculo matematico, y
> algunos complementos se optimizaran con [numba](https://numba.pydata.org_quot).


### TODO Funciones necesarias para IQ

Estas funciones son necesarias para todo IQ pues son ecuaciones matematicas
representadas en funciones.

1.  TODO Interporlación

    La Interpolación lineal es una tecnica rapida para calculos que son cercanos
    especialmente si se usa en tablas porque son datos cercanos y con poco error
    experimental. La siguiente ecuación representa representa la función a crear.
    
    \begin{equation}
    f_1\left ( x \right ) = f\left ( x_0 \right ) + \frac{f\left ( x_1 \right ) -
    f\left ( x_0 \right )}{x_1 - x_0}\left ( x - x_0 \right )
    \end{equation}
    
        def inter_lineal(x, X, Y):
            """Interporlación lineal con dos vectores de datos y el valor a interpolar"""
            pass


### TODO Calculos


### TODO Coeficientes de actividad


### TODO Coeficientes de Fugacidad en Mezcla


### TODO Energias de Exceso


### TODO Energia Interna Residual


### TODO Energia  Libre de Gibbs Residual


### TODO Entalpía Residual


### TODO Entropía Residual


### TODO Factor de Compresibilidad


### TODO Operaciones Unitarias


### TODO Parámetros de EoS


### TODO Presión


### TODO Presión de Vapor


### TODO Propiedades Fisicoquímicas y de Transporte


### TODO Psicrometría


### TODO Trabajo de Expansión/Comprensión


### TODO Volumen Molar


# Archivo final

    import xlwings as xw
    
    # Funciones a importar
    from package.macros.main import main
    from package.funciones.demo import hello, hola_mundo
    from package.funciones.num import double_sum
    
    if __name__ == "__main__":
        xw.Book("osm4iq.xlsm").set_mock_caller()
        main()

