import numpy as np
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

np.random.seed(42)
dates = pd.date_range("2023-01-01", periods=200)
values = np.cumsum(np.random.randn(200) * 10)
categories = np.random.choice(["A", "B", "C"], size=200)
df = pd.DataFrame({"Date": dates, "Value": values, "Category": categories})

pivot = df.pivot_table(index="Date", columns="Category", values="Value", aggfunc="mean")
pivot = pivot.interpolate().rolling(7).mean().reset_index()

fig = px.line(pivot, x="Date", y=pivot.columns[1:], title="Trend Analysis", template="plotly_dark")

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Trend Analysis Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
