# Filename: bar_graphs.py
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
import data_cleaning

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
def makeBarGraph(data, xlabel, ylabel, date):
    if xlabel == 'CRASH TIME':
        data = simplifyTime(data)

    df = pd.DataFrame(data)

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Add x, y gridlines
    ax.grid(visible=True, color='black',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    x_values = df[xlabel]
    y_values = df[ylabel]

    plt.barh(x_values, y_values)

    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


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
def compareGraphs(data, xlabel, ylabel, date1, date2):
    data.plot(x=xlabel, y=[date1, date2], kind="barh")
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.title('Car Accident Info for ' + date1 + ' and ' + date2)
    # plt.savefig('Car_Accident_Info_' + date + '.png')

    plt.show()


"""


returns: a dictionary - (type of accident, number of occurrences)
"""
def accidentByVehicle(data):
    vehicles = dict()

    """
    # First attempt at organizing accidents by vehicle involved
    # Issues: Too many vehicles listed lead to too many bars in chart thus the chart was unreadable
    #         Labels for vehicles on csv also inconsistent
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

    for automobile in data_cleaning.vehicles:
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
def dictToDataFrame(dictionary, col1, col2):
    newDF = pd.DataFrame(dictionary.items(), columns=[col1, col2])
    return newDF


"""

"""
def main():
    try:
        csv_filename1 = sys.argv[1]
    except:
        print("Usage: bar_graphs.py filename1.csv [filename2.csv]")
        return

    data1 = pd.read_csv(csv_filename1)

    if len(sys.argv) > 2:
        csv_filename2 = sys.argv[2]
        data2 = pd.read_csv(csv_filename2)
        accidentData = dictToDataFrame(accidentByVehicle(data1), 'Vehicles', 'Number of Accidents')
        accidentData2 = dictToDataFrame(accidentByVehicle(data2), 'Vehicles', 'Number of Accidents')
        graphableData = combineData(accidentData, accidentData2, 'Number of Accidents', ' April 2021', ' August 2021')
        print(graphableData.to_string())
        compareGraphs(graphableData, 'Vehicles', 'Number of Accidents', 'Number of Accidents April 2021', 'Number of Accidents August 2021')
    else:
        accidentData = dictToDataFrame(accidentByVehicle(data1), 'Vehicles', 'Number of Accidents')
        makeBarGraph(accidentData, 'Vehicles', 'Number of Accidents', 'August 2021')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()