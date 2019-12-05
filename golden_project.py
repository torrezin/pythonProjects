import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')


df_ac = pd.read_csv('Dados-AC.csv')
df_es = pd.read_csv('Dados-ES.csv')
df_rn = pd.read_csv('Dados-RN.csv')
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

df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 1,'n_sg_sexo'] = 'Homem'
df_morteNeonatal_AC.loc[df_morteNeonatal_AC.n_sg_sexo == 2,'n_sg_sexo'] = 'Mulher'

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
        dcc.Tabs(id="tabs", value='tab-2', children=[
            dcc.Tab(label='Número de óbitos por peso, cor da mãe, ano, local de nascença', value='tab-1', children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='xaxis-column2',
                            options=[{'label': i, 'value': i} for i in available_indicators_cor_mae],
                            value='maes_pardas'
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
                            id='yaxis-column2',
                            options=[{'label': i, 'value': i} for i in available_indicators_tipo_de_parto],
                            value='hospital'
                        ),
                        dcc.RadioItems(
                            id='yaxis-type2',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
                ]),
                dcc.Graph(id='indicator-graphic2'),
                html.Br(), html.Br(),
                dcc.Slider(
                    id='year--slider2',
                    min=df_morteNeonatal_AC['year_death'].min(),
                    max=df_morteNeonatal_AC['year_death'].max(),
                    value=df_morteNeonatal_AC['year_death'].max(),
                    marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
                    step=None
                )
            ]),
            dcc.Tab(label='Segunda tab', value='tab-2', children=[
                html.Div([
                    html.Div([
                        html.Br(), html.Br(),
                        dcc.Graph(id='indicator-graphic3'),
                    ],style={'width': '40%', 'float': 'right', 'display': 'inline-block'}),
                    html.Div([
                        html.Br(), html.Br(),
                        dcc.Graph(id='indicator-graphic4'),
                    ],style={'width': '60%','height':'100%','float': 'left', 'display': 'inline-block'}),
                    dcc.Slider(
                        id='year--slider3',
                        min=df_morteNeonatal_AC['year_death'].min(),
                        max=df_morteNeonatal_AC['year_death'].max(),
                        value=df_morteNeonatal_AC['year_death'].max(),
                        marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
                        step=None
                    ),
                ])
                
            ]),
            dcc.Tab(label='Terceira tab', value='tab-3', children=[


            ]),
        ]),
        html.Div(id='tabs-content'),
        
    ])
])
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
        ])
    elif tab == 'tab-2':
        return html.Div([
        ])
    elif tab == 'tab-3':
        return html.Div([
        ])

@app.callback(
    Output('indicator-graphic2', 'figure'),
    [Input('xaxis-column2', 'value'),
     Input('yaxis-column2', 'value'),
     Input('xaxis-type2', 'value'),
     Input('yaxis-type2', 'value'),
     Input('year--slider2', 'value')])
