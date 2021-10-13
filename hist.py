import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def createHist():
  df = pd.read_csv('laadpaaldata.csv')

  mean = df['ChargeTime'].mean()
  median = df['ChargeTime'].median()

  fig = px.histogram(df, x= 'ChargeTime', range_x=[0,15], nbins=2000, title='Histogram oplaadtijd in uren van elektrische auto\'s')

  fig.update_xaxes(dtick=.5)
  fig.update_xaxes(title='Oplaadtijd in uren')
  fig.update_xaxes(fixedrange=True)
  fig.update_yaxes(title='Aantal')
  fig.update_yaxes(fixedrange=True)
  fig.update_layout(showlegend=False)

  fig.add_shape(type="line",
    x0=mean, y0=0, x1=mean, y1=1900,
    line=dict(color="Black",width=3)
  )

  fig.add_shape(type="line",
    x0=median, y0=0, x1=median, y1=1800,
    line=dict(color="Black",width=3)
  )

  fig.add_trace(go.Scatter(
    x=[3.5],
    y=[1900],
    text=["Gemiddelde laadtijd"],
    mode="text")
  )

  fig.add_trace(go.Scatter(
    x=[3.7],
    y=[1800],
    text=["Mediaan laadtijd"],
    mode="text")
  )

  return fig