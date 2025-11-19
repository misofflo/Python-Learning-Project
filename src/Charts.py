import numpy as np
import pandas as pd
import plotly as plt

world_gdp_data = pd.read_csv("world_gdp_data.csv")

figure = world_gdp_data.loc[66].plot.line(
    backend = "plotly",
    title = "Germany GDP Growth Over Years"
)

figure.show()

#print(world_gdp_data)