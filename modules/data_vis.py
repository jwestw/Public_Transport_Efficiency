import pandas as pd
import plotly.express as px
import geopandas as gpd
from shapely.geometry import Point

def plot_map(newport_locations_df, city_centre, width=1500, height=1500, hover_data=None):
    fig = px.scatter_mapbox(
        newport_locations_df,  # Our DataFrame
        lat="lat",
        lon="lng",
        center=city_centre,  # where map will be centered
        width=width,  # Width of map
        height=height,  # Height of map
        hover_data=["id"],  # what to display when hovering mouse over coordinate
    )
    
    fig.update_layout(mapbox_style="open-street-map")  # adding beautiful street layout to map
    
    fig.show()    
    return fig

