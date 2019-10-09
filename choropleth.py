# Import your libraries as required not all are needed*
import cufflinks as cf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import download_plotlyjs,plot,iplot,init_notebook_mode
init_notebook_mode(connected=True)
cf.go_offline()

from plotly import graph_objs as go

# Load data frame and tidy it.
# Air Quality Dataset from Kaggle 1980 - 2017
df = pd.read_csv("epa_air_quality_annual_summary.csv")
df1=df.dropna()#.head(1000)



state_codes = {
    'District of Columbia' : 'DC','Mississippi': 'MS', 'Oklahoma': 'OK',
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR',
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA',
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ',
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT',
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT',
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV',
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND',
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY',
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH',
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD',
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA',
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX',
    'Nevada': 'NV', 'Maine': 'ME'}

data=dict(type='choropleth',
         locations=list(state_codes.values()),
         # plotly does not take state names rather codes, can use fif codes with county
         locationmode='USA-states',
         colorscale='Portland',
         text="Pollutant: " + df1['parameter_name'] + '<br>' + "Year: " + df1['year'].apply(str) + \
               '<br>' + "Observation Percent: " + df1['observation_percent'].apply(str) ,
         z = df1['seventy_five_percentile'].astype(float),
         colorbar={'title':'Pollutant Concentration Index'})

layout = dict(geo={'scope':'usa'})

choromap = go.Figure(data=[data], layout=layout)

iplot(choromap)
