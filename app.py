######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_options=['santa bond mike', 'prison mike', 'willy wonka mike', 'datemike']
list_of_images=['bondmike.jpg', 'prisonmike.png', 'wonkamike.png', 'datemike.png', 'tellmoremike.gif']
githublink = 'https://github.com/xshakib/201-chuck-norris-callback'
myheading1='Pick Your Favorite Michael Scott Character'
sourceurl = 'https://github.com/xshakib/201-chuck-norris-callback'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='MGC'

####### Layout of the app ########
app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.RadioItems(
        id='your_input_here',
        options=[
                {'label':list_of_options[0], 'value':list_of_images[0]},
                {'label':list_of_options[1], 'value':list_of_images[1]},
                {'label':list_of_options[2], 'value':list_of_images[2]},
                {'label':list_of_options[3], 'value':list_of_images[3]},
                ],
        value=list_of_images[4],
        ),
    html.Div(id='your_output_here', children=''),
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
    return f'Michael will now entertain you with a {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
