# Filename: avg_num_crashes_per_month.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-02-22
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import data_cleaning
import util_functions as uf
import re


"""

"""
def main():
    if len(sys.argv) < 2:
        print("Usage: avg_num_crashes_per_month.py filename1.csv [filename2.csv]")
        return

    csv_filename1 = sys.argv[1]
    data1 = pd.read_csv(csv_filename1)
    # File name should follow the format Motor_Vehicle_Collisions_[Year].csv
    #  in order for this to work
    year1 = csv_filename1.split("_")[3]

    if len(sys.argv) > 2:
        csv_filename2 = sys.argv[2]

    print(year1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()