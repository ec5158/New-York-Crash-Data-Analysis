# Filename: data_cleaning.py
# Desc:
#
#
# @Author: Eric Chen
# @Date: 2023-01-11
#

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

time_spans = ['0:00 - 0:59', '1:00 - 1:59', '2:00 - 2:59', '3:00 - 3:59', '4:00 - 4:59', '5:00 - 5:59', '6:00 - 6:59',
              '7:00 - 7:59', '8:00 - 8:59', '9:00 - 9:59', '10:00 - 10:59', '11:00 - 11:59', '12:00 - 12:59',
              '13:00 - 13:59', '14:00 - 14:59', '15:00 - 15:59', '16:00 - 16:59', '17:00 - 17:59', '18:00 - 18:59',
              '19:00 - 19:59', '20:00 - 20:59', '21:00 - 21:59', '22:00 - 22:59', '23:00 - 24:00']

vehicles = ['Sedan', 'Bus', 'Truck', 'Ambulance', 'Bike', 'Station wagon/sport utility vehicle', 'Ambulance',
            'Van', 'Taxi', 'E-scooter/E-bike', 'Convertible', 'Motorcycle', 'Other']

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
    data.to_csv("csv/Motor_Vehicle_Collisions_" + month + "_" + year + ".csv")


"""

"""
def main():
    try:
        csv_filename = sys.argv[1]
    except:
        print("Usage: data_cleaning.py filename.csv")
        return
    data = pd.read_csv(csv_filename)
    year2021 = getMonthData(data, "4", "2021")
    year2021 = cleanData(year2021)
    print(year2021)
    createCVS(year2021, "April", "2021")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
