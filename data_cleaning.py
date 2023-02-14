# Filename: data_cleaning.py
# Desc:
#
#
# @Author: Eric Chen
# @Date: 2023-01-11
#

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from datetime import datetime

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

vehicles_categories = ['Sedan', 'Bus', 'Truck', 'Ambulance', 'Bike', 'Station wagon/Sport Utility Vehicle',
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
    return data1.join(extra_col, how='left', lsuffix=' '+date1, rsuffix=' '+date2)


"""

"""
def dictToDataFrame(dictionary, col1, col2):
    newDF = pd.DataFrame(dictionary.items(), columns=[col1, col2])
    return newDF


"""


returns: a dictionary - (type of accident, number of occurrences)
"""


def accidentByVehicle(data):
    data = simplifyVehicles(data)

    vehicles = dict()

    for automobile in vehicles_categories:
        vehicles[automobile] = 0

    for row in data.iterrows():
        row = row[1]
        for x in range(25, 30):
            key = row[x]
            if key is np.NaN:
                break
            elif key in vehicles.keys():
                vehicles[key] += 1
            else:
                vehicles['Other'] += 1

    return vehicles


"""

"""
def getAccidentDataFrame(data):
    return dictToDataFrame(accidentByVehicle(data), 'Vehicles', 'Number of Accidents')


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
            if int(dataAspects[0]) == month and dataAspects[2] == year:
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

        intTime = timeToNum(row[2])
        hrTime = str(math.floor(intTime))
        data.iloc[rowCount, 2] = hrTime + ':00' + ' - ' + hrTime + ':59'

        rowCount += 1

    return data


"""

"""
def simplifyVehicles(data):
    rowCount = 0
    for row in data.iterrows():
        row = row[1]
        for x in range(25, 30):
            key = row[x]
            if key is np.NaN:
                break
            elif key.capitalize() in vehicles_categories:
                data.iloc[rowCount, x] = key.capitalize()
            else:
                found = False
                for vehicle in vehicles_categories:
                    if key.lower() in vehicle.lower():
                        data.iloc[rowCount, x] = vehicle
                        found = True
                        break
                    if vehicle.lower() in key.lower():
                        data.iloc[rowCount, x] = vehicle
                        found = True
                        break
                if not found:
                    data.iloc[rowCount, x] = 'Other'
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
    if len(sys.argv) < 4:
        print("Usage: data_cleaning.py filename.csv month year")
        return

    csv_filename = sys.argv[1]
    month = sys.argv[2]
    month_num = datetime.strptime(month, '%B').month
    year = sys.argv[3]
    data = pd.read_csv(csv_filename)
    created_data = getMonthData(data, month_num, year)
    created_data = cleanData(created_data)

    # Used to double-check the values and data seem accurate before going into the
    #  process of converting it into a CVS
    # print(created_data)

    createCVS(created_data, month, year)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
