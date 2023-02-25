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


def main():
    """

    :return:
    """
    if len(sys.argv) < 2:
        print("Usage: yearly_stats.py filename1.csv [filename2.csv]")
        return

    csv_filename1 = sys.argv[1]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Year].csv
    #  in order for this to work
    year1 = re.split('[._]', csv_filename1)[3]
    accidentData1 = dcl.getAccidentDataFrame(data1, "Months")

    if len(sys.argv) > 2:
        csv_filename2 = sys.argv[2]
        data2 = pd.read_csv(csv_filename2)
        year2 = re.split('[._]', csv_filename2)[3]
        accidentData2 = dcl.getAccidentDataFrame(data2, "Months")
        comparableData = uf.combineData(accidentData1, accidentData2, 'Number of Accidents', year1, year2)
        bar.compareGraphs(comparableData, "Months", 'Number of Accidents', year1, year2)
    else:
        bar.makeBarGraph(accidentData1, "Months", "Number of Accidents", year1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
