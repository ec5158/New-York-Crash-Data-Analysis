# Filename: line_graphs.py
# Desc: This file handles the actual creation of line graphs using
#   data preprocessed and cleaned in the other files.
#
# @Author: Eric Chen
# @Date: 2023-03-01
#
import matplotlib.pyplot as plt
import data_cleaning as dcl


def makeLineGraph(data, xlabel, ylabel, date):
    """
    Creates a line graph from the DataFrame plotted using a given
        x-label and y-label

    :param data: the DataFrame of two columns - x-label and y-label
    :param xlabel: the name of the column that holds the values to be plotted as the x_values
    :param ylabel: the name of the column that holds the values to be plotted as the x_values
    :param date: the date (likely to be the year) the data represents
    :return: None
    """
    # Gets the actual values from the DataFrame
    x_values = data[xlabel]
    y_values = data[ylabel + " " + date]

    # Plots the data
    plt.plot(x_values, y_values)

    # Rotates the x-axis ticks so that they don't overlap
    plt.xticks(rotation=45)
    # Labels the axis
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Car Accident Info for ' + date)
    # Optional: used to create a more permanent version of the line graph
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


def makeMultipleLineGraphs(dataSet, xlabel, ylabel, labelSet, title):
    """
    Creates a line graph with multiple data sources or a single data source with
        multiple options

    :param dataSet: a list of DataFrames
    :param xlabel: the label for the x-axis
    :param ylabel: the label for the y-axis
    :param labelSet: a list of names for each different line of data for the legend
    :param title: the name of the new graph (usually the time period being looked at)
    :return: None
    """
    # Used to iterate through the list of line labels
    count = 0

    # Goes through every DataFrame in the list of data and adds the values to the graph
    #   as a separate line for each DataFrame
    for data in dataSet:
        x_values = data[xlabel]
        y_values = data[ylabel + " " + labelSet[count]]

        plt.plot(x_values, y_values, label=labelSet[count])
        count += 1

    # Rotates the x-axis ticks so that they don't overlap
    plt.xticks(rotation=45)
    # Labels the axis
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Places the legend in the upper right corner
    plt.legend(loc="upper right")
    plt.title('Car Accident Info for ' + title)
    # Optional: used to create a more permanent version of the line graph
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()
