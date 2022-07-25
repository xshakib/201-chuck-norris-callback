######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['santa bond mike', 'prison mike', 'willy wonka mike', 'datemike']
list_of_images=['bondmike.jpg', 'prisonmike.png', 'wonkamike.png', 'datemike.png']
githublink = 'https://github.com/xshakib/201-chuck-norris-callback'
myheading1='Pick Your Michael Scott Experience!'
sourceurl = 'https://github.com/xshakib/201-chuck-norris-callback'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Scott\'s Tots'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(myheading1),
    html.Img(id='show-image', src=app.get_asset_url('tellmoremike.png'),style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
                 options=[{'label': i, 'value': i} for i in list_of_choices],
                 value='initial',
                 style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback([dash.dependencies.Output('your-output-here', 'children'),
              dash.dependencies.Output('show-image', 'src')],
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    
    print(whatever_you_chose)
    if whatever_you_chose == "initial":
        print("000000000")
        return (f'Pick your favorite Michael Scott characters and enjoy!',
                app.get_asset_url('tellmoremike.png'))
    
    else:
        print("11111111")
        return (f'You are now rolling with {whatever_you_chose}!',
                app.get_asset_url(list_of_images[list_of_choices.index(whatever_you_chose)]))



######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
