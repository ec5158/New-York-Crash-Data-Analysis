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
import util_functions as uf
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
              '19:00 - 19:59', '20:00 - 20:59', '21:00 - 21:59', '22:00 - 22:59', '23:00 - 23:59']

vehicles_categories = ['Sedan', 'Bus', 'Truck', 'Ambulance', 'Bike', 'Station wagon/Sport Utility Vehicle',
                       'Ambulance', 'Van', 'Taxi', 'E-scooter/E-bike', 'Convertible', 'Motorcycle', 'Other']

boroughs = ['Queens', 'Brooklyn', 'Bronx', 'Manhattan', 'Staten Island', 'Unspecified']

factor_categories = []

"""

"""
def simplifyTime(data):
    rowCount = 0
    for row in data.iterrows():
        row = row[1]

        intTime = uf.timeToNum(row[2])
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
            if pd.isnull(key):
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


returns: a dictionary - (type of accident, number of occurrences)
"""
def accidentByVehicle(data):
    data = simplifyVehicles(data)

    vehicles = dict()

    for automobile in vehicles_categories:
        vehicles[automobile] = 0

    for row in data.iterrows():
        this_row = row[1]
        for x in range(25, 30):
            key = this_row[x]
            if pd.isnull(key):
                break
            elif key in vehicles.keys():
                vehicles[key] += 1
            else:
                vehicles['Other'] += 1

    return vehicles


"""


returns: a dictionary - (time of accident, number of occurrences)
"""
def accidentByTime(data):
    data = simplifyTime(data)

    times = dict()

    for spans in time_spans:
        times[spans] = 0

    for row in data.iterrows():
        this_row = row[1]
        key = this_row[2]
        if pd.isnull(key):
            continue
        elif key in times.keys():
            times[key] += 1
        else:
            print("Error: " + key + " is not a valid time.")

    return times


"""


returns: a dictionary - (borough/location of accident, number of occurrences)
"""
def accidentByBorough(data):
    places = dict()

    for borough in boroughs:
        places[borough] = 0

    for row in data.iterrows():
        this_row = row[1]
        key = this_row[3]
        if pd.isnull(key):
            places['Unspecified'] += 1
        elif key.title() in places.keys():
            places[key.title()] += 1
        else:
            print("Error: " + key + " is not a valid borough.")

    return places


"""


returns: a dictionary - (Reasons/Factors contributing to accident, number of occurrences)
"""
def accidentByFactor(data):
    reasons = dict()

    for row in data.iterrows():
        this_row = row[1]
        for x in range(19, 23):
            key = this_row[x]
            if pd.isnull(key):
                break
            if key.title() in reasons.keys():
                reasons[key.title()] += 1
            else:
                reasons[key.title()] = 1

    return reasons


"""

"""
def getAccidentDataFrame(data, xlabel):
    if xlabel == 'Vehicles':
        return uf.dictToDataFrame(accidentByVehicle(data), 'Vehicles', 'Number of Accidents')
    if xlabel == 'Crash Time':
        return uf.dictToDataFrame(accidentByTime(data), 'Crash Time', 'Number of Accidents')
    if xlabel == 'Borough':
        return uf.dictToDataFrame(accidentByBorough(data), 'Borough', 'Number of Accidents')
    if xlabel == 'Factor':
        return uf.dictToDataFrame(accidentByFactor(data), 'Factor', 'Number of Accidents')

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

    uf.createCVS(created_data, month, year)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
