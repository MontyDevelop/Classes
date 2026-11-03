from dash import Dash, html, dcc
import plotly.express as px

fig = px.line(x=[1,2,3,4], y=[10,15,13,20])

app = Dash(__name__)
app.layout = html.Div([
    html.H2("Dash Web App"),
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
