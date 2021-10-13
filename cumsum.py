import pandas as pd
import plotly.express as px

def createCumSum():
  df = pd.read_csv('data_cumsum.csv')

  fig = px.line(df, x="Datum tenaamstelling", y="cumsum", color='Brandstof', log_y=True, title='Cumulatief aantal tenaamgestelde auto\'s per brandstofsoort per maand')

  fig.update_xaxes(title='Tijd in maanden')
  fig.update_yaxes(title='Totaal tenaamgestelde auto\'s')

  return fig