import folium
import pandas

data = pandas.read_csv('Volcanoes_USA.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def color_procidure(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 2500:
        return 'yellow'
    else:
        return 'red'


map = folium.Map(location=[38.5937, -90.9629], zoom_start=6, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + "m",
                                      fill_color=color_procidure(el), color='gray', fill_Opacity=0.7))

fgp = folium.FeatureGroup(name='population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'red' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'yellow'}))

map.add_child(fgv)

map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
