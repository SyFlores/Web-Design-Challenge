import pandas as pd
import os

df = pd.read_csv("cities.csv")

df.to_html("tablecities.html")