#%%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sao-paulo-properties-april-2019.csv')

df_rent = df[df["Negotiation Type"]=="rent"]
df_sale = df[df["Negotiation Type"]=="sale"]
px.set_mapbox_access_token(open("mapbox_token.txt").read())
#%%
display(df_sale)
#%%

fig = px.scatter_mapbox(df_sale, lat="Latitude", lon="Longitude", color="Price", size="Size",
color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, opacity=0.3)

fig.update_coloraxes(colorscale = [[0, 'rgb(166, 206, 277, 0.5)'],
                        [0.02, 'rgb(31,120,180, 0.5)'],
                        [0.05, 'rgb(178,223,138, 0.5)'],
                        [0.10, 'rgb(51,160,44, 0.5)'],
                        [0.15, 'rgb(251,154,153, 0.5)'],
                        [1, 'rgb(227,26,28, 0.5)'],
                        ],
                    )

fig.update_layout(height=800, mapbox=dict(center=go.layout.mapbox.Center(lat=-23.543138, lon=-46.69486)), template="plotly_dark")
fig.show()

#%%
df_rent.describe()
# %%
