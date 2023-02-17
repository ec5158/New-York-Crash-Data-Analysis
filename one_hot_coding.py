# Filename: one_hot_coding.py
# Desc:
#
# @Author: Eric Chen
# @Date: 2023-02-16
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import data_cleaning
import re

"""

"""
def one_hot_code(data, filename):
    # List of category headers
    categories = ["2", "18", "19", "24", "25", "26"]
    # List of labels for the new one hot coded columns
    labels = ["Borough", "Contributing_Factor_Vehicle1", "Contributing_Factor_Vehicle2", "Vehicle_Type1",
              "Vehicle_Type2", "Vehicle_Type3"]

    # Performs one hot coding by removing the original categories and
    #   replacing them with the one hot coded versions of them
    one_hot_coded = pd.get_dummies(data, columns=categories, prefix=labels)

    # Creates a separate CSV file of the one hot coded data
    one_hot_coded.to_csv("Updated_" + filename)

    # Prints out the one hot coded data
    print(one_hot_coded)


"""

"""
def main():
    if len(sys.argv) < 2:
        print("Usage: one_hot_coding.py filename1.csv")
        return

    # Name of file to be analysed
    filename = sys.argv[1]

    # The data itself
    data = pd.read_csv(filename)

    one_hot_code(data, filename)


if __name__ == '__main__':
    main()
