# Filename: main.py
# Desc:
#
#
# @Author: Eric Chen
# @Date: 2023-01-11
#
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# The columns for the crash data
columns = ["ID", "CRASH DATE", "CRASH TIME", "BOROUGH", "ZIP CODE", "LATITUDE", "LONGITUDE", "LOCATION",
           "ON STREET NAME", "CROSS STREET NAME", "OFF STREET NAME", "NUMBER OF PERSONS INJURED",
           "NUMBER OF PERSONS KILLED", "NUMBER OF PEDESTRIANS INJURED", "NUMBER OF PEDESTRIANS KILLED",
           "NUMBER OF CYCLIST INJURED", "NUMBER OF CYCLIST KILLED", "NUMBER OF MOTORIST INJURED",
           "NUMBER OF MOTORIST KILLED", "CONTRIBUTING FACTOR VEHICLE 1", "CONTRIBUTING FACTOR VEHICLE 2",
           "CONTRIBUTING FACTOR VEHICLE 3", "CONTRIBUTING FACTOR VEHICLE 4", "CONTRIBUTING FACTOR VEHICLE 5",
           "COLLISION_ID", "VEHICLE TYPE CODE 1", "VEHICLE TYPE CODE 2", "VEHICLE TYPE CODE 3", "VEHICLE TYPE CODE 4",
           "VEHICLE TYPE CODE 5"]

"""

"""
def getYearData(data, year):
    rowList = []

    for row in data.iterrows():
        crashDate = row[1][0]
        dataAspects = crashDate.split("/")
        if dataAspects[0] != "CRASH DATE":
            if dataAspects[2] == year:
                rowList.append(row[1])

    return pd.DataFrame.from_records(rowList)

"""

"""
def getMonthData(data, month, year):
    rowList = []

    for row in data.iterrows():
        crashDate = row[1][0]
        dataAspects = crashDate.split("/")
        if dataAspects[0] != "CRASH DATE":
            if dataAspects[0] == month and dataAspects[2] == year:
                rowList.append(row[1])

    return pd.DataFrame.from_records(rowList)

"""

"""
def cleanData(data):
    rowCount = 0
    for row in data.iterrows():
        row = row[1]
        colCount = 0
        for columns in data.items():
            current = row[colCount]
            if isinstance(current, str):
                current = current.rstrip()
                data.iloc[rowCount, colCount] = current
                if current == 'Unspecified':
                    data.iloc[rowCount, colCount] = np.NaN
            if pd.isnull(current):
                data.iloc[rowCount, colCount] = np.NaN
            colCount += 1
        rowCount += 1
    return data


"""

"""
def createCVS(data, month, year):
    data.to_csv("cvs/Motor_Vehicle_Collisions_" + month + "_" + year + ".csv")


"""

"""
def main():
    try:
        csv_filename = sys.argv[1]
    except:
        print("Usage: main.py [csv_filename]")
        return
    data = pd.read_csv(csv_filename)
    year2021 = getMonthData(data, "8", "2021")
    year2021 = cleanData(year2021)
    print(year2021)
    createCVS(year2021, "August", "2021")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
