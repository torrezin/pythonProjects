import dash
import dash_core_components as dcc
import dash_html_components as html
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
##------------------RN---------------------
# df_morteNeonatal_RN=df_rn[:]
# df_morteNeonatal_RN['year_death'] = df_morteNeonatal_RN['year_death'].astype('Int64')
# df_morteNeonatal_RN=df_morteNeonatal_RN[df_morteNeonatal_RN["morte_menor_28d"] == 1]
# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_sg_sexo == 'M','n_sg_sexo'] = 1
# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_sg_sexo == 'F','n_sg_sexo'] = 2
# df_morteNeonatal_RN['n_sg_sexo']=df_morteNeonatal_RN['n_sg_sexo'].astype(int)

# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_tp_raca_cor_mae == 1,'n_tp_raca_cor_mae'] = 'maes_brancas'
# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_tp_raca_cor_mae == 2,'n_tp_raca_cor_mae'] = 'maes_negras'
# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_tp_raca_cor_mae == 3,'n_tp_raca_cor_mae'] = 'maes_asiaticas'
# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_tp_raca_cor_mae == 4,'n_tp_raca_cor_mae'] = 'maes_pardas'
# df_morteNeonatal_RN.loc[df_morteNeonatal_RN.n_tp_raca_cor_mae == 5,'n_tp_raca_cor_mae'] = 'maes_indigenas'
# ##------------------RN---------------------
# ##------------------ES---------------------
# df_morteNeonatal_ES=df_es[:]
# df_morteNeonatal_ES['year_death'] = df_morteNeonatal_ES['year_death'].astype('Int64')
# df_morteNeonatal_ES=df_morteNeonatal_ES[df_morteNeonatal_ES["morte_menor_28d"] == 1]
# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_sg_sexo == 'M','n_sg_sexo'] = 1
# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_sg_sexo == 'F','n_sg_sexo'] = 2
# df_morteNeonatal_ES['n_sg_sexo']=df_morteNeonatal_ES['n_sg_sexo'].astype(int)

# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_tp_raca_cor_mae == 1,'n_tp_raca_cor_mae'] = 'maes_brancas'
# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_tp_raca_cor_mae == 2,'n_tp_raca_cor_mae'] = 'maes_negras'
# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_tp_raca_cor_mae == 3,'n_tp_raca_cor_mae'] = 'maes_asiaticas'
# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_tp_raca_cor_mae == 4,'n_tp_raca_cor_mae'] = 'maes_pardas'
# df_morteNeonatal_ES.loc[df_morteNeonatal_ES.n_tp_raca_cor_mae == 5,'n_tp_raca_cor_mae'] = 'maes_indigenas'
# ##------------------ES---------------------


estados = []

estados.append(df_morteNeonatal_AC)
# estados.append(df_morteNeonatal_RN)
# estados.append(df_morteNeonatal_ES)

available_indicators_cor_mae = df_morteNeonatal_AC['n_tp_raca_cor_mae'].unique()
available_indicators_tipo_de_parto = df_morteNeonatal_AC['n_tp_ocorrencia'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators_cor_mae],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators_tipo_de_parto],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(
                id='crossfilter-yaxis-type',
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

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),

    html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df_morteNeonatal_AC['year_death'].min(),
        max=df_morteNeonatal_AC['year_death'].max(),
        value=df_morteNeonatal_AC['year_death'].max(),
        marks={str(year): str(year) for year in df_morteNeonatal_AC['year_death'].unique()},
        step=None
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df_morteNeonatal_AC[df_morteNeonatal_AC['year_death'] == year_value]

    return {
        'data': [dict(
            x=dff[dff['n_tp_raca_cor_mae'] == xaxis_column_name]['n_tp_raca_cor_mae'],
            y=dff[dff['n_tp_ocorrencia'] == yaxis_column_name]['n_tp_raca_cor_mae'],
            text=dff[dff['n_tp_ocorrencia'] == yaxis_column_name]['n_tp_ocorrencia'],
            customdata=dff[dff['n_tp_ocorrencia'] == yaxis_column_name]['n_tp_ocorrencia'],
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
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


def create_time_series(dff, axis_type, title):
    return {
        'data': [dict(
            x=dff['Year'],
            y=dff['Value'],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    dff = df_morteNeonatal_AC[df_morteNeonatal_AC['n_tp_ocorrencia'] == country_name]
    dff = df_morteNeonatal_AC[df_morteNeonatal_AC['n_tp_raca_cor_mae'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
    return create_time_series(dff, axis_type, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
    dff = dff[dff['Indicator Name'] == yaxis_column_name]
    return create_time_series(dff, axis_type, yaxis_column_name)


if __name__ == '__main__':
    app.run_server(debug=True)