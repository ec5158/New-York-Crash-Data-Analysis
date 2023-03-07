# Filename: one_hot_coding.py
# Desc: This file performs one hot encoding on CSV files
#
# @Author: Eric Chen
# @Date: 2023-02-16
#

import pandas as pd
import sys


def one_hot_code(data, filename):
    """
    Performs one hot encoding on data, which is to say columns of the data
        will be simplified into lists of numbers of strings in order for
        other data analysis processes to be performed on them easier

    :param data: the DataFrame that one hot encoding will be performed on
    :param filename: the name of the original file the data is from
    :return: None
    """
    # List of category headers
    categories = ["BOROUGH", "CONTRIBUTING FACTOR VEHICLE 1", "CONTRIBUTING FACTOR VEHICLE 2", "VEHICLE TYPE CODE 1",
                  "VEHICLE TYPE CODE 2", "VEHICLE TYPE CODE 3"]
    # List of labels for the new one hot coded columns
    labels = ["Borough", "Contributing_Factor_Vehicle1", "Contributing_Factor_Vehicle2", "Vehicle_Type1",
              "Vehicle_Type2", "Vehicle_Type3"]

    # Performs one hot coding by removing the original categories and
    #   replacing them with the one hot coded versions of them
    one_hot_coded = pd.get_dummies(data, columns=categories, prefix=labels)

    # Creates a separate CSV file of the one hot coded data
    one_hot_coded.to_csv(filename[:len(filename) - 4] + "_Updated.csv")

    # Prints out the one hot coded data
    print(one_hot_coded.to_string())


def main():
    """
    This is the main driver function that handles the command line inputs

    :return: None
    """
    if len(sys.argv) < 2:
        print("Usage: one_hot_coding.py filename1.csv")
        return

    # Name of file to be analysed
    filename = sys.argv[1]

    # The data itself
    data = pd.read_csv(filename)

    # Performs one hot encoding on the data
    one_hot_code(data, filename)


if __name__ == '__main__':
    main()
