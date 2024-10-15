from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

import load_data

"""
    Resources:
        www.google.com
        https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
        https://www.geeksforgeeks.org/setup-matplotlib-on-pycharm/
        https://matplotlib.org/basemap/stable/users/mapcoords.html
        https://jakevdp.github.io/PythonDataScienceHandbook/
        04.13-geographic-data-with-basemap.html
"""


def draw_ship_histogram() -> None:
    """
    Generates and saves a histogram of ship speeds.

    Steps:
    1. Loads ship speed data.
    2. Creates a histogram with 10 bins, blue bars, and black edges.
    3. Labels the plot with a title, x-axis as 'Speed',
       and y-axis as 'Frequency'.
    4. Saves the plot as 'speed_histogram.png' and closes
       the plot to free memory.

    Returns:
        None
    """
    data = load_data.call_search_ship_histogram_load_data()

    plt.hist(data, bins=10, color='blue', edgecolor='black')

    plt.title('Histogram of Ship Speed')
    plt.xlabel('Speed')
    plt.ylabel('Frequency')

    plt.savefig("speed_histogram.png")
    plt.close()


def draw_map() -> None:
    """
    Generates and saves a map showing ship locations.

    Steps:
    1. Plots ships using their latitude and longitude data.
    2. Saves the plot as 'ships_on_map.png' and closes it.

    Returns:
        None
    """
    # I need to adjust lat_1=0. to make the map bigger
    m = Basemap(width=12000000, height=9000000, projection='lcc',
                resolution='c', lat_1=0., lat_2=55, lat_0=50, lon_0=0.)

    m.drawmapboundary(fill_color='aqua')

    m.fillcontinents(color='coral', lake_color='aqua')

    parallels = np.arange(0., 81, 10.)

    m.drawparallels(parallels, labels=[False, True, True, False])
    meridians = np.arange(10., 351., 20.)
    m.drawmeridians(meridians, labels=[True, False, False, True])

    for key in load_data.call_search_ship_lat_lon_load_data():
        plot_ship(key[2], key[1], m)

    plt.savefig("ships_on_map.png")
    plt.close()


def plot_ship(lat: str, lon: str, m: Basemap) -> None:
    xpt, ypt = m(lon, lat)

    m.plot(xpt, ypt, 'bo')
