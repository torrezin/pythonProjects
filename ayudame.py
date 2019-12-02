import time
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, assets_external_path='./assets/', external_stylesheets=stylesheets)

siglas_uf = ['RO', 'AC', 'AM', 'RR', 'PA',
'AP', 'TO', 'MA', 'PI', 'CE',
'RN', 'PB', 'PE', 'AL', 'SE',
'BA', 'MG', 'ES', 'RJ', 'SP',
'PR', 'SC', 'RS', 'MS', 'MT',
'GO', 'DF']
numeros_uf = [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]
codigos_uf = {numeros_uf[i]: siglas_uf[i] for i in range(0, 27)}
regioes = {
    'Norte': ['AC', 'AM', 'PA', 'RR', 'TO', 'RO', 'AP'],
    'Nordeste': ['MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA'],
    'Centro-Oeste': ['MT', 'MS', 'GO', 'DF'],
    'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
    'Sul': ['PR', 'RS', 'SC']
}

def obterRegiao(r, sigla):
    num = codigos_uf[sigla]
    for key in r:
        if num in r[key]:
            return key
    return None

def scale(x):
    return ((np.log10(2 ** x)) ** 2) + 15

xls = pd.read_excel('\\Users\\re91951z\\Documents\\Caio\\Lab\\Dados\\nasc_mortos.xlsx',encoding='utf8')
dfCesarios = pd.read_excel(xls, 0, index_col='UF')
dfHospitalares = pd.read_excel(xls, 1, index_col='Código UF')
dfMortalidade = pd.read_excel(xls, 2, index_col='UF')

dfHospitalares.index.names = ['UF']

rnDict = {
    0: 'Partos Cesários (%)',
    1: 'Partos Hospitalares (%)',
    2: 'Mortalidade (%)'
}

# I'm sorry.

dfs = []
# Cada ano, desde 2000 até 2016
for anoI in range(17):
    ano = 2000 + anoI
    dft = pd.DataFrame([dfCesarios[ano], dfHospitalares[ano], dfMortalidade[ano]]).transpose()
    dft.columns = ['Partos Cesários (%)', 'Partos Hospitalares (%)', 'Mortalidade (%)']
    dft['Região'] = dft.index
    dft['Região'] = dft['Região'].apply(lambda x: obterRegiao(regioes, x))
    dft['Sigla'] = dft.index
    dft['Sigla'] = dft['Sigla'].apply(lambda x: codigos_uf[x])
    dft['Partos Cesários (%)'] = dft['Partos Cesários (%)'].apply(lambda x: x * 100)
    dft['Partos Hospitalares (%)'] = dft['Partos Hospitalares (%)'].apply(lambda x: x * 100)
    dft['Mortalidade (%)'] = dft['Mortalidade (%)'].apply(lambda x: float('{0:.1f}'.format(x)))
    dft['Raio'] = dft['Mortalidade (%)'].apply(lambda x: scale(x))
    dft['Texto'] = dft['Sigla'] + ' - ' + dft['Mortalidade (%)'].apply(lambda x: str(x))
    dft['Ano'] = ano
    dfs.append(dft)

df = pd.concat(dfs)

app.layout = html.Div(children = [
    dcc.Graph(
        id='relacao-partos',
        figure = {
            'data': []
        }
    ),
    html.Div(id='grafico-slider', style={'width': '60%', 'margin': '0 auto', 'fontFamily': 'sans-serif', 'textAlign': 'center'}, children=[
        html.Label('Ano:'),
        dcc.Slider(
            id='ano-slider',
            min = 2000,
            max = 2016,
            marks = {
                i: str(i) for i in range(2000, 2017)
            },
            value = 2000,
        ),
        html.Br(), html.Br(),
        html.Label('Delay de transição (ms):'),
        dcc.Slider(
            id='transicao-slider',
            min=0,
            max=1000,
            marks = {
                i: str(i) + ' ms' for i in range(0, 1001, 100)
            },
            value = 500,
        ),
    ]),
])

N_CLICKS = 0

@app.callback(Output('relacao-partos', 'figure'),
                [Input('ano-slider', 'value'), Input('transicao-slider', 'value')])
def atualizarFig(slider, transic):
    figura = {
        'data': [
            go.Scatter(
                x = df[(df['Região'] == i) & (df['Ano'] == slider)]['Partos Cesários (%)'],
                y = df[(df['Região'] == i) & (df['Ano'] == slider)]['Partos Hospitalares (%)'],
                mode = 'markers+text',
                textposition = 'middle right',
                text = df[(df['Região'] == i) & (df['Ano'] == slider)]['Texto'],
                marker = {
                    'size': df[(df['Região'] == i) & (df['Ano'] == slider)]['Raio'],
                },
                name = i,
            ) for i in df['Região'].unique()
        ],
        'layout': go.Layout(
            xaxis = {
                'title': 'Partos Cesários (%)',
                'range': [0, 100],
            },
            yaxis = {
                'title': 'Partos Hospitalares',
                'range': [0, 119],
            },
            height = 700,
            hovermode = 'closest',
            transition = {
                'duration': transic,
            }
        )
    }
    return figura

if __name__ == '__main__':
    app.run_server(host='192.168.15.10',port='8050',debug=True)