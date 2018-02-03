import pandas as pd
import numpy as np

df = pd.read_csv("data_final.txt")




for x in range(0, 5):
    year_ini = 1870 + x*30
    year_fin = year_ini + 30
    dfx = df[(df['year'] <= year_fin) & (df['year'] > year_ini)]
    dfy = dfx.groupby(['month'])
    for group, month_df in dfy:

        prom = month_df[['temperatura']][month_df['region'] == 12].mean()
        prom = float(prom)
        df.loc[(df['year'] <= year_fin) & (df['year'] > year_ini) & (df['region'] == 12) & (df['month'] == group), ['anom_temp']] = df['temperatura'] - prom

        prom = month_df[['temperatura']][month_df['region'] == 40].mean()
        prom = float(prom)
        df.loc[(df['year'] <= year_fin) & (df['year'] > year_ini) & (df['region'] == 40) & (df['month'] == group), ['anom_temp']] = df['temperatura'] - prom

        prom = month_df[['temperatura']][month_df['region'] == 43].mean()
        prom = float(prom)
        df.loc[(df['year'] <= year_fin) & (df['year'] > year_ini) & (df['region'] == 43) & (df['month'] == group), [
            'anom_temp']] = df['temperatura'] - prom

        prom = month_df[['temperatura']][month_df['region'] == 34].mean()
        prom = float(prom)
        df.loc[(df['year'] <= year_fin) & (df['year'] > year_ini) & (df['region'] == 34) & (df['month'] == group), [
            'anom_temp']] = df['temperatura'] - prom

        prom = month_df[['temperatura']][month_df['region'] == 30].mean()
        prom = float(prom)
        df.loc[(df['year'] <= year_fin) & (df['year'] > year_ini) & (df['region'] == 30) & (df['month'] == group), [
            'anom_temp']] = df['temperatura'] - prom


df = df.round(2)

df.to_csv('data_final.txt',index=False)



