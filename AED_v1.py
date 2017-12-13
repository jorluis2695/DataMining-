
# coding: utf-8

# # Análisis Exploratorio de Datos 

# ## Descripción del Dataset 

# Las entidades cientificas realizan diversos estudios enfocados en las condiciones del oceano en especial las anomalías climáticas que conllevan presencia de eventos extremos con grandes impactos a los paises de la región de América. La NOAA a traves de su servicio de información pone a disposición de las organizaciones información de las variables climatológicas con el fin de generar insights sobre el comportamiento del oceano. 
# 
# A traves del Satélite XYZ, se realizó la recolección de información de variables superficiales y hasta los 317 metros de profundidad del oceano Pacífico entre los +-30 grados de longitud y latitud con temporabilidad mensual centrado a los 17 días de cada mes desde XXXX a YYYY años 
# 
# Las variables que se obtuvieron son: 
#   *tp* - temperatura.
#   *sa* - salinidad.
#   *u*  - corriente zonal.
#   *v*  - corriente meridional.
#   *w*  - corriente vertical.
#   *n*  - profundidad.
# 
# Adicionalmente se tienen los datos a nivel supervicial:
#   *sl* - nivel del mar.
#   *tx* - esfuerzo superficial del viento en x.
#   *ty* - esfuerzo superficial del viento en y
# 
# Para mayor detalle, se tiene la descripción de la metadata en el link: http://apdrc.soest.hawaii.edu/dods/public_data/SODA/soda_pop2.2.4.info
# http://apdrc.soest.hawaii.edu/datadoc/soda_2.2.4.php

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator, WeekdayLocator
from matplotlib.dates import date2num
from pylab import rcParams
import plotly 
import plotly.plotly as py
import seaborn as sns
from datetime import datetime, timedelta


# In[2]:


df =pd.read_csv("fileN01.txt",
                sep=",",names=["lon","lat","tiempo", "profundidad","salinidad","nivel_mar","temperatura","esfuerzo_x","esfuerzo_y",
                               "corriente_u","corriente_v","corriente_w"])


# ## Análisis Descriptivo

# In[11]:


len(df)


# In[15]:


df.describe()


# In[71]:


#campos que se encuentran con missing values
df.isnull().sum().sum()


# In[74]:


print("salinidad: %s"% df.salinidad.isnull().sum())


# In[76]:


print ("Missing Values salinidad: %s" %  df.salinidad.isnull().sum())
print ("Missing Values Temperatura: %s" %  df.temperatura.isnull().sum())
print ("Missing Values nivel del mar: %s" %  df.nivel_mar.isnull().sum())
print ("Missing Values Esfuerzo del viento en X: %s" % df.esfuerzo_x.isnull().sum())
print ("Missing Values Esfuerzo del viento en Y: %s" % df.esfuerzo_y.isnull().sum())
print ("Missing Values Corriente u: %s" %  df.corriente_u.isnull().sum())
print ("Missing Values Corriente v: %s" %  df.corriente_v.isnull().sum())
print ("Missing Values Corriente w: %s" %  df.corriente_w.isnull().sum())


# In[4]:


df2 = df.head(100)


# ## Análisis Univariado y Multivariado

# In[77]:


plt.close()
sns.set_style("whitegrid")
f, axes = plt.subplots(4,2,figsize=(7,7), sharey=False)
sns.kdeplot(df['salinidad'],shade= True, ax=axes[0,0])
sns.kdeplot(df['temperatura'],shade= True, ax=axes[0,1])
sns.kdeplot(df['nivel_mar'],shade= True, ax=axes[1,0])
sns.kdeplot(df['esfuerzo_x'],shade= True, ax=axes[1,1])
sns.kdeplot(df['esfuerzo_y'],shade= True, ax=axes[2,0])
sns.kdeplot(df['corriente_u'],shade= True, ax=axes[2,1])
sns.kdeplot(df['corriente_v'],shade= True, ax=axes[3,0])
sns.kdeplot(df['corriente_w'],shade= True, ax=axes[3,1])
plt.tight_layout()
sns.plt.show()


# ## Estratificación y Discretización

# ## Análisis Geográfico

# In[32]:


def grid(lat, lon):
    lat -= 20.25
    lon += 0.25
    lon = lon *2
    lon = 581 -lon
    lat *= (-2)
    return lat *1000 + lon


# In[43]:


df2=df.sample(frac=0.000005)

df2['grid_id']= df2.apply(lambda x: grid(x.lat,x.lon),axis=1)
df2.head()


# In[48]:


#script para etiquetado de grid
df['grid_id']= df.apply(lambda x: grid(x.lat,x.lon),axis=1)


# In[46]:


# script para generación de archivo. 
df.to_csv("fileN01_etq.txt")


# ## Análisis Temporal

# In[6]:




#python_datetime = datetime.fromordinal(int(matlab_datenum)) + timedelta(days=matlab_datenum%1) - timedelta(days = 366)

def valorfecha(x, fr):
    p_datetime =  datetime.fromordinal(int(x)) + timedelta(days=x%1) - timedelta(days = 366)
    if fr=="y":
        return p_datetime.year
    if fr=="m":
        return p_datetime.month





# In[12]:


# columna de años
df['year']=df['tiempo'].apply(lambda x: valorfecha(x,"y"))


# In[14]:


# columna de mes
df['month']=df['tiempo'].apply(lambda x: valorfecha(x,"m"))


# In[47]:


df.head(10)


# In[78]:


df.head(5)


# In[ ]:


df.to_csv("fileN01_grid.txt")


# In[ ]:





# In[ ]:




