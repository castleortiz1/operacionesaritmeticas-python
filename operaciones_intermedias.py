def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    else:
        return "Error: Raíz cuadrada de número negativo no permitida"

def modulo(a, b):
    return a % b

def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: División por cero no permitida"
