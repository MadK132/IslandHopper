
import networkx as nx


def shortest_route(G, start, destination):
    """Find a route with the minimum number of flights."""
    try:
        return nx.shortest_path(
            G,
            source=start,
            target=destination
        )
    except nx.NetworkXNoPath:
        return None


def calculate_flight_time(G, airport1, airport2, customs_hours=2):
    """Calculate flight time, including customs when crossing borders."""
    edge = G[airport1][airport2]

    distance = edge["distance"]
    flight_time = distance / 500

    country1 = G.nodes[airport1]["country"]
    country2 = G.nodes[airport2]["country"]

    if country1 != country2:
        flight_time += customs_hours

    return flight_time


def fastest_route(G, start, destination, customs_hours=2):
    """Find the fastest route using Dijkstra."""
    def weight(u, v, edge):
        flight_time = edge["distance"] / 500

        country1 = G.nodes[u]["country"]
        country2 = G.nodes[v]["country"]

        if country1 != country2:
            flight_time += customs_hours

        flight_time += 1

        return flight_time

    try:
        return nx.dijkstra_path(
            G,
            source=start,
            target=destination,
            weight=weight
        )
    except nx.NetworkXNoPath:
        return None


def route_statistics(G, route, customs_hours=2):
    """Calculate total distance, flight time and stop count."""
    if route is None:
        return None

    total_distance = 0
    total_time = 0

    for i in range(len(route) - 1):
        airport1 = route[i]
        airport2 = route[i + 1]

        distance = G[airport1][airport2]["distance"]

        total_distance += distance
        total_time += calculate_flight_time(
            G, airport1, airport2, customs_hours
        )

    stops = max(0, len(route) - 2)
    total_time += stops  

    return {
        "distance_km": total_distance,
        "time_hours": total_time,
        "flights": max(0, len(route) - 1),
        "stops": stops
    }


def farthest_reachable(G, start, max_stops=10):
    """Find the farthest reachable airport within the stop limit."""
    max_flights = max_stops + 1

    reachable = nx.single_source_shortest_path_length(
        G, source=start, cutoff=max_flights
    )

    candidates = [
        airport for airport in reachable
        if airport != start
    ]

    if not candidates:
        return None

    from distances import haversine

    source = G.nodes[start]

    return max(
        candidates,
        key=lambda airport: haversine(
            source["latitude"],
            source["longitude"],
            G.nodes[airport]["latitude"],
            G.nodes[airport]["longitude"]
        )
    )
