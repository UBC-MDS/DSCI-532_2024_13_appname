from dash import Dash, dcc, callback, Output, Input, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt
import pandas as pd
import plotly.graph_objs as go

from data import df
import callbacks
from components import title, global_widgets, card_women, card_men, industry, line_chart, barchart, barchart2, map
# Adding new components in a new line so it is easier to isolate anything new which might be causing problems
from components import dataset_description, collapse_button, collapse_section, card_ratio
from dash import State

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(title, style={"margin-top": "5px",
                              'backgroundColor': '#800080', 
                              'padding': 20, 'color': 'white'}, 
                              className="text-center"),
    ]),
    dbc.Col(html.Div(collapse_button), className="text-center"),
    dbc.Row([
        dbc.Col(collapse_section, style={"margin-top": "10px"})
    ]),
    dbc.Row(dbc.Col(dataset_description, style={"margin-top": "10px"})),
    dbc.Row([
        dbc.Col([
                dbc.Card([dbc.Col(industry), dbc.Col(card_women), dbc.Col(card_men), dbc.Col(card_ratio)], style={
        'background-color': '#F5F5F5',
        'padding': 15,
        'border-radius': 3,
        'width':'80%',
        'margin-bottom': '20px'
    }, ),
                dbc.Row(dbc.Col(global_widgets, width=6)),
            ],
            sm= "5",
        ), 
        dbc.Col([dvc.Vega(id="map",opt = {"rendered":"svg", "actions":False})], width = 1), 
    ]), 
    dbc.Row([dbc.Col(dvc.Vega(id='line-chart'))]),
    dbc.Row([dbc.Col(dcc.Graph(id='bar-chart')), dbc.Col(dcc.Graph(id='bar2-chart'))]),
    html.Footer([
        html.P(''),
        html.Hr(),       
        html.P('Last updated on April 13, 2024.', style={'font-size': '12px', 'margin-bottom': '10px'}),
        html.A('The source code can be found on GitHub.', href='https://github.com/UBC-MDS/DSCI-532_2024_13_Juno', style={'font-size': '14px', 'margin-bottom': '10px'})
    ]),

])

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = 8052)