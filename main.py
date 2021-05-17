import folium
import pandas as pd

df = pd.read_excel('./Data/Fallout 4 YOLO Everything.xlsx', sheet_name=6, usecols=[12, 13, 14, 15], header=None, skiprows=[0])
df.columns = ['X', 'Y', 'Location', 'Episode']

basemap = folium.Map(crs='Simple', zoom_start=4, tiles=None)
bounds = [[0,0], [1000, 1000]]
f4_overlay = folium.raster_layers.ImageOverlay('https://nerdist.com/wp-content/uploads/2015/11/Fallout-4-Map.png',
                                               bounds=bounds,
                                               zindex=1)
f4_overlay.add_to(basemap)

basemap.fit_bounds(bounds)
basemap.save('index.html')