import pandas as pd

def preprocess(path):
    df = pd.read_csv(path)

    df = df[df["type"].isin([
            "large_airport",
            "medium_airport"
        ])].copy()

    df = df.dropna(subset=[
            "latitude_deg",
            "longitude_deg",
            "iso_country"
        ])
    return df
