# Filename: data_cleaning.py
# Desc: This file extracts subsections of crash data from CSV files, performs
#   some cleaning of the data, and then creates a new CSV file presenting the month
#   and/or year the subsection of data represents
#
# @Author: Eric Chen
# @Date: 2023-01-11
#

import math
import pandas as pd
import numpy as np
import sys
import util_functions as uf
from datetime import datetime

# The columns for the data in the CSV files
columns = ["ID", "CRASH DATE", "CRASH TIME", "BOROUGH", "ZIP CODE", "LATITUDE", "LONGITUDE", "LOCATION",
           "ON STREET NAME", "CROSS STREET NAME", "OFF STREET NAME", "NUMBER OF PERSONS INJURED",
           "NUMBER OF PERSONS KILLED", "NUMBER OF PEDESTRIANS INJURED", "NUMBER OF PEDESTRIANS KILLED",
           "NUMBER OF CYCLIST INJURED", "NUMBER OF CYCLIST KILLED", "NUMBER OF MOTORIST INJURED",
           "NUMBER OF MOTORIST KILLED", "CONTRIBUTING FACTOR VEHICLE 1", "CONTRIBUTING FACTOR VEHICLE 2",
           "CONTRIBUTING FACTOR VEHICLE 3", "CONTRIBUTING FACTOR VEHICLE 4", "CONTRIBUTING FACTOR VEHICLE 5",
           "COLLISION_ID", "VEHICLE TYPE CODE 1", "VEHICLE TYPE CODE 2", "VEHICLE TYPE CODE 3", "VEHICLE TYPE CODE 4",
           "VEHICLE TYPE CODE 5"]

# The spans of time used for the crash time from the data
time_spans = ['0:00 - 0:59', '1:00 - 1:59', '2:00 - 2:59', '3:00 - 3:59', '4:00 - 4:59', '5:00 - 5:59', '6:00 - 6:59',
              '7:00 - 7:59', '8:00 - 8:59', '9:00 - 9:59', '10:00 - 10:59', '11:00 - 11:59', '12:00 - 12:59',
              '13:00 - 13:59', '14:00 - 14:59', '15:00 - 15:59', '16:00 - 16:59', '17:00 - 17:59', '18:00 - 18:59',
              '19:00 - 19:59', '20:00 - 20:59', '21:00 - 21:59', '22:00 - 22:59', '23:00 - 23:59']

# A simplified list of possible vehicles involved in the accidents from the data
vehicles_categories = ['Sedan', 'Bus', 'Truck', 'Ambulance', 'Bike', 'Station wagon/Sport Utility Vehicle',
                       'Ambulance', 'Van', 'Taxi', 'E-scooter/E-bike', 'Convertible', 'Motorcycle', 'Other']

# A list of the possible NYC Boroughs the accident can occur in
boroughs = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Unspecified']

# A list of the days of the week used to categorize accidents
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# A list of the months used to categorize accidents
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


def simplifyTime(data):
    """
    Goes through the column containing the time of the accident in the data
        and simplifies it into a time-span for easier plotting in graphs

    :param data: the original data in a DataFrame
    :return: the DataFrame with every time simplified into a time-span
    """
    # Used to access data.iloc[] and put the proper time-span in the right place
    rowCount = 0
    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]

        # Gets the crash time and converts from a string into a float
        intTime = uf.timeToNum(this_row[2])
        # Gets the hour from the time
        hrTime = str(math.floor(intTime))
        # Puts a new time-span into the original location
        data.iloc[rowCount, 2] = hrTime + ':00' + ' - ' + hrTime + ':59'

        rowCount += 1

    return data


def simplifyVehicles(data):
    """
    Goes through the data and simplifies the vehicles involved in the
        accident by replacing them with a vehicle from the
        uniformed list of vehicles (vehicles_categories)

    :param data: the original data in a DataFrame
    :return: the DataFrame with every unique vehicle simplified into a vehicle from a list
    """
    # Used to access data.iloc[] and replace the vehicle name
    rowCount = 0
    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]

        # Vehicle names only appear in the 25th to 30th columns in the data file
        #   The columns are VEHICLE TYPE CODE 1 - 5
        for x in range(25, 30):
            # Gets the name of the vehicle
            key = this_row[x]
            # If the entry is np.NaN then that must mean there are no more vehicles involved to change
            #   for this accident
            if pd.isnull(key):
                break
            # If the vehicle name already fits in the vehicles_categories
            #   then simplify format it into a capitalized form
            elif key.capitalize() in vehicles_categories:
                data.iloc[rowCount, x] = key.capitalize()
            else:
                found = False
                # Searches through the categories in vehicles_categories and tries to find
                #   a close enough match to the original entry to replace it with
                #   Ex: FIRE TRUCK is a truck so the entry becomes Truck
                for vehicle in vehicles_categories:
                    # Checks if the original entry would be a part of a given vehicle category
                    #   Ex: An entry of e-scooter would be changed into E-scooter/E-bike
                    if key.lower() in vehicle.lower():
                        data.iloc[rowCount, x] = vehicle
                        found = True
                        break
                    # Checks if one of the vehicle categories is a part of the original entry
                    #   If so simplify the entry to only be the vehicle category
                    #   Ex: An entry of school bus has bus in it, so it would be changed to just Bus
                    if vehicle.lower() in key.lower():
                        data.iloc[rowCount, x] = vehicle
                        found = True
                        break
                # If the entry does not match anything then classify it as Other
                if not found:
                    data.iloc[rowCount, x] = 'Other'
        rowCount += 1

    return data


