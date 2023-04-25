"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name

class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        self.cities = cities
        #TODO

    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        total_distance = 0
        if len(self.cities) > 1:
            for i in range(len(self.cities) - 1):
                total_distance += self.cities[i].distance(self.cities[i + 1])
            return int(total_distance)
        else: 
            return 0

        #TODO

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        self.cities.append(city)

        #TODO

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        # find the position that results in the minimum distance
        min_distance = math.inf
        min_position = None
        for i in range(len(self.cities)):
            self.cities.insert(i, city)
            distance = self.total_distance()
            if distance < min_distance:
                min_distance = distance
                min_position = i
            self.cities.pop(i)

        # insert the city at the chosen position
        self.cities.insert(min_position, city)

    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        if len(self.cities) == 0:
            return "(0 km)"
        else:
            itinerary_str = ""
            for i in range(len(self.cities) - 1):
                itinerary_str += f"{self.cities[i].name} -> "
            itinerary_str += self.cities[-1].name
            itinerary_str += f" ({self.total_distance()} km)"
            return itinerary_str
        #TODO


if __name__ == "__main__":
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],
                           get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)
