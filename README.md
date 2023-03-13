osm4iq singifica "Osvarcha's macros for Iq" que traducido es "Las
macros de osvarcha para IQ" que tiene como objetivo crear UDF's
(Funciones definidas por el Usuario) con [xlwings](https://www.xlwings.org/), una biblioteca que
enlaza python con excel, tanto para hacer macros como UDF's solo para
windows.


# Table de Cotenido     :TOC_3_ORG:

-   [Epilogo](#org899be96)
-   [Instalaci�n](#org00fbda2)
-   [Macros](#orgc616fb3)
-   [UDF's](#org3988963)
    -   [Funciones demo](#org87d74c3)
    -   [Funciones num](#org14f889e)
    -   [Complemento IQ](#org98a2eac)
        -   [Funciones necesarias para IQ](#orgde8e76a)
        -   [Calculos](#org56483fe)
        -   [Coeficientes de actividad](#org7c30a65)
        -   [Coeficientes de Fugacidad en Mezcla](#org434d0f1)
        -   [Energias de Exceso](#org849228b)
        -   [Energia Interna Residual](#org4c4a8f0)
        -   [Energia  Libre de Gibbs Residual](#orga7f4eef)
        -   [Entalp�a Residual](#orgd00a7cb)
        -   [Entrop�a Residual](#orge7f4e08)
        -   [Factor de Compresibilidad](#org8691479)
        -   [Operaciones Unitarias](#org7456e97)
        -   [Par�metros de EoS](#org3aa6e8d)
        -   [Presi�n](#org14e2e2d)
        -   [Presi�n de Vapor](#orgf114e7a)
        -   [Propiedades Fisicoqu�micas y de Transporte](#org503161b)
        -   [Psicrometr�a](#org77f8c29)
        -   [Trabajo de Expansi�n/Comprensi�n](#orgefc7434)
        -   [Volumen Molar](#orgaf19fe2)
-   [Archivo final](#org3889e8d)


# Epilogo

La documentaci�n y el codigo esta hecho en [org-mode](https://orgmode.org) tanto para
escribir las funciones de python como para autodocumentarlas a medida
que avanzo.

> [org-mode](https://orgmode.org) es una herramientas fantastica de [emacs](https://www.gnu.org/software/emacs/) es mas que un formato
> de texto plano, se usa para crar documentos, notebooks, agenda, notas,
> listas en fin es hackeable, tanto asi que todo el codigo se hara en
> este notebook que sera una autodocumentaci�n.


# TODO Instalaci�n

se puede esar miniconda tanto como anaconda, pero este complemento lo
hice con miniconda porque lo considero mas liviano aunque anaconda
incluye toda la paqueteria completa para el analisis de datos.

1.  Descargar una distribuci�n de que incluya conda.
    Puede elegir [miniconda](https://docs.conda.io/en/latest/miniconda.html) o tambien la distribuci�n completa de
    [anaconda](https://www.anaconda.com/products/distribution)
2.  Clone este repositorio
3.  Crear el entorno conda
    En el repositorio hay un archivo `environment.yml` lo cual creara
    el entorno con sus dependencias.
    
        conda env create -f environment.yml
4.  A�adir el complento a excel
    Abrir el excel, a�adir el complemento `osm4iq.yml` y probarlo.


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
> paqueterias como a�adir [SymPy](https://www.sympy.org/es/) para calculo simbolico ejecutados desde
> la cinta de opciones, asi como [numpy](https://numpy.org/) para calculo matematico, y
> algunos complementos se optimizaran con [numba](https://numba.pydata.org_quot).


### TODO Funciones necesarias para IQ

Estas funciones son necesarias para todo IQ pues son ecuaciones matematicas
representadas en funciones.

1.  TODO Interporlaci�n

    La Interpolaci�n lineal es una tecnica rapida para calculos que son cercanos
    especialmente si se usa en tablas porque son datos cercanos y con poco error
    experimental. La siguiente ecuaci�n representa representa la funci�n a crear.
    
    $$
    f_1\left ( x \right ) = f\left ( x_0 \right ) + \frac{f\left ( x_1 \right ) -
    f\left ( x_0 \right )}{x_1 - x_0}\left ( x - x_0 \right )
    $$
    
        def inter_lineal(x, X, Y):
            """Interporlaci�n lineal con dos vectores de datos y el valor a interpolar"""
            pass


### TODO Calculos


### TODO Coeficientes de actividad


### TODO Coeficientes de Fugacidad en Mezcla


### TODO Energias de Exceso


### TODO Energia Interna Residual


### TODO Energia  Libre de Gibbs Residual


### TODO Entalp�a Residual


### TODO Entrop�a Residual


### TODO Factor de Compresibilidad


### TODO Operaciones Unitarias


### TODO Par�metros de EoS


### TODO Presi�n


### TODO Presi�n de Vapor


### TODO Propiedades Fisicoqu�micas y de Transporte


### TODO Psicrometr�a


### TODO Trabajo de Expansi�n/Comprensi�n


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

