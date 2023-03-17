# Filename: heat_map.py
# Desc: This file creates a heat map about the motor accidents in NYC using
#   kernel density estimation for a given year and/or month
#
# @Author: Eric Chen
# @Date: 2023-03-10
#

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns
import sys
import re


def getCoordinates(data):
    """
    Creates a dictionary consisting of keys - the coordinates where the
        accident occurred and values - the number of times an accident occurred there

    :param: the original data in a DataFrame
    :return: a dictionary - (coordinates of the accident, number of occurrences)
    """
    # Gets the longitude and latitude of every accident
    longitude = data["LONGITUDE"]
    latitude = data["LATITUDE"]

    locations = dict()
    count = 0

    # For every latitude in the data set
    for lat in latitude:
        # Only adds the coordinates if the latitude
        #   exists and is not zero
        if not pd.isnull(lat) and lat != 0.0:
            # If the latitude exists then assume the longitude
            #   also exists
            loc = (lat, longitude[count])
            # Increases the number of accidents at that coordinate
            if loc in locations.keys():
                locations[loc] += 1
            # Creates a new key-value pair of the new coordinate
            else:
                locations[loc] = 1

        count += 1

    return locations


def main():
    """
    This is the main driver function that handles the command line inputs

    :return: None
    """
    # The program needs to at least have a CSV file to find a heat map for
    if len(sys.argv) < 2:
        print("Usage: heat_map.py <filename1.csv>")
        return

    # Gets the file name and the data itself
    filename = sys.argv[1]
    data = pd.read_csv(filename)

    # Gets the date the data represents
    # File name should follow the format Motor_Vehicle_Collisions_[Month]_[Year].csv
    #  or Motor_Vehicle_Collisions_[Year].csv in order for this to work
    date = re.split('[._]', filename)
    # If the length is 6 elements in the list then it must be in the format
    #   Motor_Vehicle_Collisions_[Month]_[Year].csv
    if len(date) == 6:
        date = date[3] + " " + date[4]
    else:
        date = date[3]

    # Gets the coordinates (longitude and latitude) of the accidents
    #   Removes any null values (coordinates are not available)
    #   and any 0 values that would skew the kernel density estimation
    longitude = [x for x in data["LONGITUDE"] if not pd.isnull(x) and x != 0.0]
    latitude = [x for x in data["LATITUDE"] if not pd.isnull(x) and x != 0.0]

    # Get a background map of the New York City Boroughs
    df = gpd.read_file(gpd.datasets.get_path('nybb'))
    # Set the parameters of the map to fit proper longitude and latitude coordinates
    df_wm = df.to_crs(epsg=4326)
    # Adds the background map to the graph
    ax = df_wm.plot(figsize=(10, 10), alpha=0.6, edgecolor='k')

    # Performs Kernel Density Estimation and plots the results
    kde = sns.kdeplot(
        ax=ax,
        x=longitude,
        y=latitude,
        fill=True,
        cmap='Reds',
        alpha=0.8
    )

    # Removes the x-axis and y-axis from the graph
    #   Can comment this out if coordinates need to be seen
    ax.set_axis_off()

    # Set the limits of the x-axis and y-axis to focus only on the
    #   coordinates of New York City
    plt.xlim(-74.26, -73.5)
    plt.ylim(40.47, 41.0)
    plt.tight_layout()
    plt.title("Heat Map of Motor Vehicle Accidents for New York City during " + date)

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
