import numpy as np
import random
import copy
import pandas as pd
import folium
from folium.plugins import HeatMap
import mapas_accidentes as ma
data = ma.data

def calcular_distancia(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def evaluar_solucion(solucion, accidentes):
    total_distancia = 0
    for ambulancia in solucion:
        distancia_minima = float('inf')
        for accidente in accidentes:
            distancia = calcular_distancia(ambulancia, accidente)
            distancia_minima = min(distancia_minima, distancia)
        total_distancia += distancia_minima
    return total_distancia


def generar_solucion_vecina(solucion, radio=0.00000000000001):

    solucion_vecina = copy.deepcopy(solucion)
    for i in range(len(solucion_vecina)):
        solucion_vecina[i][0] += random.uniform(-radio, radio)
        solucion_vecina[i][1] += random.uniform(-radio, radio)
    return solucion_vecina


def recocido_simulado(accidentes, num_ambulancias, temperatura_inicial=1000, factor_enfriamiento=0.95, num_iteraciones=1000):
    solucion_actual = [[random.uniform(min(data['LATITUD']), max(data['LATITUD'])),
                        random.uniform(min(data['LONGITUD']), max(data['LONGITUD']))] for _ in range(num_ambulancias)]
    mejor_solucion = solucion_actual
    temperatura = temperatura_inicial

    for _ in range(num_iteraciones):
        solucion_vecina = generar_solucion_vecina(solucion_actual)
        delta_evaluacion = evaluar_solucion(solucion_vecina, accidentes) - evaluar_solucion(solucion_actual, accidentes)

        if delta_evaluacion < 0 or random.uniform(0, 1) < np.exp(-delta_evaluacion / temperatura):
            solucion_actual = solucion_vecina

        if evaluar_solucion(solucion_actual, accidentes) < evaluar_solucion(mejor_solucion, accidentes):
            mejor_solucion = solucion_actual

        #print(mejor_solucion)

        temperatura *= factor_enfriamiento

    return mejor_solucion


accidentes = list(zip(data['LATITUD'], data['LONGITUD']))
solucion_optima = recocido_simulado(accidentes, num_ambulancias=16)
m_solucion = folium.Map(location=[data['LATITUD'].mean(), data['LONGITUD'].mean()], zoom_start=12)
for accidente in accidentes:
    folium.Marker(location=accidente, icon=folium.Icon(color='red')).add_to(m_solucion)

# Agregar puntos de ambulancias al mapa
for ambulancia in solucion_optima:
    folium.Marker(location=ambulancia, icon=folium.Icon(color='green')).add_to(m_solucion)

m_solucion.save('solucion_optima.html')