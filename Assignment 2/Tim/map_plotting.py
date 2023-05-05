from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City, create_example_cities, get_cities_by_name

def plot_itinerary(itinerary: Itinerary, projection='robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """
    # Get the list of cities from the itinerary
    cities: List[City] = itinerary.cities

    # Define the file name for the plot
    file_name = f"map_{'_'.join([c.name for c in cities])}.png"

    # Define the map bounds
    min_lat, min_lon = min([c.coordinates[0] for c in cities]), min([c.coordinates[1] for c in cities])
    max_lat, max_lon = max([c.coordinates[0] for c in cities]), max([c.coordinates[1] for c in cities])
    extra_padding = 5
    min_lat, max_lat = min_lat - extra_padding, max_lat + extra_padding
    min_lon, max_lon = min_lon - extra_padding, max_lon + extra_padding

    # Ensure a minimum size of 50 degrees in each direction
    if max_lon - min_lon < 50:
        avg_lon = (max_lon + min_lon) / 2
        min_lon, max_lon = avg_lon - 25, avg_lon + 25
    if max_lat - min_lat < 50:
        avg_lat = (max_lat + min_lat) / 2
        min_lat, max_lat = avg_lat - 25, avg_lat + 25

    # Define the map projection and size
    m = Basemap(projection=projection, lon_0=0, resolution='l')
    plt.figure(figsize=(10, 8))

    # Draw the map features
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='beige', lake_color='lightblue')
    m.drawmapboundary(fill_color='lightblue')

    # Draw the cities and the itinerary
    for city in cities:
        x, y = m(city.coordinates[1], city.coordinates[0])
        m.plot(x, y, 'bo', markersize=6)
        plt.text(x, y, city.name, fontsize=10, fontweight='bold', ha='center', va='center')
    for i in range(len(cities) - 1):
        city1, city2 = cities[i], cities[i + 1]
        x1, y1 = m(city1.coordinates[1], city1.coordinates[0])
        x2, y2 = m(city2.coordinates[1], city2.coordinates[0])
        m.drawgreatcircle(x1, y1, x2, y2, linewidth=line_width, color=colour)

    # Save the plot to file
    plt.savefig(file_name)
    plt.show

if __name__ == "__main__":
    city_list = list()
    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))
