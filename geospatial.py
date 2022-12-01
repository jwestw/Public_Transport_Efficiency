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
  pd_df = pd_df.rename(columns={"lon":"lng"})

  # Add number to end of duplicate id  values
  mask = pd_df['id'].duplicated()
  pd_df.loc[mask, 'id'] += pd_df.groupby('id').cumcount().add(1).astype(str)

  # Drop na values - this occurs do to error in the original spreadsheet which needs fixing
  pd_df = pd_df.dropna(axis=0)

  return pd_df

  def walking_time(meters = 500, speed = 5):
  # To calculate time use formula time = distance / speed
  speed_meters = speed * 1000
  max_walk_time = (meters/speed_meters)*60*60

  return max_walk_time