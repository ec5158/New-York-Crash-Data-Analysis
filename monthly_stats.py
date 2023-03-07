# Filename: monthly_stats.py
# Desc: This file creates bar graphs based on set parameters given by the user.
#   This program only handles bar graphs for data that represents singular months and only plots:
#    - number of accidents per [Crash Time, Borough, Day of the Week, Reason for the Crash, Vehicles Involved]
#       per month
#    - number of accidents per [Crash Time, Borough, Day of the Week, Reason for the Crash, Vehicles Involved]
#       between two different months
#
# @Author: Eric Chen
# @Date: 2023-02-24
#

import util_functions as uf
import data_analysis as da
import bar_graphs as bar
import pandas as pd
import sys
import re


def main():
    """
    This is the main driver function that handles the command line inputs

    :return: None
    """
    # The program needs to at least have a CSV file and an x-label to graph for
    if len(sys.argv) < 3:
        print("Usage: monthly_stats.py <x-label> <filename1.csv> [<filename2.csv>]")
        return

    # Gets the x-label from the command line
    xlabel = sys.argv[1]

    # These are the acceptable data to look for when making the bar graphs
    #   More will be added later
    acceptable_options = ['Vehicles', 'Crash_Time', 'Borough', 'Factor', 'Week_Day']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Vehicles', 'Crash_Time', 'Borough',"
              " 'Week_Day', or 'Factor' instead.")
        return

    # Removing the "_" makes the labels for the graph cleaner
    xlabel = xlabel.replace("_", " ")
    ylabel = 'Number of Accidents'

    # Gets the first file and its data
    csv_filename1 = sys.argv[2]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Month]_[Year].csv
    #  in order for this to work
    date1 = csv_filename1.split("_")[3] + " " + re.split('[._]', csv_filename1)[4]

    # If the number of command line arguments equals 4 then there must be a
    #   second CSV file to look at
    if len(sys.argv) == 4:
        csv_filename2 = sys.argv[3]
    else:
        csv_filename2 = " "

    # Gets an accident DataFrame from the first file
    accidentData = da.getAccidentDataFrame(data1, xlabel, date1)

    # If there is a second file, then creates a double bar graph that compares
    #   the two data sources
    if csv_filename2 != " ":
        # Gets the second file and its data
        data2 = pd.read_csv(csv_filename2)
        date2 = csv_filename2.split("_")[3] + " " + re.split('[._]', csv_filename2)[4]

        # Gets an accident DataFrame from the second file
        accidentData2 = da.getAccidentDataFrame(data2, xlabel, date2)
        # Combines the two accident DataFrames into one DataFrame
        #   i.e. the column of the number of accidents from the second file is
        #   appended onto the first
        graphableData = uf.combineData(accidentData, accidentData2, ylabel + ' ' + date2)

        # Creates the double bar graph
        bar.compareGraphs(graphableData, xlabel, ylabel, date1, date2)
    else:
        # Creates a singular bar graph of the data of accidents
        bar.makeBarGraph(accidentData, xlabel, ylabel, date1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
