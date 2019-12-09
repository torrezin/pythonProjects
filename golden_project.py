import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output

import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

#listas globais
lista_dias_vividos=[]
lista_total=[]
#df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')


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
#available_indicators = df['Indicator Name'].unique()

available_indicators_peso = df_morteNeonatal_AC['n_nu_peso'].unique()
available_indicators_idade_mae = df_morteNeonatal_AC['n_ct_idade'].unique()
available_indicators_cor_mae = df_morteNeonatal_AC['n_tp_raca_cor_mae'].unique()
available_indicators_tipo_de_parto = df_morteNeonatal_AC['n_tp_ocorrencia'].unique()
##----------------- Indicadores -------------
app.layout = html.Div([
    html.Div([
        dcc.Tabs(id="tabs", value='tab-3', children=[
            dcc.Tab(label='1º Visualização:', value='tab-1', children=[
                html.H1(["Número de óbitos por peso, cor da mãe, ano, local de nascença"],style={'text-align':'center'}),
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
            dcc.Tab(label='2º Visualização:', value='tab-2', children=[
                html.H1(["Número de óbitos e média de dias vividos por faixa de peso"],style={'text-align':'center'}),
                html.Div([
                    html.Div([
                        html.Br(),
                        dcc.Graph(id='indicator-graphic3'),
                    ],style={'width': '30%', 'float': 'right', 'display': 'inline-block'}),
                    html.Div([
                        html.Br(), html.Br(),
                        dcc.Graph(id='indicator-graphic4'),
                    ],style={"width": "70%" }),
                    dcc.Slider(
                        id='year--slider3',
                        min=df_morteNeonatal_AC['year_death'].min(),
                        max=df_morteNeonatal_AC['year_death'].max(),
                        value=df_morteNeonatal_AC['year_death'].max(),
                        marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
                        step=None
                    ),
                ],style={'height':'100%'}),               
            ]),
            dcc.Tab(label='3º Visualização:', value='tab-3', children=[
                html.H1(["Título 3"],style={'text-align':'center'}),
                dcc.Graph(id='indicator-graphic5'),
                html.Br(), html.Br(),

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
    ##Criando dataframes auxiliares
    df_teste = df_ac[:]
    df_morteNeonatal=df_teste[:]

    #Filtrando o csv e convertendo informações
    df_morteNeonatal['year_death'] = df_morteNeonatal['year_death'].astype('Int64')
    df_morteNeonatal=df_morteNeonatal[df_morteNeonatal["morte_menor_28d"] == 1]

    df_morteNeonatal.loc[df_morteNeonatal.n_sg_sexo == 'M','n_sg_sexo'] = 1
    df_morteNeonatal.loc[df_morteNeonatal.n_sg_sexo == 'F','n_sg_sexo'] = 2
    df_morteNeonatal['n_sg_sexo']=df_morteNeonatal['n_sg_sexo'].astype(int)
    menor_ano=df_morteNeonatal['year_death'].min()

    ##Data frame ordenado
    teste_order=df_morteNeonatal.sort_values(by=['n_nu_peso'])
    aux=teste_order[:]

    #Criando listas para realização de calculos
    lista_dia_nascimento_ordenada=[]
    lista_dia_morte_ordenada=[]
    lista_mes_nascimento_ordenada=[]
    lista_mes_morte_ordenada=[]
    lista_ano_nascimento_ordenada=[]
    lista_ano_morte_ordenada=[]

    #Ocorrencia momentanea que é inserida na lista de ocorrencias    
    ocorrencias=0
    lista_ocorrencias=[]
    
    #Agrupando csv's por ano
    menor_ano=aux['year_death'].min()
    dataframe_original=aux[aux['year_death']==2006]
    if year_value3>menor_ano:
       for i in range(menor_ano+1,year_value3+1):
           dataframe_auxiliar=aux[aux['year_death']==i]
           dataframe_original=dataframe_original.append(dataframe_auxiliar)

    ##--------------------------------------------------------------------------------------------------------------

    teste_order=dataframe_original.sort_values(by=['n_nu_peso'])
    elemetos_linha_matriz=0
    #Pegando os pesos do dataframe
    lista_ordenada=list(teste_order['n_nu_peso'].values)

    if year_value3==2016:
        #Inserindo pesos lixos pra completar 280 e ter 10 partes inteiras de 28 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        elemetos_linha_matriz=28
    if year_value3==2015:
        #Inserindo pesos lixos pra completar 250 e ter 10 partes inteiras de 25 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        elemetos_linha_matriz=25
    if year_value3==2014:
        #Inserindo pesos lixos pra completar 210 e ter 10 partes inteiras de 21 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        elemetos_linha_matriz=21
    if year_value3==2013:
        #Inserindo pesos lixos pra completar 160 e ter 10 partes inteiras de 16 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)        
        lista_ordenada.insert(0,9)        
        lista_ordenada.insert(0,10) 
        elemetos_linha_matriz=16       
    if year_value3==2012:
        #Inserindo pesos lixos pra completar 110 e ter 10 partes inteiras de 11 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)          
        lista_ordenada.insert(0,9)          
        lista_ordenada.insert(0,10)          
        lista_ordenada.insert(0,11)         
        lista_ordenada.insert(0,12) 
        elemetos_linha_matriz=11    
    if year_value3==2011:
        #Inserindo pesos lixos pra completar 90 e ter 10 partes inteiras de 9 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5) 
        lista_ordenada.insert(0,6) 
        lista_ordenada.insert(0,7) 
        lista_ordenada.insert(0,8) 
        elemetos_linha_matriz=9       
    if year_value3==2010:
        #Inserindo pesos lixos pra completar 80 e ter 10 partes inteiras de 8 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4) 
        elemetos_linha_matriz=8    
    if year_value3==2009:
        #Inserindo pesos lixos pra completar 70 e ter 10 partes inteiras de 7 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        elemetos_linha_matriz=7
    if year_value3==2008:
        #Inserindo pesos lixos pra completar 60 e ter 10 partes inteiras de 6 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)
        lista_ordenada.insert(0,6)
        lista_ordenada.insert(0,7)
        lista_ordenada.insert(0,8)   
        elemetos_linha_matriz=6             
    if year_value3==2007:
        #Inserindo pesos lixos pra completar 40 e ter 10 partes inteiras de 4 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)        
        lista_ordenada.insert(0,9)        
        lista_ordenada.insert(0,10)        
        lista_ordenada.insert(0,11)        
        lista_ordenada.insert(0,12)
        elemetos_linha_matriz=4 
    if year_value3==2006:
        #Inserindo pesos lixos pra completar 30 e ter 10 partes inteiras de 3 na matriz de pesos
        lista_ordenada.insert(0,1)
        lista_ordenada.insert(0,2)
        lista_ordenada.insert(0,3)
        lista_ordenada.insert(0,4)
        lista_ordenada.insert(0,5)        
        lista_ordenada.insert(0,6)        
        lista_ordenada.insert(0,7)        
        lista_ordenada.insert(0,8)        
        lista_ordenada.insert(0,9)        
        lista_ordenada.insert(0,10)        
        lista_ordenada.insert(0,11)         
        lista_ordenada.insert(0,12)
        elemetos_linha_matriz=3
        
    #Removendo elementos repetidos da lista
    i = 0
    while i < len(lista_ordenada):
        count = lista_ordenada.count(lista_ordenada[i]) 
        for j in range(0, count-1):
            lista_ordenada.remove(lista_ordenada[i])

        i = i+1
    print(len(lista_ordenada))   
    #Criando matriz para agrupamento dos pesos //Nem queira entender...
    matriz_pesos=np.zeros((10,elemetos_linha_matriz))
    aux=0
    cont = 0
    aux2=elemetos_linha_matriz
    aux3=1

    for y in range(0,10):
        l_teste=[]
        for j in range(aux,aux2):
            #print("Elemento adicionado = "+str(lista_ordenada[j]))
            #print("posicao da lista = "+str(j))
            #print("cont "+str(cont))
            #print("Aux = "+str(aux))
            aux=j
            l_teste.append(lista_ordenada[j])
            
        for tamanho in range(0,len(l_teste)):
            matriz_pesos[cont][tamanho]=int(l_teste[tamanho])
        l_teste=[]

        j=aux+1
        aux=aux+1
        cont=cont+1
        aux3=aux3+1
        aux2=aux3*elemetos_linha_matriz
        
    #Criando listas auxiliares para tirar a média de dias vividos por agrupamento de pesos
    for i in range(0,len(matriz_pesos)):
        for j in range(0,elemetos_linha_matriz):
            aux=teste_order[teste_order['n_nu_peso']==matriz_pesos[i][j]]
            valores_a_inserir_day_birth=aux['day_birth'].values
            valores_a_inserir_day_death=aux['day_death'].values
            valores_a_inserir_month_birth=aux['month_birth'].values
            valores_a_inserir_month_death=aux['month_death'].values
            valores_a_inserir_year_birth=aux['year_birth'].values
            valores_a_inserir_year_death=aux['year_death'].values
            for x in range(0,len(valores_a_inserir_day_birth)):
                lista_dia_nascimento_ordenada.append(valores_a_inserir_day_birth[x])
                lista_dia_morte_ordenada.append(valores_a_inserir_day_death[x])
                
                lista_mes_nascimento_ordenada.append(valores_a_inserir_month_birth[x])
                lista_mes_morte_ordenada.append(valores_a_inserir_month_death[x])
                
                lista_ano_nascimento_ordenada.append(valores_a_inserir_year_birth[x])
                lista_ano_morte_ordenada.append(valores_a_inserir_year_death[x])
                
            ocorrencias = ocorrencias + teste_order[teste_order['n_nu_peso']==matriz_pesos[i][j]].count().values[0]
        lista_ocorrencias.append(ocorrencias)
        lista_dia_nascimento_ordenada.append("___")
        lista_dia_morte_ordenada.append("___")
        lista_mes_nascimento_ordenada.append("___")
        lista_mes_morte_ordenada.append("___")
        lista_ano_nascimento_ordenada.append("___")
        lista_ano_morte_ordenada.append("___")
        ocorrencias= 0

    #Listas auxiliares
    lista_db=[]
    lista_dd=[]
    lista_mb=[]
    lista_md=[]
    lista_yb=[]
    lista_yd=[]

    #Preenchendo listas auxiliares para calcular a média de dias vividos por faixa de peso
    for i in range(0,len(lista_dia_nascimento_ordenada)):
        if(lista_dia_nascimento_ordenada[i]!='___'):
            lista_db.append(lista_dia_nascimento_ordenada[i])
            lista_dd.append(lista_dia_morte_ordenada[i])
            lista_mb.append(lista_mes_nascimento_ordenada[i])
            lista_md.append(lista_mes_morte_ordenada[i])
            lista_yb.append(lista_ano_nascimento_ordenada[i])
            lista_yd.append(lista_ano_morte_ordenada[i])
            #print(str(lista_dia_nascimento_ordenada[i])+"---> "+str(i+1))
        else:
            i=i+1
            dias_vividos_v2(lista_db,lista_mb,lista_yb,lista_dd,lista_md,lista_yd)
            lista_db=[]
            lista_dd=[]
            lista_mb=[]
            lista_md=[]
            lista_yb=[]
            lista_yd=[]
    lista_pesos_grafico=[]
    for i in range(0,len(matriz_pesos)):
        lista_pesos_grafico.append(str(int(matriz_pesos[i].min()))+"-"+str(int(matriz_pesos[i].max())))

##---------------------------------------------------------------------------------------------------------------------------

    

    lista_pesos=list(available_indicators_peso)
    return {
        'data': [
            dict(
                x = lista_ocorrencias,#Ocorrencias por faixa de peso
                y = lista_pesos_grafico,#Faixas de peso
                z=lista_total, #Média de dias vividos por faixa de peso
                type='scatter3d',
                surfacecolor='rgb(0, 255, 30)',
                mode='markers', 
                marker={'size': 8, 'color': lista_total, 'colorscale': 'Viridis', "showscale": True,
                        "colorbar": {"thickness": 15, "len": 0.5, "x": 0.8, "y": 0.6, }, },
                # camera= dict(
                # up=dict(x=0,y=0,z=1),
                # center=dict(x=0,y=0,z=0),
                # eye=dict(x=0,y=0,z=0),
                #),
            )
        ],
        'layout': dict(
            paper_bgcolor="#f3f3f3",
            height=600,
            scene={
                "xaxis":{'title':'Número de óbitos'},
                "yaxis":{'title':'Peso'},
                "zaxis":{'title':'Média de dias vividos'},
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
@app.callback(
    Output('indicator-graphic5', 'figure'),
    [Input('year--slider3', 'value')])
def update_graph5(year_value5):
    var config = {mapboxAccessToken: "pk.eyJ1IjoidGhsaW5kdXN0cmllcyIsImEiOiJjazN5ZnN1ZnkxazBqM2Vtcjd2ZzFwOTY1In0.wNk2ICvUYS1E4L7ubsHvlg"}

    return {
        'data': [
            dict(
                # values=[10,20,30],
                # labels=['Meninos','Meninas','Meninx'],
                # type='pie',
                # marker={
                #     'colors':['rgb(0, 179, 255)','rgb(255, 105, 217)']
                # }
                type= "scattermapbox",
				text= unpack(rows, "Globvalue"),
				lon= unpack(rows, "Lon"),
				lat= unpack(rows, "Lat"),
				marker= { color: "fuchsia", size: 4 }
            )
        ],
        'layout': dict(
            # margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            # hovermode='closest'
            dragmode= "zoom",
			mapbox= { style: "open-street-map",center: { lat: 38, lon: -90 }, zoom: 3 },
			margin= { r: 0, t: 0, b: 0, l: 0 }
        )
    }


def dias_vividos_v2(lista_db,lista_mb,lista_yb,lista_dd,lista_md,lista_yd):
    aux=0
    aux2=0
    lista_dias_vividos.append("___________")
    for i in range(0,len(lista_db)):
        aux=(lista_yd[i]-lista_yb[i])
        aux=(aux*12)+lista_md[i]-lista_mb[i]
        aux=aux*31
        aux=aux+lista_dd[i]
        aux=aux-lista_db[i]
        aux2=aux2+aux
    aux2=aux2/int(len(lista_db))
    if round(aux2) not in lista_total:
        lista_total.append(int(round(aux2)))

    




if __name__ == '__main__':
    app.run_server(host='192.168.240.158',port='8050',debug=True)
# #     app.run_server(debug=True)
# if __name__ == "__main__":
#     app.run_server(debug=True)


