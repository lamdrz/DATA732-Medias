from dash import Dash, html
from components.timelapse import TimeLapse
from components.heatmap import HeatMap
from utils.load_file import load_data
data = load_data()
    

app = Dash(__name__)

layout = []
layout.extend(TimeLapse(data).get_layout())
layout.append(HeatMap(data).get_layout())

app.layout = html.Div(layout)

TimeLapse(data).get_callbacks(app)
HeatMap(data).get_callbacks(app)

app.run(debug=True)
