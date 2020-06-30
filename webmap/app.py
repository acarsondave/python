import folium
import pandas

data = pandas.read_csv("original.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
el = list(data["ELEV"])
name = list(data["NAME"])

html = """Volcano name:<br> <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m """

def colorize(elvation_pass):
    if elvation_pass < 1000:
        return "blue"
    elif elvation_pass >= 1000 and elvation_pass < 3000:
        return "orange"
    else:
        return "red"

map1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='Stamen Terrain')
fgvolc = folium.FeatureGroup(name="Volcanoes")
for lati, long, elev, name in zip(lat,lon,el,name):
    iFrame = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fgvolc.add_child(folium.Marker(location=[lati, long], popup=folium.Popup(iFrame), icon=folium.Icon(color=colorize(elev))))

fgpop = folium.FeatureGroup(name="Population")
fgpop.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map1.add_child(fgvolc)
map1.add_child(fgpop)
map1.add_child(folium.LayerControl())

map1.save('map1.html')
