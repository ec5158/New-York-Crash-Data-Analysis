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
import data_cleaning as dcl
import data_analysis as da
import bar_graphs as bar
import pandas as pd
import sys
import re


def getAverageDataWeekDay(week_set):
    """
    Creates a dictionary containing the average number of accidents
        that happen on a specific day of the week for multiple years

    :param week_set: a list containing DataFrames of different years
    :return: a dictionary containing the days of the week and the average number of accidents
             that occurred on that day over multiple years
    """
    xlabel = "Week Day"

    week_dict = dict()

    # For every day in days_of_the_week create a key with empty values
    for day in dcl.days_of_the_week:
        week_dict[day] = 0

    # Goes through every DataFrame given in the list, year by year
    for year in week_set:
        # Creates a new DataFrame of the number of accidents that occurred every
        #   day of the week for the given year
        newData = da.getAccidentDataFrame(year, xlabel, "")

        rowCount = 0
        # For every accident, gets the number of accidents that occurred and
        #   the day of the week it occurred
        for row in newData.iterrows():
            week_dict[dcl.days_of_the_week[rowCount]] += row[1][1]
            rowCount += 1

    # After getting all the number of accidents sorted by day of the week
    #   divide by the number of years used to get the average
    for day in dcl.days_of_the_week:
        week_dict[day] //= len(week_set)

    return week_dict


def getAverageDataMonth(year_set):
    """
    Creates a dictionary containing the average number of accidents
        that happen on a specific month for multiple years

    :param year_set: a list containing DataFrames of different years
    :return: a dictionary containing the months and the average number of accidents
             that occurred on those months over multiple years
    """
    xlabel = "Months"

    year_dict = dict()

    # For every month in months create a key with empty values
    for month in dcl.months:
        year_dict[month] = 0

    # Goes through every DataFrame given in the list, year by year
    for year in year_set:
        # Creates a new DataFrame of the number of accidents that occurred every
        #   month for the given year
        newData = da.getAccidentDataFrame(year, xlabel, "")

        rowCount = 0
        # For every accident, gets the number of accidents that occurred and
        #   the month it occurred
        for row in newData.iterrows():
            year_dict[dcl.months[rowCount]] += row[1][1]
            rowCount += 1

    # After getting all the number of accidents sorted by months
    #   divide by the number of years used to get the average
    for month in dcl.months:
        year_dict[month] //= len(year_set)

    return year_dict


def getAverageData(data_set, xlabel):
    """
    Helper function to get the right data analysis algorithm and
        create the desired dictionary of average data

    :param data_set: the list containing multiple DataFrames
    :param xlabel: the label/category to search with
    :return:
    """
    if xlabel == "Months":
        return getAverageDataMonth(data_set)
    elif xlabel == "Week Day":
        return getAverageDataWeekDay(data_set)


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
        df_year = uf.dictToDataFrame(getAverageData(dataSet, xlabel), xlabel, ylabel + " Average")

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
