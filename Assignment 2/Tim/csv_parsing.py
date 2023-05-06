"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country, add_city_to_country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    with open(path_to_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract fields from the row
            city_name = row['city_ascii']
            latitude = float(row['lat'])
            longitude = float(row['lng'])
            country_name = row['country']
            iso3 = row['iso3']
            city_type = row['capital']
            population = row['population']
            city_id = row['id']
            location = (latitude, longitude)

            # Convert population to an integer
            if population == '':
                population = 0
            else:
                population = int(population)

            # Create City and Country instances
            city = City(city_name, location, city_type, population, city_id)
            #country = Country(country_name, iso3)
            #country.add_city(city)
            add_city_to_country(city, country_name, iso3)
            #print(city)
            #Country.name_to_countries["Australia"].print_cities()

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()