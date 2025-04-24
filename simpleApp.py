import dash
from dash import html, Output, Input

# Create the app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.Button("Click me", id="my-button", n_clicks=0),
    html.Div(id="output-div")
])

# Callback to update the text based on number of clicks
#  @app.callback is a decorator that links the input and output components
#  The function update_output will be called whenever the button is clicked
#  The function takes the number of clicks as input and returns a string to be displayed in the output div
#  The Output specifies which component to update and what property to change
'''The function following the @app.callback decorator is the callback function.'''

@app.callback(
    Output("output-div", "children"),
    # Input to trigger the callback
    Input("my-button", "n_clicks")
)
def update_output(n_clicks):
    return f"You clicked the button {n_clicks} times."

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5001)