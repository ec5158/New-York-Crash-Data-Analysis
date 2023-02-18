# Filename: bar_graphs.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-01-11
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import data_cleaning
import re


"""

"""
def makeBarGraph(data, xlabel, ylabel, date):
    x_values = data[xlabel]
    y_values = data[ylabel]

    plt.barh(x_values, y_values)

    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


"""

"""
def compareGraphs(data, xlabel, ylabel, date1, date2):
    data.plot(x=xlabel, y=[ylabel + ' ' + date1, ylabel + ' ' + date2], kind="barh")
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date1 + ' and ' + date2)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


"""

"""
def main():
    if len(sys.argv) < 3:
        print("Usage: bar_graphs.py filename1.csv [filename2.csv] x-label")
        return

    csv_filename1 = sys.argv[1]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Month]_[Year].csv
    #  in order for this to work
    date1 = csv_filename1.split("_")[3] + " " + re.split('[._]', csv_filename1)[4]

    next = sys.argv[2]
    csv_filename2 = " "

    if next[len(next) - 4:] == ".csv":
        csv_filename2 = next
        xlabel = sys.argv[3]
    else:
        xlabel = next

    # These are the acceptable data to look for when making the bar graphs
    # More will be added later
    acceptable_options = ['Vehicles', 'CRASH_TIME']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Vehicles' or 'CRASH_TIME' instead.")
        return

    xlabel = xlabel.replace("_", " ")

    if csv_filename2 != " ":
        data2 = pd.read_csv(csv_filename2)
        date2 = csv_filename2.split("_")[3] + " " + re.split('[._]', csv_filename2)[4]

        accidentData = data_cleaning.getAccidentDataFrame(data1, xlabel)
        accidentData2 = data_cleaning.getAccidentDataFrame(data2, xlabel)
        graphableData = data_cleaning.combineData(accidentData, accidentData2, 'Number of Accidents', date1, date2)
        print(graphableData.to_string())
        compareGraphs(graphableData, xlabel, 'Number of Accidents', date1, date2)
    else:
        accidentData = data_cleaning.getAccidentDataFrame(data1, xlabel)
        print(accidentData.to_string())
        makeBarGraph(accidentData, xlabel, 'Number of Accidents', date1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()