import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("sales_data.csv")

# Create app
app = dash.Dash(__name__)

# Charts
sales_chart = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend")
users_chart = px.bar(df, x="Month", y="Users", title="Monthly Users")
profit_chart = px.bar(df, x="Month", y="Profit", title="Monthly Profit")

# Layout
app.layout = html.Div([
    html.H1("CODTECH Dashboard Development", style={'textAlign': 'center'}),

    dcc.Graph(figure=sales_chart),
    dcc.Graph(figure=users_chart),
    dcc.Graph(figure=profit_chart)
])

# Run server
if __name__ == "__main__":
    app.run(debug=True)

