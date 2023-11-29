
import numpy as np
import random
import copy
import pandas as pd
import folium
from folium.plugins import HeatMap
import mapas_accidentes as ma
from sklearn.cluster import KMeans
data = ma.data


data = pd.read_csv('filtered_accidentes_EDO1_MPIO1.csv', encoding='ISO-8859-1')

m_solucion = folium.Map(location=[data['LATITUD'].mean(), data['LONGITUD'].mean()], zoom_start=12)

heat_data = [[row['LATITUD'], row['LONGITUD']] for index, row in data.iterrows()]

HeatMap(heat_data, radius=10).add_to(m_solucion)

accidentes = list(zip(data['LATITUD'], data['LONGITUD']))
solucion_optima = [
[21.8884667521488,-102.277712208393],
[21.8870303716242,-102.302542999298],
[21.8630939806027,-102.294565160091],
[21.8606529677169,-102.261647752538],
[21.9004580369436,-102.250530925034],
[21.8754320256285,-102.323391696023],
[21.8830783540132,-102.239458094067],
[21.9307562324488,-102.284518682626],
[21.9026746262807,-102.327925541264],
[21.8349018650047,-102.274712064425],
[21.9227239041612,-102.31585487846],
[21.9254670675307,-102.247273764821],
[21.8792914263936,-102.345202979211],
[21.8634360455092,-102.222687583108],
[21.8351054897873,-102.239572330219],
[21.947237090806,-102.265928653423],
[21.9050590500857,-102.218844305078]
]


for ambulancia in solucion_optima:
    folium.Marker(location=ambulancia, icon=folium.Icon(color='green')).add_to(m_solucion)

m_solucion.save('solucion_optima.html')