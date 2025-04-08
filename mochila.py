import random
from itertools import product

objetos = [
    {"nombre": "Cuaderno", "peso": 1.2, "valor": 15},
    {"nombre": "Lápiz", "peso": 0.1, "valor": 5},
    {"nombre": "Plumones", "peso": 2.0, "valor": 25},
    {"nombre": "Regla", "peso": 0.5, "valor": 8},
    {"nombre": "Escuadra", "peso": 1.8, "valor": 20},
    {"nombre": "Calculadora", "peso": 0.7, "valor": 35},
    {"nombre": "Compás", "peso": 0.6, "valor": 12},
    {"nombre": "Libro de texto", "peso": 3.5, "valor": 50},
    {"nombre": "Tablet", "peso": 1.3, "valor": 55},
    {"nombre": "USB", "peso": 0.2, "valor": 10},
    {"nombre": "Agenda", "peso": 0.8, "valor": 18},
    {"nombre": "Colores", "peso": 1.1, "valor": 22}
]

CAPACIDAD_MAXIMA = 6
TAMANO_POBLACION = 30
TASA_MUTACION = 0.05
GENERACIONES_LIMITE = 1000

def generar_individuo():
    return [random.randint(0, 1) for _ in range(len(objetos))]

def generar_poblacion():
    return [generar_individuo() for _ in range(TAMANO_POBLACION)]

def calcular_fitness(individuo):
    peso_total = 0.0
    valor_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso_total += objetos[i]["peso"]
            valor_total += objetos[i]["valor"]
    if peso_total > CAPACIDAD_MAXIMA:
        return 0
    return valor_total

def seleccion_ruleta(poblacion, fitnesses):
    pass

def crossover(padre1, padre2):
    pass

def mutar(individuo):
    pass