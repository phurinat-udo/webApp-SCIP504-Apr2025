import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd

# Create a simple Pandas DataFrame (data source)
data = {'X-Axis': [1, 2, 3, 4, 5],
        'Y-Axis': [3, 7, 4, 8, 6]}
df = pd.DataFrame(data)

# Create a basic line plot using Plotly Graph Objects
fig = go.Figure(data=[go.Scatter(x=df['X-Axis'], y=df['Y-Axis'], marker_color='blue')])

# Add title and labels for clarity
fig.update_layout(title='My First Plotly Dash App',
                  xaxis_title='X-Axis Label',
                  yaxis_title='Y-Axis Label')

# Initialize the Dash app.  Note external_stylesheets can be used to import CSS.
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# Define the app layout.  This is the structure of the web page.
app.layout = html.Div(children=[
    html.H1(children='Hello Dash',  # A header
            style={'textAlign': 'center', 'color': '#1E3091'}), #styling the text

    html.Div(children='A simple example using Plotly and Dash.',  # A sub-header
             style={'textAlign': 'center', 'color': '#A9A9A9'}), #styling the text

    dcc.Graph(  # A Plotly graph component
        id='example-graph',  # Unique identifier for the component
        figure=fig  # The Plotly figure we created earlier
    ),
    html.Div(children=[       # Adding an interactive slider
        html.Label('Select a value:'), # Label above the slider
        dcc.Slider(
            id='my-slider',  # Unique identifier
            min=1,           # Minimum value of the slider
            max=5,           # Maximum value of the slider
            step=1,          # Interval between slider values
            value=3,          # Initial value of the slider
            marks={i: f'Label {i}' if i != 1 and i != 5 else { 'label': f'Label {i}', 'style': {'color': '#77b0b1'}}, #Custom labels
                   1: {'label': 'Start', 'style': {'color': '#77b0b1'}},
                   5: {'label': 'End', 'style': {'color': '#77b0b1'}}}, # More custom labels
            )
        ], style={'width': '50%', 'padding': '40px', 'display': 'inline-block'})
])



# Run the app.  This starts the Dash server.
if __name__ == '__main__':
    app.run_server(debug=True)  # Set debug=True for hot-reloading
