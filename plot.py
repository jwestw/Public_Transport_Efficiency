import pandas as pd
import plotly.express as px
import geopandas as gpd
from shapely.geometry import Point

points_of_interest_newport_df = pd.read_csv(r"/Users/chloemurrell/DSST - Public Transport Efficiency/points-of-interest-newport-csv.csv", delimiter="|", dtype={"POINTX_CLASSIFICATION_CODE": str})


def clean_points_of_interest_df(df_in):

    # Select relevant columns
    df_clean = points_of_interest_newport_df[["NAME", "FEATURE_EASTING", "FEATURE_NORTHING"]]
    # Rename "NAME" column
    df_clean = df_clean.rename(columns={"NAME": "id"})

    return df_clean


newport_locations_df = clean_points_of_interest_df(points_of_interest_newport_df)


def convert_coordinates(df_in, coord_col_1, coord_col_2):

    # Convert northing and easting -> longnitude and latitude
    geometry = [Point(xy) for xy in zip(df_in[coord_col_1], df_in[coord_col_2])]

    geo_df = gpd.GeoDataFrame(df_in, geometry=geometry)

    geo_df.crs = "EPSG:27700"

    geo_df.to_crs("EPSG:4326", inplace=True)

    # Extract lng and lat coodinates into separate columns from POINT() column.
    geo_df['lng'] = geo_df['geometry'].x
    geo_df['lat'] = geo_df['geometry'].y

    # Convert to pandas df
    pd_df = pd.DataFrame(df_in)

    # Drop unnecessary columns
    pd_df = pd_df.drop([coord_col_1, coord_col_2, "geometry"], axis=1)

    # Rename longnitude column in line with API requirements - delete
    pd_df = pd_df.rename(columns={"lon": "lng"})

    # Add number to end of duplicate id  values
    mask = pd_df['id'].duplicated()
    pd_df.loc[mask, 'id'] += pd_df.groupby('id').cumcount().add(1).astype(str)

    # Drop na values - this occurs do to error in the original spreadsheet which needs fixing
    pd_df = pd_df.dropna(axis=0)

    return pd_df


newport_locations_df = convert_coordinates(newport_locations_df, "FEATURE_EASTING", "FEATURE_NORTHING")

fig = px.scatter_mapbox(
    newport_locations_df,  # Our DataFrame
    lat="lat",
    lon="lng",
    center={"lat": 51.586106, "lon": -2.991391},  # where map will be centered
    width=1500,  # Width of map
    height=1500,  # Height of map
    hover_data=["id"],  # what to display when hovering mouse over coordinate
)

fig.update_layout(mapbox_style="open-street-map")  # adding beautiful street layout to map

fig.show()
