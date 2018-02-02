import pandas as pd
import numpy as np

#df = pd.read_csv("fileN01_grid.txt",usecols = ['year', 'month', 'grid_id', 'nivel_mar','profundidad', 'salinidad', 'temperatura', 'esfuerzo_x',  'esfuerzo_y',  'corriente_u',  'corriente_v',  'corriente_w'])

#df.to_csv('fileNO1_filt.txt', index=False)

df = pd.read_csv("fileN01_grid.txt", usecols = ['lat','lon'])
#df = pd.read_csv("fileN01_grid.txt", usecols = ['year', 'month', 'nivel_mar','profundidad', 'salinidad', 'temperatura', 'esfuerzo_x',  'esfuerzo_y',  'corriente_u',  'corriente_v',  'corriente_w'])
#df2 = pd.read_csv("lat_lon_id.txt", usecols = ['grid_id'])
def grid(lat, lon):
    lat -= 20.25
    lon += 0.25
    lon = lon *2 - 300
    lat *= (-2)
    return int(lat *1000 + lon)



print(df.head())
#df['grid_id'] = df2['grid_id']

df['region']= df.apply(lambda x: grid(x.lat,x.lon),axis=1)
#df =  df[['year', 'month', 'grid_id', 'nivel_mar','profundidad', 'salinidad', 'temperatura', 'esfuerzo_x',  'esfuerzo_y',  'corriente_u',  'corriente_v',  'corriente_w']]
df.to_csv('lat_lon_region.txt', index=False)
print(df.head())