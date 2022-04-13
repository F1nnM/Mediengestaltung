import imp
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#st.set_page_config(layout="wide")

data = pd.DataFrame([
  {
    "Bundesland": country,
    "Bartwuchs": bart,
    "Anzahl": col.slider(f"{country} {bart}", 0, 10),
  }
for bart in ["Bart", "Bartlos"] for country,col in zip(["Bayern", "BW", "Hessen", "NRW"], st.columns(4))])

# generate plotly scatterplot. X is the country, Y is the Bart/Bartlos category, size is the value
fig = px.scatter(data, x="Bundesland", y="Bartwuchs", size="Anzahl", color="Anzahl", opacity=1)
fig.update_layout(height=300)
st.plotly_chart(fig)