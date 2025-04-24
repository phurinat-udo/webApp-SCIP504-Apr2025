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
@app.callback(
    Output("output-div", "children"),
    Input("my-button", "n_clicks")
)
def update_output(n_clicks):
    return f"You clicked the button {n_clicks} times."

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5001)