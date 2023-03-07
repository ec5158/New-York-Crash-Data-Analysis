# Filename: data_analysis.py
# Desc: This file contains functions used to categorize and analyze
#   data into dictionaries and DataFrames that can be used to graph
#   insights of the motor accidents into visual forms
#
# @Author: Eric Chen
# @Date: 2023-03-06
#

import pandas as pd
import util_functions as uf
import data_cleaning as dcl


def accidentByVehicle(data):
    """
    Creates a dictionary consisting of keys - the type of vehicles involved in the
        accident and values - the number of times that type of vehicle was involved

    :param data: the original data in a DataFrame
    :return: a dictionary - (vehicles involved in the accident, number of occurrences)
    """
    vehicles = dict()

    # For every vehicle in vehicles_categories create a key with empty values
    for automobile in dcl.vehicles_categories:
        vehicles[automobile] = 0

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]
        # Vehicle names only appear in the 25th to 30th columns in the data file
        #   The columns are VEHICLE TYPE CODE 1 - 5
        for x in range(25, 30):
            # Gets the name of the vehicle
            key = this_row[x]
            # If the entry is np.NaN then that must mean there are no more vehicles involved to check
            #   for this accident
            if pd.isnull(key):
                break
            # Increases the number of accidents the vehicle is involved in
            elif key in vehicles.keys():
                vehicles[key] += 1
            # If the vehicle name somehow doesn't fit the given list, mark it under Other
            else:
                vehicles['Other'] += 1

    return vehicles


def accidentByTime(data):
    """
    Creates a dictionary consisting of keys - the time span the accident occurred
        and values - the number of times an accident occurred during that time

    :param data: the original data in a DataFrame
    :return: a dictionary - (time the accident occurred, number of occurrences)
    """
    times = dict()

    # For every time span in time_spans create a key with empty values
    for spans in dcl.time_spans:
        times[spans] = 0

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]
        # Gets the time span of this accident
        key = this_row[2]
        # If there is no entry then skip this accident
        if pd.isnull(key):
            continue
        # Increases the number of accidents corresponding to this time span
        elif key in times.keys():
            times[key] += 1
        # If this statement is somehow reached then there are issues in the original DataFrame
        else:
            print("Error: " + key + " is not a valid time.")

    return times


def accidentByBorough(data):
    """
    Creates a dictionary consisting of keys - the borough the accident occurred in
        and values - the number of times an accident occurred in that borough

    :param data: the original data in a DataFrame
    :return: a dictionary - (borough/location of accident, number of occurrences)
    """
    places = dict()

    # For every borough in boroughs create a key with empty values
    for borough in dcl.boroughs:
        places[borough] = 0

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]
        # Gets the name of this borough
        key = this_row[3]
        # If there is no entry for this borough, then consider it Unspecified
        if pd.isnull(key):
            places['Unspecified'] += 1
        # Otherwise, increase the record of the number of accidents that occurred at this borough
        elif key.title() in places.keys():
            places[key.title()] += 1
        # If this statement is somehow reached then there are issues in the original DataFrame
        else:
            print("Error: " + key + " is not a valid borough.")

    return places


def accidentByFactor(data):
    """
    Creates a dictionary consisting of keys - the recorded reason the accident occurred
        and values - the number of times an accident occurred because of that factor

    :param data: the original data in a DataFrame
    :return: a dictionary - (reasons/factors contributing to accident, number of occurrences)
    """
    reasons = dict()

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]

        # Contributing factors only appear in the 19th to 23rd columns in the data file
        #   The columns are CONTRIBUTING FACTOR VEHICLE 1 - 5
        for x in range(19, 23):
            # Gets the contributing vehicle factor
            key = this_row[x]
            # If the entry is np.NaN then that must mean there are no more factors involved to check
            #   for this accident
            if pd.isnull(key):
                break
            # If the factor has already been seen before and is recorded as a key,
            #   then increase the value (number of accidents) for it
            # .title() is used to keep the keys uniform and prevent creating different keys
            #   for something like GLARE and glare
            if key.title() in reasons.keys():
                reasons[key.title()] += 1
            # If the factor has not been recorded yet, then create a new key value pair
            #   to represent it
            else:
                reasons[key.title()] = 1

    return reasons


