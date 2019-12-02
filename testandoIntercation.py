import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')


df_ac = pd.read_csv('/home/wdnfywaa/Desktop/tiagoFDP/Dados-AC.csv')
df_es = pd.read_csv('/home/wdnfywaa/Desktop/tiagoFDP/Dados-ES.csv')
df_rn = pd.read_csv('/home/wdnfywaa/Desktop/tiagoFDP/Dados-RN.csv')
##------------------ACRE---------------------
df_morteNeonatal_AC=df_ac[:]
df_morteNeonatal_AC['year_death'] = df_morteNeonatal_AC['year_death'].astype('Int64')
df_morteNeonatal_AC=df_morteNeonatal_AC[df_morteNeonatal_AC["morte_menor_28d"] == 1]
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 'M','n_sg_sexo'] = 1
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 'F','n_sg_sexo'] = 2
df_morteNeonatal_AC['n_sg_sexo']=df_morteNeonatal_AC['n_sg_sexo'].astype(int)

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 1,'n_tp_raca_cor_mae'] = 'maes_brancas'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 2,'n_tp_raca_cor_mae'] = 'maes_negras'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 3,'n_tp_raca_cor_mae'] = 'maes_asiaticas'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 4,'n_tp_raca_cor_mae'] = 'maes_pardas'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_raca_cor_mae == 5,'n_tp_raca_cor_mae'] = 'maes_indigenas'

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 1,'n_tp_ocorrencia'] = 'hospital'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 2,'n_tp_ocorrencia'] = 'other_health_establishment'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 3,'n_tp_ocorrencia'] = 'residence'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_tp_ocorrencia == 4,'n_tp_ocorrencia'] = 'other'
##------------------ACRE---------------------
##----------------- Indicadores -------------
available_indicators = df['Indicator Name'].unique()

available_indicators_peso = df_morteNeonatal_AC['n_nu_peso'].unique()
available_indicators_idade_mae = df_morteNeonatal_AC['n_ct_idade'].unique()
available_indicators_cor_mae = df_morteNeonatal_AC['n_tp_raca_cor_mae'].unique()
available_indicators_tipo_de_parto = df_morteNeonatal_AC['n_tp_ocorrencia'].unique()
##----------------- Indicadores -------------

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            ),
            dcc.Dropdown(
                id='xaxis-column2',
                options=[{'label': i, 'value': i} for i in available_indicators_cor_mae],
                value='maes_brancas'
            ),
            dcc.RadioItems(
                id='xaxis-type2',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            ),
            dcc.Dropdown(
                id='yaxis-column2',
                options=[{'label': i, 'value': i} for i in available_indicators_tipo_de_parto],
                value='residence'
            ),
            dcc.RadioItems(
                id='yaxis-type2',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),
    dcc.Graph(id='indicator-graphic2'),

    dcc.Slider(
        id='year--slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
    ),
    dcc.Slider(
        id='year--slider2',
        min=df_morteNeonatal_AC['year_death'].min(),
        max=df_morteNeonatal_AC['year_death'].max(),
        value=df_morteNeonatal_AC['year_death'].max(),
        marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
        step=None
    )
])


# @app.callback(
#     Output('indicator-graphic2', 'figure'),
#     [Input('xaxis-column2', 'value'),
#      Input('yaxis-column2', 'value'),
#      Input('xaxis-type2', 'value'),
#      Input('yaxis-type2', 'value'),
#      Input('year--slider2', 'value')])
# def update_graph2(xaxis_column_name, yaxis_column_name,
#                  xaxis_type2, yaxis_type2,
#                  year_value2):
#     dff2 = df_morteNeonatal_AC[df_morteNeonatal_AC['year_death'] == year_value2]
#     

#     return {
#         'data': [dict(
#             x=available_indicators_peso,
#             y=dff2[dff2['Indicator Name'] == yaxis_column_name]['Value'],

#             aux=df_morteNeonatal_AC[df_morteNeonatal_AC['year_death']==year_value2]
#             aux=df_morteNeonatal_AC[df_morteNeonatal_AC['year_death']==year_value2]

#             text=dff2[dff2['Indicator Name'] == yaxis_column_name]['Country Name'],
#             mode='markers',
#             marker={
#                 'size': 15,
#                 'opacity': 0.5,
#                 'line': {'width': 0.5, 'color': 'white'}
#             }
#         )],
#         'layout': dict(
#             xaxis={
#                 'title': xaxis_column_name,
#                 'type': 'linear' if xaxis_type2 == 'Linear' else 'log'
#             },
#             yaxis={
#                 'title': yaxis_column_name,
#                 'type': 'linear' if yaxis_type2 == 'Linear' else 'log'
#             },
#             margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
#             hovermode='closest'
#         )
#     }

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    return {
        'data': [dict(
            x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(host='192.168.15.10',port='8050',debug=True)