# Filename: util_functions.py
# Desc: This file contains some basic utility functions
#   used to manipulate and create things such as CSV files, dataframes,
#   and dictionaries.
#
# @Author: Eric Chen
# @Date: 2023-02-18
#

import pandas as pd
import datetime


def combineData(data1, data2, col):
    """
    This function takes a column from one DataFrame and appends it to another DataFrame

    :param data1: the DataFrame the column will be added to
    :param data2: the DataFrame the column of data will be extracted from
    :param col: the name of the column from data2
    :return: the first DataFrame will the extra column added on to it
    """
    # Finds the column
    extra_col = data2[col]
    # Appends it to the first DataFrame
    data1[col] = extra_col
    return data1


def dictToDataFrame(dictionary, col1, col2):
    """
    Converts a given dictionary into a DataFrame of two columns with
        the two names given as col1 and col2

    :param dictionary: the dictionary to be converted
    :param col1: the name of the keys from the dictionary (the first column of the DataFrame)
    :param col2: the name of the values from the dictionary (the second column of the DataFrame)
    :return: a DataFrame with the data from the dictionary represented as two columns
    """
    # Creates a new DataFrame from the dictionary with the column names col1 and col2
    newDF = pd.DataFrame(dictionary.items(), columns=[col1, col2])
    return newDF


def timeToNum(str_time):
    """
    Converts a string in the format of 00:00 into a numeric value with format of 00.00

    :param str_time: the string in the format 00:00
    :return: the time as a float in the format 00.00
    """
    # Splits the original string into numbers without the :
    nums = str_time.split(':')
    # Returns the number into a float (Ex: The string 12:32 would become the float 12.32)
    return float(nums[0]) + (float(nums[1]) / 100.00)


def dateToWeekDay(date):
    """
    Gets the day of the week (Monday, Tuesday, etc.) from a date in the format MM/DD/YYYY

    :param date: the date in the format MM/DD/YYYY
    :return: the corresponding day of the week the date matches to
    """
    # Splits the original date string into individual strings of month, day, and year
    month, day, year = (int(x) for x in date.split('/'))
    # Uses the month, day, and year to calculate the date as a datetime object
    weekday = datetime.date(year, month, day)
    # Returns only the day of the week
    return weekday.strftime("%A")


def createCSV(data, month, year):
    """
    Creates a CSV file from a given DataFrame

    :param data: the DataFrame the CSV file will contain
    :param month: the month the data represents if it represents a month at all
    :param year: the year the data represents
    :return: a CSV file of the data
    """
    # If there is no month given then the data must represent only a year
    if month == "":
        data.to_csv("csv/Motor_Vehicle_Collisions_" + year + ".csv")
    else:
        data.to_csv("csv/Motor_Vehicle_Collisions_" + month + "_" + year + ".csv")
