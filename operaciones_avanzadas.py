import math

def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    return math.tan(math.radians(angulo))

def logaritmo(base, numero):
    if base > 0 and base != 1 and numero > 0:
        return math.log(numero, base)
    else:
        return "Error: Base o número inválido para el logaritmo"
