import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt


st.title('Analyse de données : voitures')

st.header("Corrélations entre les variables")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

df_cars['continent'] = df_cars['continent'].apply(lambda x : x.replace('.', ''))


sns.set_style(style = 'darkgrid')
corr = df_cars.corr()
# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=np.bool))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
viz_correlation = sns.heatmap(corr, mask=mask, cmap=cmap, annot = True, vmax=1, vmin=-1, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.title('Heatmap des corrélations dans le dataset des voitures')
st.pyplot(viz_correlation.figure)



st.write("Les corrélations les plus fortes sont :")
st.write("   - Les variables 'cubicinches', 'hp' et weightlbs sont correlées positivement entre elles")
st.write("   - La variable 'mpg' est correlée négativement avec 'cylinders', 'cubicinches', 'hp' et 'weightlbs'")
st.write("   - La variable 'time-to-60' est correlée négativement avec 'hp'")

st.header("Distribution des données")

option = st.selectbox(
     'Choisi un continent',
     df_cars.continent.sort_values().unique())

option_2 = st.selectbox(
     'Choisi une variable',
     sorted(df_cars.select_dtypes(include=[np.number]).columns))


st.write(f"Tu vois la distribution des données de '{option_2}' pour le continent {option}")

viz_distribution = px.violin(df_cars[df_cars.continent == option], 
								x=option_2,
                                #x="year",
                                box=True,
                                orientation="h",
								)

st.plotly_chart(viz_distribution)

st.write("Les données sur les voitures sont disponibles en suivant ce lien : https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
