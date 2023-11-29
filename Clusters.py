import pandas as pd
import folium
from folium.plugins import HeatMap
from sklearn.cluster import KMeans

# Cargar los datos
data = pd.read_csv('filtered_accidentes_EDO1_MPIO1.csv', encoding='ISO-8859-1')

# Obtener las coordenadas de los accidentes
coordenadas_accidentes = data[['LATITUD', 'LONGITUD']].values

# Utilizar KMeans para agrupar los accidentes en k clusters
k = 16  # Puedes ajustar este valor según tu necesidad
kmeans = KMeans(n_clusters=k, random_state=42).fit(coordenadas_accidentes)
data['cluster'] = kmeans.labels_

# Calcular el centroide de cada cluster
centroides_clusters = []
for i in range(k):
    accidentes_en_cluster = coordenadas_accidentes[data['cluster'] == i]
    centroide_cluster = accidentes_en_cluster.mean(axis=0)
    centroides_clusters.append(centroide_cluster)

# Imprimir los centroides de los clusters
print("Centroides de los clusters:")
for i, centroide in enumerate(centroides_clusters):
    print(f"Cluster {i + 1}: {centroide}")

# Crear un mapa centrado en el centroide del primer cluster
m_mapa_clusters = folium.Map(location=centroides_clusters[0], zoom_start=12)

# Mostrar el mapa con los accidentes y los centroides de los clusters
HeatMap(coordenadas_accidentes, radius=10).add_to(m_mapa_clusters)
for i, centroide in enumerate(centroides_clusters):
    folium.Marker(location=centroide, popup=f'Cluster {i + 1}').add_to(m_mapa_clusters)

# Guardar el mapa en un archivo HTML
m_mapa_clusters.save('mapa_clusters.html')