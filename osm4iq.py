import xlwings as xw

# Funciones a importar
from package.macros.main import main
from package.udf.demo import hello
from package.udf.num import double_sum

if __name__ == "__main__":
    xw.Book("osm4iq.xlsm").set_mock_caller()
    main()
