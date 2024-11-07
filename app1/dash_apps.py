# app1/dash_apps.py
import dash
from django_plotly_dash import DjangoDash
import pandas as pd
from dash import dcc, html
import plotly.express as px
from .models import Orders, OrderDetails

# Initialize the Dash app
app = DjangoDash('OrdersDashboard')  # Name should be unique across your project

# Fetch data from the database
def load_data():
    orders = Orders.objects.all().values('order_date', 'order_total')
    df = pd.DataFrame(orders)
    return df

# Load the data and create a sample graph
df = load_data()
fig = px.line(df, x='order_date', y='order_total', title="Total Orders Over Time")

# Define layout and content of the dashboard
app.layout = html.Div([
    html.H1("Orders Dashboard"),
    dcc.Graph(id='orders-graph', figure=fig),
    # Add more charts as needed
])