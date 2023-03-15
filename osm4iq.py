import xlwings as xw

# Funciones a importar
from package.macros.main import main
from package.funciones.demo import hello, hola_mundo
from package.funciones.num import double_sum

if __name__ == "__main__":
    xw.Book("osm4iq.xlsm").set_mock_caller()
    main()