def getYearData(data, year):
    """
    Takes a DataFrame containing crashes in NYC and gets a new DataFrame
        from it that only contains crashes that occurred on a given year

    :param data: the original data as a DataFrame
    :param year: the year the crashes should occur in
    :return: a new DataFrame containing only crashes on a specific year
    """
    rowList = []

    # Goes through every row
    for row in data.iterrows():
        # Gets the data of the crash
        crashDate = row[1][0]
        # Separates the date into Month, Day, and Year
        dataAspects = crashDate.split("/")
        # Skips the first row which contains only the column headings
        if dataAspects[0] != "CRASH DATE":
            # If the year matches, then append the accident row to an array of accidents
            if dataAspects[2] == year:
                rowList.append(row[1])

    # Creates a new DataFrame from the list of accidents
    return pd.DataFrame.from_records(rowList)


def getMonthData(data, month, year):
    """
    Takes a DataFrame containing crashes in NYC and gets a new DataFrame
        from it that only contains crashes that occurred on a given month and year

    :param data: the original data as a DataFrame
    :param month: the month the crashes should occur in
    :param year: the year the crashes should occur in
    :return: a new DataFrame containing only crashes on a specific month and year
    """
    rowList = []

    # Goes through every row
    for row in data.iterrows():
        # Gets the data of the crash
        crashDate = row[1][0]
        # Separates the date into Month, Day, and Year
        dataAspects = crashDate.split("/")
        # Skips the first row which contains only the column headings
        if dataAspects[0] != "CRASH DATE":
            # If the month and year matches, then append the accident row to an array of accidents
            if int(dataAspects[0]) == month and dataAspects[2] == year:
                rowList.append(row[1])

    # Creates a new DataFrame from the list of accidents
    return pd.DataFrame.from_records(rowList)


def cleanData(data):
    """
    Goes through every entry in the DataFrame and removes excess white spaces
        and replaces an empty entries or entries containing Unspecified with
        np.NaN to denote there is nothing there

    :param data: the original data as a DataFrame
    :return: the data cleaned
    """
    # Used to access data.iloc[] and change the data
    rowCount = 0

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        row = row[1]
        # Keeps track of which col is being looked at
        colCount = 0

        # Goes through every column in the row
        for columns in data.items():
            # Gets the current data entry
            current = row[colCount]

            # If the entry is a string then remove the trailing white space before
            #   and after the actual string
            if isinstance(current, str):
                current = current.rstrip()
                data.iloc[rowCount, colCount] = current

                # If the entry is Unspecified, replace it with np.NaN
                #   to make data analysis more effective
                if current == 'Unspecified':
                    data.iloc[rowCount, colCount] = np.NaN

            # If there is no entry then, change it to np.NaN so there
            #   is no issue when parsing through the data later
            if pd.isnull(current):
                data.iloc[rowCount, colCount] = np.NaN

            colCount += 1
        rowCount += 1

    return data


def main():
    """
    This is the main driver function that handles the command line inputs

    :return: None
    """
    # The program needs to at least have a CSV file and a year to create a new CSV files
    if len(sys.argv) < 3:
        print("Usage: data_cleaning.py <filename.csv> [<month>] <year>")
        return

    # Gets the CSV file
    csv_filename = sys.argv[1]

    # Used to for checking and adding a month to the file
    month_num = 0
    month = ""
    has_month = False

    # If a month was given in the command line then
    #   calculate what number the month represents and
    #   get the year and month
    if sys.argv[2].title() in months:
        month = sys.argv[2].title()
        month_num = datetime.strptime(month, '%B').month
        year = sys.argv[3]
        has_month = True
    else:
        year = sys.argv[2]

    # Gets the original data
    data = pd.read_csv(csv_filename)

    # If there is a month, then the data should reflect that
    if has_month:
        created_data = getMonthData(data, month_num, year)
    else:
        created_data = getYearData(data, year)

    # Removes any stray spaces in strings, Unspecified results, and
    #   adds np.NaN to any empty spaces
    created_data = cleanData(created_data)

    # Simplifies values in the time column and the columns detailing the
    #   vehicles involved in the accident in order for the graphing to work
    created_data = simplifyTime(created_data)
    created_data = simplifyVehicles(created_data)

    # Used to double-check the values and data seem accurate before going into the
    #  process of converting it into a CVS
    # print(created_data)

    # Creates a new CSV representing data of the given year and/or month
    uf.createCSV(created_data, month, year)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
