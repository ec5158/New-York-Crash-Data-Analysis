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

vehicles_categories = ['Sedan', 'Bus', 'Truck', 'Ambulance', 'Bike', 'Station wagon/sport utility vehicle',
                       'Ambulance', 'Van', 'Taxi', 'E-scooter/E-bike', 'Convertible', 'Motorcycle', 'Other']

"""
This function takes a column from one DataFrame and appends it to another DataFrame

parameters: data1 - the DataFrame the column will be added to
            data2 - the DataFrame the column of data will be extracted from
            col   - the name of the column from data2
returns: the first DataFrame will the extra column added on to it
"""
def combineData(data1, data2, col, date1, date2):
    extra_col = data2[col]
    return data1.join(extra_col, how='left', lsuffix=date1, rsuffix=date2)


"""

"""
def dictToDataFrame(dictionary, col1, col2):
    newDF = pd.DataFrame(dictionary.items(), columns=[col1, col2])
    return newDF


"""


returns: a dictionary - (type of accident, number of occurrences)
"""


def accidentByVehicle(data):
    vehicles = dict()
    """
    # First attempt at organizing accidents by vehicle involved
    # Issues: Too many vehicles listed lead to too many bars in chart thus the chart was unreadable
    #         Labels for vehicles on csv also inconsistent
    # Could use again if data cleaning on vehicle categories done on data before using this method
    for row in data.iterrows():
        row = row[1]
        for x in range(25, 30):
            key = row[x]
            if key is np.NaN:
                break
            if key.capitalize() in vehicles.keys():
                vehicles[key.capitalize()] += 1
            else:
                for vehicle in vehicles.keys():
                    if key.capitalize() in vehicle:
                        vehicles[vehicle] += 1
                        break
                vehicles[key.capitalize()] = 1
    """

    # TODO: Maybe create method that cleans the data in csv first before calling this method?
    # Also maybe move this to data_cleaning.py
    for automobile in vehicles_categories:
        vehicles[automobile] = 0

    for row in data.iterrows():
        row = row[1]
        for x in range(25, 30):
            key = row[x]
            if key is np.NaN:
                break
            elif key.capitalize() in vehicles.keys():
                vehicles[key.capitalize()] += 1
            else:
                found = False
                for vehicle in vehicles.keys():
                    if key.lower() in vehicle.lower():
                        vehicles[vehicle] += 1
                        found = True
                        break
                    if vehicle.lower() in key.lower():
                        vehicles[vehicle] += 1
                        found = True
                        break
                if not found:
                    vehicles['Other'] += 1

    return vehicles

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
def timeToNum(str_time):
    nums = str_time.split(':')
    return float(nums[0]) + (float(nums[1]) / 100.00)


"""

"""
def simplifyTime(data):
    rowCount = 0
    for row in data.iterrows():
        row = row[1]

        match timeToNum(row[2]):
            case num if num < 1.00:
                data.iloc[rowCount, 2] = '0:00 - 0:59'
            case num if 1.00 <= num < 2.00:
                data.iloc[rowCount, 2] = '1:00 - 1:59'
            case num if 2.00 <= num < 3.00:
                data.iloc[rowCount, 2] = '2:00 - 2:59'
            case num if 3.00 <= num < 4.00:
                data.iloc[rowCount, 2] = '3:00 - 3:59'
            case num if 4.00 <= num < 5.00:
                data.iloc[rowCount, 2] = '4:00 - 4:59'
            case num if 5.00 <= num < 6.00:
                data.iloc[rowCount, 2] = '5:00 - 5:59'
            case num if 6.00 <= num < 7.00:
                data.iloc[rowCount, 2] = '6:00 - 6:59'
            case num if 7.00 <= num < 8.00:
                data.iloc[rowCount, 2] = '7:00 - 7:59'
            case num if 8.00 <= num < 9.00:
                data.iloc[rowCount, 2] = '8:00 - 8:59'
            case num if 9.00 <= num < 10.00:
                data.iloc[rowCount, 2] = '9:00 - 9:59'
            case num if 10.00 <= num < 11.00:
                data.iloc[rowCount, 2] = '10:00 - 10:59'
            case num if 11.00 <= num < 12.00:
                data.iloc[rowCount, 2] = '11:00 - 11:59'
            case num if 12.00 <= num < 13.00:
                data.iloc[rowCount, 2] = '12:00 - 12:59'
            case num if 13.00 <= num < 14.00:
                data.iloc[rowCount, 2] = '13:00 - 13:59'
            case num if 14.00 <= num < 15.00:
                data.iloc[rowCount, 2] = '14:00 - 14:59'
            case num if 15.00 <= num < 16.00:
                data.iloc[rowCount, 2] = '15:00 - 15:59'
            case num if 16.00 <= num < 17.00:
                data.iloc[rowCount, 2] = '16:00 - 16:59'
            case num if 17.00 <= num < 18.00:
                data.iloc[rowCount, 2] = '17:00 - 17:59'
            case num if 18.00 <= num < 19.00:
                data.iloc[rowCount, 2] = '18:00 - 18:59'
            case num if 19.00 <= num < 20.00:
                data.iloc[rowCount, 2] = '19:00 - 19:59'
            case num if 20.00 <= num < 21.00:
                data.iloc[rowCount, 2] = '20:00 - 20:59'
            case num if 21.00 <= num < 22.00:
                data.iloc[rowCount, 2] = '21:00 - 21:59'
            case num if 22.00 <= num < 23.00:
                data.iloc[rowCount, 2] = '22:00 - 22:59'
            case num if 23.00 <= num <= 24.00:
                data.iloc[rowCount, 2] = '23:00 - 24:00'
            case _:
                print("Error")

        rowCount += 1

    return data


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
    if len(sys.argv) < 2:
        print("Usage: data_cleaning.py filename.csv")
        return

    csv_filename = sys.argv[1]
    data = pd.read_csv(csv_filename)
    year2021 = getMonthData(data, "4", "2021")
    year2021 = cleanData(year2021)
    # print(year2021)
    createCVS(year2021, "April", "2021")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
