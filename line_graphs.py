# Filename: line_graphs.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-03-01
#
import matplotlib.pyplot as plt
import data_cleaning as dcl

def makeLineGraph(data, xlabel, ylabel, date):
    """

    :param data:
    :param xlabel:
    :param ylabel:
    :param date:
    :return:
    """
    x_values = data[xlabel]
    y_values = data[ylabel + " " + date]

    plt.plot(x_values, y_values)

    plt.xticks(rotation=45)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Car Accident Info for ' + date)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


def makeMultipleLineGraphs(dataSet, xlabel, ylabel, labelSet, title):
    """

    :param dataSet:
    :param xlabel:
    :param ylabel:
    :param labelSet:
    :param title:
    :return:
    """
    count = 0

    for data in dataSet:
        x_values = data[xlabel]
        y_values = data[ylabel + " " + labelSet[count]]

        plt.plot(x_values, y_values, label=dcl.boroughs[count])
        count += 1

    plt.xticks(rotation=45)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="upper right")
    plt.title('Car Accident Info for ' + title)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()
