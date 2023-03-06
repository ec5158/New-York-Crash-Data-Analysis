# Filename: accident_line_graphs.py
# Desc: This file creates line graphs based on set parameters given by the user.
#   This program only handles line graphs that plot:
#    - number of accidents per [Crash Time, Borough, Day of the Week] per year
#    - number of accidents per Crash Time per Borough for one year
#    - number of accidents per [Crash Time, Borough, Day of the Week] between two years
#    - number of accidents per [Crash Time, Borough, Day of the Week] between one year and an average of other years
#
# @Author: Eric Chen
# @Date: 2023-03-01
#
import util_functions as uf
import data_cleaning as dcl
import bar_graphs as bar
import line_graphs as line
import pandas as pd
import sys
import re


def getDataBoroughHour(data_set):
    """
    This function takes a DataFrame of crash data, sorts it by boroughs, and then produces five new
        DataFrames that represent each borough from NYC and contain the number of accidents that occurried
        during a specific time period

    :param data_set: the full DataFrame from the CSV file
    :return: a set of new DataFrames that are grouped by boroughs and contain the number of accidents per time of crash
    """
    xlabel = "Crash Time"

    # Sort the DataFrame by Borough
    data_set.sort_values(by='BOROUGH', axis=0, inplace=True)

    # Set the index to be this and don't drop
    data_set.set_index(keys=['BOROUGH'], drop=False, inplace=True)

    # Get a list of borough names
    boroughs = data_set['BOROUGH'].unique().tolist()

    # Now we can perform a lookup on a 'view' of the dataframe
    queens = data_set.loc[data_set.BOROUGH == 'QUEENS']

    new_data_set = []

    # Goes through every borough except for the undefined ones (i.e. there was no borough reported for the accident)
    for borough in boroughs[:len(boroughs) - 1]:
        # Gets a DataFrame for the current Borough that contains the time of the accident and the number of accidents
        #   that occurred during this time
        acc_data = dcl.getAccidentDataFrame(data_set.loc[data_set.BOROUGH == borough], xlabel, borough.title())
        new_data_set.append(acc_data)

    return new_data_set


def getAverageLineData(data_set, xlabel):
    # In progress
    if xlabel == "Crash Time":
        pass
    elif xlabel == "Week Day":
        pass
    elif xlabel == "Borough":
        pass


def main():
    """
    This is the main driver function that handles the command line inputs

    :return: None
    """
    # The program needs to at least have a CSV file and an x-label to graph for
    if len(sys.argv) < 3:
        print("Usage: accident_line_graphs.py <x-label> <filename1.csv> [<filename2.csv> ...]")
        return

    # Checks if the inputted x-label is something that can be graphed
    xlabel = sys.argv[1]
    acceptable_options = ['Crash_Time', 'Week_Day', 'Borough']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Week_Day', 'Borough', or 'Crash_Time' instead.")
        return

    # Removing the "_" makes the labels for the graph cleaner
    xlabel = xlabel.replace("_", " ")
    ylabel = "Number of Accidents"

    # Gets the first CSV file and converts it into a DataFrame
    csv_filename1 = sys.argv[2]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Year].csv
    #  in order for this to work
    year1 = re.split('[._]', csv_filename1)[3]
    # Turns the DataFrame into a more simplified one that only has the number of accidents that occurred sorted
    #   by the given x-label
    accidentData1 = dcl.getAccidentDataFrame(data1, xlabel, year1)

    # If there are only two CSV files then compare the two and their data
    if len(sys.argv) == 4:
        # Gets the second CSV file and converts into a DataFrame and then a more simplified one
        #   with only the number of accidents sorted by the given xlabel
        csv_filename2 = sys.argv[3]
        data2 = pd.read_csv(csv_filename2)
        year2 = re.split('[._]', csv_filename2)[3]
        accidentData2 = dcl.getAccidentDataFrame(data2, xlabel, year2)

        # The data is put into lists as the makeMultipleLineGraphs method uses lists
        comparableData = [accidentData1, accidentData2]
        yearSet = [year1, year2]

        # Creates the line graph using the data
        line.makeMultipleLineGraphs(comparableData, xlabel, ylabel, yearSet, year1 + " and " + year2)
    # If there is more than two CSV files, then take the average of the CSV files following
    #   the first one and compare it to the first one
    # TODO: Get averages
    elif len(sys.argv) > 4:
        dataSet = []
        for file in sys.argv[3:]:
            new_data = pd.read_csv(file)
            dataSet.append(new_data)

        df_year = uf.dictToDataFrame(getAverageLineData(dataSet, xlabel), xlabel, ylabel + ' ' + year1)
        comparableData = uf.combineData(accidentData1, df_year, ylabel + ' ' + year1)
        bar.compareGraphs(comparableData, xlabel, ylabel, year1, "Average")
    # If there is only one CSV file inputted then create a graph for it alone
    else:
        # Borough is a special case where the x-axis is actually the time of the crash and
        #   instead every borough's accidents from that year are compared with one another
        if xlabel == "Borough":
            accidentData1 = getDataBoroughHour(data1)

            xlabel = "Crash Time"
            line.makeMultipleLineGraphs(accidentData1, xlabel, ylabel, dcl.boroughs, year1)
        else:
            line.makeLineGraph(accidentData1, xlabel, ylabel, year1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
