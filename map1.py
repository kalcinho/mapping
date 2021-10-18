import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#changing color of the marker according to Volcanoes hights
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

#feature group for Volcanoes
fgv = folium.FeatureGroup(name = "Volcanoes")

#using zip function for parallel iteration and setting circle marker color
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m",
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))

#feature group for Population
fgp = folium.FeatureGroup(name = "Population")

#adding json map and poligon layer, and using lambda coloring countries depending of their population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10_000_000
else 'orange' if 10_000_000 <= x['properties']['POP2005'] < 20_000_000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
