# Filename: util_functions.py
# Desc: This file contains some basic utility functions
#   used to manipulate and create things such as CSV files, dataframes,
#   and dictionaries.
#
# @Author: Eric Chen
# @Date: 2023-02-18
#

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime

"""
This function takes a column from one DataFrame and appends it to another DataFrame

parameters: data1 - the DataFrame the column will be added to
            data2 - the DataFrame the column of data will be extracted from
            col   - the name of the column from data2
returns: the first DataFrame will the extra column added on to it
"""
def combineData(data1, data2, col, date1, date2):
    extra_col = data2[col]
    return data1.join(extra_col, how='left', lsuffix=' '+date1, rsuffix=' '+date2)


"""

"""
def dictToDataFrame(dictionary, col1, col2):
    newDF = pd.DataFrame(dictionary.items(), columns=[col1, col2])
    return newDF


"""

"""
def timeToNum(str_time):
    nums = str_time.split(':')
    return float(nums[0]) + (float(nums[1]) / 100.00)


"""

"""
def dateToWeekDay(date):
    month, day, year = (int(x) for x in date.split('/'))
    weekday = datetime.date(year, month, day)
    return weekday.strftime("%A")


"""

"""
def createCVS(data, month, year):
    data.to_csv("csv/Motor_Vehicle_Collisions_" + month + "_" + year + ".csv")
