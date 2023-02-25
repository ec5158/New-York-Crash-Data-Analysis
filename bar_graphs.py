# Filename: bar_graphs.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-01-11
#
import matplotlib.pyplot as plt


def makeBarGraph(data, xlabel, ylabel, date):
    """

    :param data:
    :param xlabel:
    :param ylabel:
    :param date:
    :return:
    """
    x_values = data[xlabel]
    y_values = data[ylabel]

    plt.barh(x_values, y_values)

    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


def compareGraphs(data, xlabel, ylabel, date1, date2):
    """

    :param data:
    :param xlabel:
    :param ylabel:
    :param date1:
    :param date2:
    :return:
    """
    data.plot(x=xlabel, y=[ylabel + ' ' + date1, ylabel + ' ' + date2], kind="barh")
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date1 + ' and ' + date2)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()
