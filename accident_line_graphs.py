# Filename: accident_line_graphs.py
# Desc:
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

    for borough in boroughs[:len(boroughs) - 1]:
        acc_data = dcl.getAccidentDataFrame(data_set.loc[data_set.BOROUGH == borough], xlabel, borough.title())
        new_data_set.append(acc_data)

    return new_data_set


def getLineData(data_set, xlabel):
    if xlabel == "Crash Time":
        pass
    elif xlabel == "Week Day":
        pass
    elif xlabel == "Borough":
        return getDataBoroughHour(data_set)


def main():
    """

    :return:
    """
    if len(sys.argv) < 3:
        print("Usage: accident_line_graphs.py <x-label> <filename1.csv> [<filename2.csv> ...]")
        return

    xlabel = sys.argv[1]
    acceptable_options = ['Crash_Time', 'Week_Day', 'Borough']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Week_Day', 'Borough', or 'Crash_Time' instead.")
        return

    xlabel = xlabel.replace("_", " ")
    ylabel = "Number of Accidents"

    csv_filename1 = sys.argv[2]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Year].csv
    #  in order for this to work
    year1 = re.split('[._]', csv_filename1)[3]
    accidentData1 = dcl.getAccidentDataFrame(data1, xlabel, year1)

    if len(sys.argv) == 4:
        csv_filename2 = sys.argv[3]
        data2 = pd.read_csv(csv_filename2)
        year2 = re.split('[._]', csv_filename2)[3]
        accidentData2 = dcl.getAccidentDataFrame(data2, xlabel, year2)
        comparableData = [accidentData1, accidentData2]
        yearSet = [year1, year2]
        line.makeMultipleLineGraphs(comparableData, xlabel, ylabel, yearSet, yearSet[0])
    elif len(sys.argv) > 4:
        # TODO: Edit the following from average to just one year
        dataSet = []
        for file in sys.argv[3:]:
            new_data = pd.read_csv(file)
            dataSet.append(new_data)
        df_year = uf.dictToDataFrame(getLineData(dataSet, xlabel), xlabel, ylabel + ' ' + year1)
        comparableData = uf.combineData(accidentData1, df_year, ylabel + ' ' + year1)
        bar.compareGraphs(comparableData, xlabel, ylabel, year1, "Average")
    else:
        if xlabel == "Borough":
            accidentData1 = getDataBoroughHour(data1)
            xlabel = "Crash Time"
            line.makeMultipleLineGraphs(accidentData1, xlabel, ylabel, dcl.boroughs, year1)
        else:
            line.makeLineGraph(accidentData1, xlabel, ylabel, year1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
