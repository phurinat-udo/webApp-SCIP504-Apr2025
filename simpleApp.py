import dash
from dash import html

# Create the app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div("Hello, Mars!")

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=36646)