def update_graph2(xaxis_column_name, yaxis_column_name,
                 xaxis_type2, yaxis_type2,
                 year_value2):
    aux=df_morteNeonatal_AC[:]

    menor_ano=aux['year_death'].min()
    #maior_ano=aux['year_death'].max()

    dataframe_original=aux[aux['year_death']==2006]
    if year_value2>menor_ano:
        for i in range(menor_ano+1,year_value2+1):
            #print(i)
            dataframe_auxiliar=aux[aux['year_death']==i]
            dataframe_original=dataframe_original.append(dataframe_auxiliar)
    #aux=aux[aux['year_death']==year_value2]
    dataframe_original=dataframe_original[dataframe_original['n_tp_raca_cor_mae']==xaxis_column_name]
    dataframe_original=dataframe_original[dataframe_original['n_tp_ocorrencia']==yaxis_column_name]

    aux_homem_final = dataframe_original[dataframe_original['n_sg_sexo']=='Homem']
    aux_mulher_final = dataframe_original[dataframe_original['n_sg_sexo']=='Mulher']

    lista_pesos=list(available_indicators_peso)
    #lista_idade_mae=list(available_indicators_idade_mae)

    return {
        'data': [
            dict(
                x=lista_pesos,
                y=aux_homem_final.groupby('n_nu_peso')['n_nu_peso'].count().values,
                name='Homens',
                text=aux_homem_final['n_sg_sexo'],
                #z=lista_idade_mae,
                type='histogram',
                marker={
                   'size': 20,
                   'color':'rgb(0, 179, 255)'
                }
                #type='pie'
                #type='scatter3d'
            ),
            dict(
                x=lista_pesos,
                y=aux_mulher_final.groupby('n_nu_peso')['n_nu_peso'].count().values,
                name='Mulheres',
                #z=lista_idade_mae,
                text=aux_mulher_final['n_sg_sexo'],
                type='histogram',
                marker={
                    'size': 20,
                    'color':'rgb(255, 64, 207)'
                }
                # type='scatter3d'
            )
        ],
        'layout': dict(
            xaxis={
                'title': 'Peso da criança',
                'type': 'linear' if xaxis_type2 == 'Linear' else 'log'
            },
            yaxis={
                'title': 'Número de óbitos',
                'type': 'linear' if yaxis_type2 == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
@app.callback(
    Output('indicator-graphic3', 'figure'),
    [Input('year--slider3', 'value')])
def update_graph3(year_value3):
    aux=df_morteNeonatal_AC[:]

    menor_ano=aux['year_death'].min()
    dataframe_original=aux[aux['year_death']==2006]
    if year_value3>menor_ano:
       for i in range(menor_ano+1,year_value3+1):
           dataframe_auxiliar=aux[aux['year_death']==i]
           dataframe_original=dataframe_original.append(dataframe_auxiliar)

    aux_homem_final = dataframe_original[dataframe_original['n_sg_sexo']=='Homem']
    aux_mulher_final = dataframe_original[dataframe_original['n_sg_sexo']=='Mulher']

    return {
        'data': [
            dict(
                values=[aux_homem_final.groupby('n_sg_sexo')['n_sg_sexo'].count().values[0],aux_mulher_final.groupby('n_sg_sexo')['n_sg_sexo'].count().values[0]],
                labels=['Meninos','Meninas'],
                type='pie',
                marker={
                    'colors':['rgb(0, 179, 255)','rgb(255, 105, 217)']
                }
            )
        ],
        'layout': dict(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(
    Output('indicator-graphic4', 'figure'),
    [Input('year--slider3', 'value')])
def update_graph4(year_value3):
    aux=df_morteNeonatal_AC[:]

    menor_ano=aux['year_death'].min()
    dataframe_original=aux[aux['year_death']==2006]
    if year_value3>menor_ano:
       for i in range(menor_ano+1,year_value3+1):
           dataframe_auxiliar=aux[aux['year_death']==i]
           dataframe_original=dataframe_original.append(dataframe_auxiliar)

    lista_pesos=list(available_indicators_peso)

    #aux_homem_final = dataframe_original[dataframe_original['n_sg_sexo']=='Homem']
    #aux_mulher_final = dataframe_original[dataframe_original['n_sg_sexo']=='Mulher']
    # x=[10,20,30,40]
    # y=[1,2,3,4]
    # z=[100,200,300,400]
    
    # x2=[15,20,20,15]
    # y2=[4,3,2,1]
    # z2=[400,300,200,100]

    # teste=[x,y,z]
    # teste1=[x2,y2,z2]

    #teste1=[0][x,y,z]
    #teste2=[1][x1,x2,x3]
    return {
        'data': [
            # dict(
            #     x=teste[0],
            #     y=teste[1],
            #     z=teste[2],
            #     text=['Teste1','Teste2','Teste3','teste4'],
            #     type='scatter3d',
            #     mode='lines+markers',
            #     name='TesteM',
            #     marker={
            #         'color':'rgb(0, 173, 3)'
            #     }
            # ),
            dict(
                x = [0,1,2,3,4,5],
                y = [6,7,8,9,10,11],
                z = [[1, 10, 10, 11, 11],
                    [11, 10, 11, 10, 11],
                    [10, 11, 11, 11, 10],
                    [11, 10, 111, 10, 11],
                    [10, 11, 10, 12, 10]
                ],
                type='surface',
                surfacecolor='rgb(0, 255, 30)', 
            )
        ],
        'layout': dict(
            x='TesteX',
            y='TesteY',
            z='TesteZ',
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }







if __name__ == '__main__':
    app.run_server(host='192.168.15.10',port='8050',debug=True)


