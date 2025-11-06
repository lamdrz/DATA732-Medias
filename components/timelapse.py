from dash import dcc, Input, Output
from datetime import datetime
import pandas as pd
import plotly.express as px


class TimeLapse:
    def __init__(self, data):
        self.data = data
        self.kws = data['metadata']['all']['kws']

        self.searchbar = dcc.Dropdown(
            id="searchbar",
            options=[{"label": kw, "value": kw} for kw in self.kws.keys()],
            value=None,
            multi=True
        )

        self.period_selector = dcc.Dropdown(
            id="period-selector",
            options=[
                {"label": "Yearly", "value": "year"},
                {"label": "Monthly", "value": "month"},
                {"label": "Daily", "value": "day"}
            ],
            value="month",
            clearable=False
        )

        self.graph = dcc.Graph(
            id="timelapse-graph"
        )


    def get_layout(self):
        return [
            self.searchbar,
            self.period_selector,
            self.graph
        ]
    

    def get_callbacks(self, app):
        @app.callback(
            Output("timelapse-graph", "figure"),
            Input("searchbar", "value"),
            Input("period-selector", "value"))
        def update_graph(selected_kws, period="month"):
            if not selected_kws: selected_kws = []
            out_data = {kw: {} for kw in selected_kws} if selected_kws else {}

            data = self.data['metadata'][period]
            for year in data :
                match period:
                    case "year":
                        for kw in selected_kws:
                            out_data[kw][datetime(int(year), 1, 1)] = data[year]['kws'].get(kw, 0)
                    case "month":
                        for month in data[year]:
                            for kw in selected_kws:
                                out_data[kw][datetime(int(year), int(month), 1)] = data[year][month]['kws'].get(kw, 0)
                    case "day":
                        for month in data[year]:
                            for day in data[year][month]:
                                for kw in selected_kws:
                                    out_data[kw][datetime(int(year), int(month), int(day))] = data[year][month][day]['kws'].get(kw, 0)

            for kw in out_data:
                out_data[kw] = dict(sorted(out_data[kw].items()))

            fig = px.line(out_data, labels={'index': 'Time', 'value': 'Frequency'}, title='Keyword Frequency Over Time')
            return fig