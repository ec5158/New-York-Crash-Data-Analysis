# Filename: monthly_stats.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-02-24
#
import util_functions as uf
import data_cleaning as dcl
import bar_graphs as bar
import pandas as pd
import sys
import re


def main():
    """

    :return:
    """
    if len(sys.argv) < 3:
        print("Usage: monthly_stats.py <x-label> <filename1.csv> [<filename2.csv>]")
        return

    xlabel = sys.argv[1]

    # These are the acceptable data to look for when making the bar graphs
    # More will be added later
    acceptable_options = ['Vehicles', 'Crash_Time', 'Borough', 'Factor', 'Week_Day']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Vehicles', 'Crash_Time', 'Borough',"
              " 'Week_Day', or 'Factor' instead.")
        return

    xlabel = xlabel.replace("_", " ")
    ylabel = 'Number of Accidents'

    csv_filename1 = sys.argv[2]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Month]_[Year].csv
    #  in order for this to work
    date1 = csv_filename1.split("_")[3] + " " + re.split('[._]', csv_filename1)[4]

    if len(sys.argv) == 4:
        csv_filename2 = sys.argv[3]
    else:
        csv_filename2 = " "

    accidentData = dcl.getAccidentDataFrame(data1, xlabel, date1)

    if csv_filename2 != " ":
        data2 = pd.read_csv(csv_filename2)
        date2 = csv_filename2.split("_")[3] + " " + re.split('[._]', csv_filename2)[4]

        accidentData2 = dcl.getAccidentDataFrame(data2, xlabel, date2)
        graphableData = uf.combineData(accidentData, accidentData2, ylabel + ' ' + date2)

        print(graphableData.to_string())
        bar.compareGraphs(graphableData, xlabel, ylabel, date1, date2)
    else:
        print(accidentData.to_string())
        bar.makeBarGraph(accidentData, xlabel, ylabel, date1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
