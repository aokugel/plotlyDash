import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('life-expectancy-vs-health-expenditure.csv')

df.dropna(subset=['Health expenditure'], inplace=True)
df.dropna(subset=['Life expectancy (years)'], inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=1970,
        max=2015,
        value=2015,
        marks={str(x): str(x) for x in range(1970, 2015, 5)},
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.Year == str(selected_year)]


    fig = px.scatter(filtered_df, 
                    x="Health expenditure", 
                    y="Life expectancy (years)", 
                    size="Population", 
                    hover_name="Entity", 
                    log_x=False, 
                    size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)