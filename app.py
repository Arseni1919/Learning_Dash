import dash

from imports import *


app = dash.Dash(__name__)

# --- DATA --- #
df = pd.DataFrame({
    'revenue': [10, 20, 30, 40, 50],
    'income': [10, 11, 12, 13, 15]
})
# ------------ #

# LAYOUT
app.layout = html.Div([
    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),
    dcc.Dropdown(
        id='sclt_year',
        options=[
            {"label": "2015", "value": 2015},
            {"label": "2016", "value": 2016},
            {"label": "2017", "value": 2017},
            {"label": "2018", "value": 2018},
        ],
        multi=False,
        value=2015,
        style={'width': '40%'}
    ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_app', figure={}),
])


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_app', component_property='figure')],
    [Input(component_id='sclt_year', component_property='value')],
)
def update_graph(option_slctd):
    print(f'option_slctd: {option_slctd}, type: {type(option_slctd)}')
    container = html.H2(f'Chosen option: {option_slctd}, type: {type(option_slctd)}', style={'text-align': 'center'})

    copy_df = df.copy()
    fig = px.scatter(copy_df, x='revenue', y='income', opacity=0.65, trendline_color_override='darkblue')
    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)


