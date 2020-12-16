# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from Projections.countyCloro import figCholoro
from Projections.countyVoterRegistration import figBarRegisteredVoters
from Projections.totalVoteBar import figTotalVotesCounty

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

figCholoro.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    geo=dict(bgcolor= 'rgba(0,0,0,0)')),

figBarRegisteredVoters.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

figTotalVotesCounty.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='North Carolina Vote Dashboard', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div(children='''
        Made by: Alexander Gjurich, Jake Ballenger, Hunter Turner
    ''', style={'textAlign': 'center', 'color': colors['text']}),


    html.H1(children='Vote Results by County in North Carolina',style={'textAlign': 'center', 'color': colors['text']}),

    dcc.Graph(
        id='map-graph',
        figure=figCholoro
    ),

    html.Hr(),
    html.Br(),

    html.H1(children='Total Registered Votes by County',
            style={'textAlign': 'center', 'color': colors['text']}),

    dcc.Graph(
        id='voters-in-each-county-barchart',
        figure=figBarRegisteredVoters
    ),

    html.Hr(),

    html.H1(children='Total Votes Per Race by County',
            style={'textAlign': 'center', 'color': colors['text']}),

    dcc.Graph(
        id='total-votes-by-county',
        figure=figTotalVotesCounty
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)