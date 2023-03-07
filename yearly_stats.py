# Filename: yearly_stats.py
# Desc: This file creates bar graphs based on set parameters given by the user.
#   This program only handles bar graphs for data that represents years and only plots:
#    - number of accidents per [Months, Day of the Week] for a single year
#    - number of accidents per [Months, Day of the Week] between two different years
#    - number of accidents per [Months, Day of the Week] between one year and an average of other years
#
# @Author: Eric Chen
# @Date: 2023-02-22
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
        print("Usage: yearly_stats.py <x-label> <filename1.csv> [<filename2.csv> ...]")
        return

    # Gets the x-label from the command line
    xlabel = sys.argv[1]

    # These are the acceptable data to look for when making the bar graphs
    #   More will be added later
    acceptable_options = ['Months', 'Week_Day']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Week_Day' or 'Months' instead.")
        return

    # Removing the "_" makes the labels for the graph cleaner
    xlabel = xlabel.replace("_", " ")
    ylabel = "Number of Accidents"

    # Gets the first file and its data
    csv_filename1 = sys.argv[2]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Year].csv
    #  in order for this to work
    year1 = re.split('[._]', csv_filename1)[3]

    # Gets an accident DataFrame from the first file
    accidentData1 = da.getAccidentDataFrame(data1, xlabel, year1)

    # If there are only two CSV files then compare the two and their data
    if len(sys.argv) == 4:
        # Gets the second CSV file and converts into a DataFrame and then a more simplified one
        #   with only the number of accidents sorted by the given xlabel
        csv_filename2 = sys.argv[3]
        data2 = pd.read_csv(csv_filename2)
        year2 = re.split('[._]', csv_filename2)[3]
        accidentData2 = da.getAccidentDataFrame(data2, xlabel, year2)

        # Combines the two data sets by taking the number of accidents from the second DataFrame
        #   and appending it to the first
        comparableData = uf.combineData(accidentData1, accidentData2, ylabel + ' ' + year2)

        # Creates the double bar graph using the data
        bar.compareGraphs(comparableData, xlabel, ylabel, year1, year2)
    # If there is more than two CSV files, then take the average of the CSV files following
    #   the first one and compare it to the first one
    elif len(sys.argv) > 4:
        # Creates a list of DataFrames that represents every year given
        dataSet = []
        for file in sys.argv[3:]:
            new_data = pd.read_csv(file)
            dataSet.append(new_data)

        # Gets the average number of accidents of all the years sorted by the given xlabel
        df_year = uf.dictToDataFrame(da.getAverageData(dataSet, xlabel), xlabel, ylabel + " Average")

        # Combines the two data sets by taking the number of accidents from the second DataFrame
        #   and appending it to the first
        comparableData = uf.combineData(accidentData1, df_year, ylabel + " Average")

        # Creates the double bar graph using the data
        bar.compareGraphs(comparableData, xlabel, ylabel, year1, "Average")
    # If there is only one CSV file inputted then create a graph for it alone
    else:
        bar.makeBarGraph(accidentData1, xlabel, ylabel, year1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
