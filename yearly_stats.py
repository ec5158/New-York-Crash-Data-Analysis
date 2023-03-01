# Filename: yearly_stats.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-02-22
#
import util_functions as uf
import data_cleaning as dcl
import bar_graphs as bar
import pandas as pd
import sys
import re


def getAverageDataWeekDay(week_set):
    xlabel = "Week Day"

    week_dict = dict()

    for day in dcl.days_of_the_week:
        week_dict[day] = 0

    for year in week_set:
        newData = dcl.getAccidentDataFrame(year, xlabel, "")
        rowCount = 0
        for row in newData.iterrows():
            week_dict[dcl.days_of_the_week[rowCount]] += row[1][1]
            rowCount += 1

    for day in dcl.days_of_the_week:
        week_dict[day] //= len(week_set)

    return week_dict


def getAverageDataMonth(year_set):
    """

    :param year_set:
    :return:
    """
    xlabel = "Months"

    year_dict = dict()

    for month in dcl.months:
        year_dict[month] = 0

    for year in year_set:
        newData = dcl.getAccidentDataFrame(year, xlabel, "")
        rowCount = 0
        for row in newData.iterrows():
            year_dict[dcl.months[rowCount]] += row[1][1]
            rowCount += 1

    for month in dcl.months:
        year_dict[month] //= len(year_set)

    return year_dict

def getAverageData(data_set, xlabel):
    if xlabel == "Months":
        return getAverageDataMonth(data_set)
    elif xlabel == "Week Day":
        return getAverageDataWeekDay(data_set)


def main():
    """

    :return:
    """
    if len(sys.argv) < 3:
        print("Usage: yearly_stats.py <x-label> <filename1.csv> [<filename2.csv> ...]")
        return

    xlabel = sys.argv[1]
    acceptable_options = ['Months', 'Week_Day']
    if xlabel not in acceptable_options:
        print("Current x-label is unusable for graphing. Try 'Week_Day' or 'Months' instead.")
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
        comparableData = uf.combineData(accidentData1, accidentData2, ylabel + ' ' + year2)
        bar.compareGraphs(comparableData, xlabel, ylabel, year1, year2)
    elif len(sys.argv) > 4:
        dataSet = []
        for file in sys.argv[3:]:
            new_data = pd.read_csv(file)
            dataSet.append(new_data)
        df_year = uf.dictToDataFrame(getAverageData(dataSet, xlabel), xlabel, ylabel + " Average")
        comparableData = uf.combineData(accidentData1, df_year, ylabel + " Average")
        bar.compareGraphs(comparableData, xlabel, ylabel, year1, "Average")
    else:
        bar.makeBarGraph(accidentData1, xlabel, ylabel, year1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
