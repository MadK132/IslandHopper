import data_loader as dl
import distances as ds
df = dl.preprocess("data/airports.csv")
airport1 = df[df["ident"] == "LIMC"]
print(airport1)
airport2 = df[df["ident"] == "YSSY"]
print(airport2)
lat1 = airport1["latitude_deg"].iloc[0]
lon1 = airport1["longitude_deg"].iloc[0]
lat2 = airport2["latitude_deg"].iloc[0]
lon2 = airport2["longitude_deg"].iloc[0]
distanceMiSy = ds.haversine(lat1, lon1, lat2, lon2)
print(distanceMiSy)