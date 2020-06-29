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
fg = folium.FeatureGroup(name="my Map")
for lati, long, elev, name in zip(lat,lon,el,name):
    iFrame = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fg.add_child(folium.Marker(location=[lati, long], popup=folium.Popup(iFrame), icon=folium.Icon(color=colorize(elev))))
map1.add_child(fg)

map1.save('map1.html')
