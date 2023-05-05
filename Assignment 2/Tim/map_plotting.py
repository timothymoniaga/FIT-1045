from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City

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
    # Extract the list of cities from the itinerary
    cities = itinerary.get_cities()

    # Determine the map boundaries by finding the min/max coordinates
    min_lat = min(city.get_latitude() for city in cities) - 5
    max_lat = max(city.get_latitude() for city in cities) + 5
    min_lon = min(city.get_longitude() for city in cities) - 5
    max_lon = max(city.get_longitude() for city in cities) + 5

    # Ensure the map size is at least 50 degrees in each direction
    lat_diff = max_lat - min_lat
    lon_diff = max_lon - min_lon
    if lat_diff < 50:
        mid_lat = (max_lat + min_lat) / 2
        min_lat = mid_lat - 25
        max_lat = mid_lat + 25
    if lon_diff < 50:
        mid_lon = (max_lon + min_lon) / 2
        min_lon = mid_lon - 25
        max_lon = mid_lon + 25

    # Create the map using the specified projection
    m = Basemap(projection=projection, resolution='l',
                llcrnrlat=min_lat, urcrnrlat=max_lat,
                llcrnrlon=min_lon, urcrnrlon=max_lon)

    # Draw the coastlines and country borders
    m.drawcoastlines()
    m.drawcountries()

    # Draw the cities as red dots
    for city in cities:
        x, y = m(city.get_longitude(), city.get_latitude())
        m.plot(x, y, 'ro')

    # Draw lines between consecutive cities
    for i in range(len(cities) - 1):
        start_city = cities[i]
        end_city = cities[i + 1]
        start_x, start_y = m(start_city.get_longitude(), start_city.get_latitude())
        end_x, end_y = m(end_city.get_longitude(), end_city.get_latitude())
        m.plot([start_x, end_x], [start_y, end_y], color=colour, linewidth=line_width)

    # Save the map to a file with the name map_city1_city2_city3_..._cityX.png
    filename = 'map_' + '_'.join(city.get_name() for city in cities) + '.png'
    plt.savefig(filename)

    # Show the map (optional)
    plt.show()
