
import data_loader as dl
import graph as gr
import routing as rt

df = dl.preprocess("data/airports.csv")

G = gr.build_graph(df, max_range_km=1500)

print("Airports:", G.number_of_nodes())
print("Connections:", G.number_of_edges())

start = "LIMC"
destination = "YSSY"

print("\n--- Shortest Route (BFS) ---")

shortest = rt.shortest_route(G, start, destination)

if shortest is not None:
    stats = rt.route_statistics(G, shortest)

    print("Route:", " -> ".join(shortest))
    print("Flights:", stats["flights"])
    print("Stops:", stats["stops"])
    print("Distance:", round(stats["distance_km"], 2), "km")
    print("Time:", round(stats["time_hours"], 2), "hours")
else:
    print("No route found")

print("\n--- Fastest Route (Dijkstra) ---")

fastest = rt.fastest_route(G, start, destination)

if fastest is not None:
    stats = rt.route_statistics(G, fastest)

    print("Route:", " -> ".join(fastest))
    print("Flights:", stats["flights"])
    print("Stops:", stats["stops"])
    print("Distance:", round(stats["distance_km"], 2), "km")
    print("Time:", round(stats["time_hours"], 2), "hours")
else:
    print("No route found")

print("\n--- Farthest Reachable Airport ---")

farthest = rt.farthest_reachable(G, start, max_stops=10)

if farthest is not None:
    print("Airport:", farthest)
    print("Name:", G.nodes[farthest]["name"])
    print("Country:", G.nodes[farthest]["country"])
else:
    print("No reachable airport found")
