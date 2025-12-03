# TODO: Aquí debes escribir tu código
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Análisis Interactivo de Datos con Streamlit")
from sklearn import datasets
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
df_california = pd.DataFrame(housing.data, columns=housing.feature_names)

df_california["MedHouseVal"] = housing.target

st.write(df_california.head())

st.header("Tipos de datos de cada columna:")
st.write(df_california.dtypes)

st.sidebar.markdown("Filtros disponibles")
st.sidebar.markdown("Ajuste los filtros para explorar según Edad de Casa y Latitud mínima.")

minage = int(df_california["HouseAge"].min())
maxage = int(df_california["HouseAge"].max())

house_age_range = st.sidebar.slider("Rango de Edad Mediana de la Casa", min_value = int(df_california['HouseAge'].min()),
                                    max_value = int(df_california['HouseAge'].max()),
                                    value = (minage, maxage) )

df_filtered = df_california[(df_california["HouseAge"] >= house_age_range[0]) &
                            (df_california["HouseAge"] <= house_age_range[1]) ]
st.dataframe (df_filtered)

active_filtro = st.sidebar.checkbox("Filtrar por Latitud Mínima")

if active_filtro:
    lat_min = st.sidebar.number_input ("Latitud mínima", min_value = float(df_california["Latitude"].min()),
    max_value = float(df_california["Latitude"].max()), value = float(df_california["Latitude"].min()))

df_filtered = df_filtered[df_filtered["Latitude"] >= lat_min]

##Gráfico de Distribución del Target
st.subheader("Distribución del Valor Mediano de la Vivienda (MedHouseVal)")

fig, ax = plt.subplots()
ax.hist(df_filtered["MedHouseVal"], bins=30)
ax.set_xlabel("MedHouseVal")
ax.set_ylabel("Frecuencia")
ax.set_title("Histograma del Valor Mediano de Vivienda")

st.pyplot(fig)

## Gráfico de Dispersión (MedInc vs MedHouseVal)
st.subheader("Relación entre Ingresos y Valor de Vivienda")

fig2, ax2 = plt.subplots()
ax2.scatter(df_filtered["MedInc"], df_filtered["MedHouseVal"], alpha=0.5)
ax2.set_xlabel("Mediana de Ingresos (MedInc)")
ax2.set_ylabel("Valor Mediano de la Vivienda (MedHouseVal)")
ax2.set_title("Scatter Plot: MedInc vs MedHouseVal")

st.pyplot(fig2)

###Mapa Geográfico

st.subheader("Mapa Geográfico de Viviendas Filtradas")
df_map = df_filtered.rename(columns={"Latitude": "lat", "Longitude": "lon"})
st.map(df_map[["lat", "lon"]])
