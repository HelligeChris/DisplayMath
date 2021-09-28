from sympy import latex
from IPython.display import display, Math

def displayMath(text, value = ""):
    if type(value) != list:
        value = [value]
    res = ""
    for i in value:
        if type(i) != list:
            res += f"{latex(i)}"
        else:
            res += i[0]
    display(Math(text + res))