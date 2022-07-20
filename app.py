######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['santa bond mike', 'prison mike', 'willy wonka mike', 'datemike']
list_of_images=['bondmike.jpg', 'prisonmike.png', 'wonkamike.png', 'datemike.png', 'tellmoremike.png']
githublink = 'https://github.com/xshakib/201-chuck-norris-callback'
myheading1='Pick Your Michael Scott Experience!'
sourceurl = 'https://github.com/xshakib/201-chuck-norris-callback'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Regional Manager'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(myheading1),
    html.Img(id='image-output', src=app.get_asset_url('download.png')),
    dcc.Dropdown(id='your-input-here',
                options=[{'value': i, 'label': list_of_choices[i]} for i in range(0, 4)],
                value='McDouble',
                style={'width': '500px'}),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):
    return f'Get ready to roll with {whatever_you_chose}!'

@app.callback(dash.dependencies.Output('image-output', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):
    return app.get_asset_url(list_of_images[whatever_you_chose])



######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
