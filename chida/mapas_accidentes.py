
import pandas as pd
import folium
from folium.plugins import HeatMap

# Cargar los datos
data = pd.read_csv('filtered_accidentes_EDO1_MPIO1.csv', encoding='ISO-8859-1')


# Crear un mapa centrado en las coordenadas promedio
m_heatmap = folium.Map(location=[data['LATITUD'].mean(), data['LONGITUD'].mean()], zoom_start=12)

# Convertir los datos para el heatmap
heat_data = [[row['LATITUD'], row['LONGITUD']] for index, row in data.iterrows()]

# Agregar el heatmap al mapa
HeatMap(heat_data, radius=10).add_to(m_heatmap)

# Guardar el mapa en un archivo HTML
m_heatmap.save('heatmap_accidentes_AGS.html')




import pandas as pd
import folium

grouped_data = data.groupby(['LONGITUD', 'LATITUD']).size().reset_index(name='count')

# Crear el mapa
m_grouped = folium.Map(location=[data['LATITUD'].mean(), data['LONGITUD'].mean()], zoom_start=12)

# Agregar puntos al mapa con el número de accidentes
for _, row in grouped_data.iterrows():
#    folium.Marker(
    folium.CircleMarker(
        location=(row['LATITUD'], row['LONGITUD']),
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=str(row['count'])
    ).add_to(m_grouped)

# Guardar el mapa en un archivo HTML
m_grouped.save('grouped_accidentes_map_AGS.html')



