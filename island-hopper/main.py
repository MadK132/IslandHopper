
import data_loader as dl
import graph as gr

df = dl.preprocess("data/airports.csv")

G = gr.build_graph(df, max_range_km=1500)

print("Airports:", G.number_of_nodes())
print("Connections:", G.number_of_edges())
print("Malpensa connections:", G.degree["LIMC"])

print("Malpensa:", G.nodes["LIMC"])
