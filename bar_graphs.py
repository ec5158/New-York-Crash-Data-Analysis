# Filename: bar_graphs.py
# Desc:
#
# TODO: Clean up bar_graphs.py, make it more flexible for different months and csv files
# @Author: Eric Chen
# @Date: 2023-01-11
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import data_cleaning


"""

"""
def makeBarGraph(data, xlabel, ylabel, date):
    if xlabel == 'CRASH TIME':
        data = data_cleaning.simplifyTime(data)

    df = pd.DataFrame(data)

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Add x, y gridlines
    ax.grid(visible=True, color='black',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    x_values = df[xlabel]
    y_values = df[ylabel]

    plt.barh(x_values, y_values)

    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


"""

"""
def compareGraphs(data, xlabel, ylabel, date1, date2):
    data.plot(x=xlabel, y=[date1, date2], kind="barh")
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date1 + ' and ' + date2)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


"""

"""
def main():
    if len(sys.argv) < 2:
        print("Usage: bar_graphs.py filename1.csv [filename2.csv]")
        return

    csv_filename1 = sys.argv[1]
    data1 = pd.read_csv(csv_filename1)

    if len(sys.argv) > 2:
        csv_filename2 = sys.argv[2]
        data2 = pd.read_csv(csv_filename2)
        accidentData = data_cleaning.dictToDataFrame(data_cleaning.accidentByVehicle(data1), 'Vehicles', 'Number of Accidents')
        accidentData2 = data_cleaning.dictToDataFrame(data_cleaning.accidentByVehicle(data2), 'Vehicles', 'Number of Accidents')
        graphableData = data_cleaning.combineData(accidentData, accidentData2, 'Number of Accidents', ' April 2021', ' August 2021')
        print(graphableData.to_string())
        compareGraphs(graphableData, 'Vehicles', 'Number of Accidents', 'Number of Accidents April 2021', 'Number of Accidents August 2021')
    else:
        accidentData = data_cleaning.dictToDataFrame(data_cleaning.accidentByVehicle(data1), 'Vehicles', 'Number of Accidents')
        makeBarGraph(accidentData, 'Vehicles', 'Number of Accidents', 'August 2021')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()