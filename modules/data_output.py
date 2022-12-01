import pandas as pd


def writeh5(df, out_path):
    "Writes data out to h5"
    store = pd.HDFStore(out_path)
    try:
        store.append("results", df, append=True)
    except NameError as e:
        print(f"The dataframe does not exist : {e}")
    store.close()
    store.is_open


def write_excel(df, out_path):
    with pd.ExcelWriter(out_path) as writer:
        df.to_excel(writer)
