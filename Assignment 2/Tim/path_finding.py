"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx

from country import Country
from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    # Create a graph with all cities and their connections
    print("test")
    graph = networkx.Graph()
    for city in City.id_to_city.values():
        for destination, distance in city.get_destinations().items():
            graph.add_edge(city.id, destination.id, weight=distance)

    # Find the shortest path between from_city and to_city
    try:
        path = networkx.shortest_path(graph, from_city.id, to_city.id, weight='weight')
    except networkx.NetworkXNoPath:
        return None

    # Compute the total travel time for the given vehicle along the path
    total_time = 0
    for i in range(len(path) - 1):
        distance = get_city_by_id(path[i]).get_destinations()[path[i+1]]
        travel_time = distance / vehicle.speed
        total_time += travel_time

    # Create an itinerary object with the path and total travel time
    itinerary = Itinerary(vehicle, [get_city_by_id(city_id) for city_id in path], total_time)
    return itinerary




if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()


    Country.name_to_countries["Australia"].print_cities()

    print(City.id_to_cities)
    first_value = next(iter(City.id_to_cities.values()))
    print(first_value)

    print(get_city_by_id(1036074917))
    from_cities = set()
    for city_id in [1036074917, 1036533631, 1036192929]:
        #print(from_cities.add(get_city_by_id(city_id)))
        from_cities.add(get_city_by_id(city_id))


    #we create some vehicles
    vehicles = create_example_vehicles()
    # print("test")

    to_cities = set(from_cities)
    print(from_cities)

    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")
