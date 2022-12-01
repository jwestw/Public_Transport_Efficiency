def clean_points_of_interest_df(df_in):

  # Select relevant columns
  df_clean = points_of_interest_df[["NAME", "FEATURE_EASTING", "FEATURE_NORTHING"]]
  # Rename "NAME" column
  df_clean = df_clean.rename(columns={"NAME":"id"})

  return df_clean