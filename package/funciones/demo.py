import xlwings as xw

@xw.func
def hola_mundo():
    """Hola mundo p papa"""
    return "hola Mundo"

@xw.func
def hello(name):
    return f"Hello {name}!"
