import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
df = pd.read_csv("income.csv")

app.layout = html.Div([
   html.H1("State Economic Metrics", style={'text-align': 'center'}),
   html.H4("Based on 2014 data", style={'text-align': 'center'}),
   html.Label('Select Data Metric: '),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Per Capita Income', 'value': 'Per Capita Income'},
            {'label': 'Median Household Income', 'value': 'Median Household Income'},
            {'label': 'Median Family Income', 'value': 'Median Family Income'},
        ],
        value='Median Household Income'
    ),
    dcc.Graph(
        id='state-economics',

    )
])

@app.callback(
    Output('state-economics', 'figure'),
    [Input('metric-dropdown', 'value')])
def update_figure(selected_metric):

   fig = px.choropleth(df, locationmode='USA-states', 
                        locations='state_code', 
                        color=selected_metric,
                        hover_name='State or Territory',
                        hover_data=[selected_metric],
                        color_continuous_scale="Viridis",
                        scope="usa",)

   fig.update_layout(
      margin=dict(l=30, r=30, t=30, b=30),
   )

   return fig

if __name__ == '__main__':
    app.run_server(debug=True)

    
