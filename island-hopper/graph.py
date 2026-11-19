
import networkx as nx
from distances import haversine


def build_graph(df, max_range_km):
    G = nx.Graph()

    for _, airport in df.iterrows():
        G.add_node(
            airport["ident"],
            name=airport["name"],
            latitude=airport["latitude_deg"],
            longitude=airport["longitude_deg"],
            country=airport["iso_country"]
        )

    airports = list(G.nodes(data=True))

    for i in range(len(airports)):
        id1, a1 = airports[i]

        for j in range(i + 1, len(airports)):
            id2, a2 = airports[j]

            distance = haversine(
                a1["latitude"],
                a1["longitude"],
                a2["latitude"],
                a2["longitude"]
            )

            if distance <= max_range_km:
                G.add_edge(
                    id1,
                    id2,
                    distance=distance
                )

    return G
