# Filename: bar_graphs.py
# Desc: This file handles the actual creation of bar graphs using
#   data preprocessed and cleaned in the other files.
#
# @Author: Eric Chen
# @Date: 2023-01-11
#
import matplotlib.pyplot as plt


def makeBarGraph(data, xlabel, ylabel, date):
    """
    Makes a bar graph from one data set

    :param data: the data to be plotted in a DataFrame
    :param xlabel: the x-label for the bar graph
    :param ylabel: the y-label for the bar graph (number of accidents)
    :param date: the date (month and/or year) the data represents
    :return: None
    """
    # Gets the actual values from the DataFrame
    x_values = data[xlabel]
    y_values = data[ylabel]

    # Creates a horizontal bar chart using the x and y values
    #   This is horizontal instead of a normal vertical bar graph due
    #   to how long the x-labels can be. Horizontal bar graphs have the x-
    #   labels horizontal too and readable
    plt.barh(x_values, y_values)

    # Labels the axis and adds a title to the graph
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


def compareGraphs(data, xlabel, ylabel, date1, date2):
    """
    Creates a double bar graph between two sets of data

    :param data: a DataFrame that contains values from two different sources (dates)
    :param xlabel: the x-label for the bar graph
    :param ylabel: the y-label for the bar graph (number of accidents)
    :param date1: the date (month and/or year) the first data source represents
    :param date2: the date (month and/or year) the second data source represents
    :return: None
    """
    # This uses the DataFrame as a source and differentiates the two columns by date
    #   to create a double bar graph
    data.plot(x=xlabel, y=[ylabel + ' ' + date1, ylabel + ' ' + date2], kind="barh")
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date1 + ' and ' + date2)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()
