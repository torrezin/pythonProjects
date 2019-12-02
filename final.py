import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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


available_indicators_cor_mae = df_morteNeonatal_AC['n_tp_raca_cor_mae'].unique()
available_indicators_tipo_de_parto = df_morteNeonatal_AC['n_tp_ocorrencia'].unique()

ocor_anos=df_ac.groupby('year_death')['year_death'].count()
ocor_anos.values

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxix_cor_mae_column',
                options=[{'label': i, 'value': i} for i in available_indicators_cor_mae],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='xaxix_cor_mae_type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis_local_ocorrencia_column',
                options=[{'label': i, 'value': i} for i in available_indicators_tipo_de_parto],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(
                id='yaxis_local_ocorrencia_type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    dcc.Graph('Testando Um novo Gráfico',
    figure = {
        'data':[{'y':[1,2,3,4,5],'x':[5,6,7,8],'type':'linear'}]
        
    },style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),    

    html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df_morteNeonatal_AC['year_death'].min(),
        max=df_morteNeonatal_AC['year_death'].max(),
        value=df_morteNeonatal_AC['year_death'].max(),
        marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
        step=None
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])

if __name__ == '__main__':
    app.run_server(host='192.168.15.10',port='8050',debug=True)