def accidentByWeekDay(data):
    """
    Creates a dictionary consisting of keys - the day of the week the accident occurred
        and values - the number of times an accident occurred during that day of the week

    :param data: the original data in a DataFrame
    :return: a dictionary - (day of the week the accident occurred, number of occurrences)
    """
    days = dict()

    # For every day of the week in days_of_the_week create a key with empty values
    for week_day in dcl.days_of_the_week:
        days[week_day] = 0

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]
        # Gets the date of the accident
        key = this_row[1]
        # If there is no entry for the date, then skip it
        if pd.isnull(key):
            break

        # Converts the date into the day of the week
        this_day = uf.dateToWeekDay(key)
        # Increases the record of number of accidents that occurred on this day
        days[this_day] += 1

    return days


def accidentByMonth(data):
    """
    Creates a dictionary consisting of keys - the month the accident occurred
        and values - the number of times an accident occurred during that month

    :param data: the original data in a DataFrame
    :return: a dictionary - (the month the accident occurred, number of occurrences)
    """
    months_dict = dict()

    # For every day of the month in months create a key with empty values
    for month in dcl.months:
        months_dict[month] = 0

    # Goes through every row
    for row in data.iterrows():
        # Gets the specific row of the accident
        this_row = row[1]
        # Gets the date of the accident
        key = this_row[1]
        # If there is no entry for the date, then skip it
        if pd.isnull(key):
            break

        # Gets the month from the date
        dataAspects = key.split("/")
        month_id = dcl.months[int(dataAspects[0]) - 1]

        # Increases the record of number of accidents that occurred on this month
        months_dict[month_id] += 1

    return months_dict


def getAccidentDataFrame(data, xlabel, time):
    """
    Given data, a category (xlabel) to search for, and a time period to
        differentiate it, creates a DataFrame containing the category as the first column
        and the number of accidents that occurred as the second column

    :param data: the original data as a DataFrame
    :param xlabel: the category or label to separate the data into
    :param time: the time period (year and/or month) the data represents
    :return: a new DataFrame that represents the number of accidents that occurred with
            (xlabel) conditions
    """
    if xlabel == 'Vehicles':
        return uf.dictToDataFrame(accidentByVehicle(data), 'Vehicles', 'Number of Accidents ' + time)
    if xlabel == 'Crash Time':
        return uf.dictToDataFrame(accidentByTime(data), 'Crash Time', 'Number of Accidents ' + time)
    if xlabel == 'Borough':
        return uf.dictToDataFrame(accidentByBorough(data), 'Borough', 'Number of Accidents ' + time)
    if xlabel == 'Factor':
        return uf.dictToDataFrame(accidentByFactor(data), 'Factor', 'Number of Accidents ' + time)
    if xlabel == 'Week Day':
        return uf.dictToDataFrame(accidentByWeekDay(data), 'Week Day', 'Number of Accidents ' + time)
    if xlabel == 'Months':
        return uf.dictToDataFrame(accidentByMonth(data), 'Months', 'Number of Accidents ' + time)


def getAverageData(year_set, xlabel):
    """
    Creates a dictionary containing the average number of accidents
        that happen under a certain category for multiple years

    :param year_set: a list containing DataFrames of different years
    :param xlabel: the category or attribute to get the average number of accidents for
    :return: a dictionary containing the average number of accidents
             that occurred over multiple years organized by the xlabel
    """
    category = ""
    if xlabel == "Crash Time":
        category = dcl.time_spans
    elif xlabel == "Week Day":
        category = dcl.days_of_the_week
    elif xlabel == "Borough":
        category = dcl.boroughs
    elif xlabel == "Months":
        category = dcl.months

    new_dict = dict()

    # For every month in months create a key with empty values
    for item in category:
        new_dict[item] = 0

    # Goes through every DataFrame given in the list, year by year
    for year in year_set:
        # Creates a new DataFrame of the number of accidents that occurred every
        #   month for the given year
        newData = getAccidentDataFrame(year, xlabel, "")

        rowCount = 0
        # For every accident, gets the number of accidents that occurred and
        #   the month it occurred
        for row in newData.iterrows():
            new_dict[category[rowCount]] += row[1][1]
            rowCount += 1

    # After getting all the number of accidents sorted by months
    #   divide by the number of years used to get the average
    for item in category:
        new_dict[item] //= len(year_set)

    return new_dict
