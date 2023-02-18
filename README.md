# New-York-Crash-Data-Analysis

## Description
This program takes data about crashes in NYC and visualizes how the number of crashes and area where crashes occurred changed due to COVID-19. This is a rewrite of an older RIT data mining school project I participated in.

The data and CSV files used for this project come from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95).

## Instructions
``` ./data_cleaning filename.csv month year ``` Starts the program with the given CSV file and creates a new CSV file of only the data falling on the inputted month and year. The CSV file should be from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) for this program to work.

``` bar_graphs.py filename1.csv [filename2.csv] x-label ``` Creates a bar chart of the number of accidents that occurred in the given CSV file and sorts them by x-label (Vehicles, Crash Time, etc.). [filename2.csv] is optional and inputting a second CSV file creates a double bar graph of both CSV files to compare accidents by month and year based on given x-label.

## Progress
- [X] Program can read in CSV file
- [X] Program can create CSV with subsection of data from original CSV file
        based on year and/or month
- [X] Program can perform basic data cleaning of data received
- [X] Bar graphs that show accidents by vehicle for a given data set
- [X] Bar graphs that can compare accidents by vehicle between different months
- [X] Bar graphs that show accidents by crash time spans for a given data set
- [X] Bar graphs that can compare accidents by crash time spans between different months
        
### Works in Progress:
- [ ] More Testing
- [ ] Documentation
- [ ] Comparing accidents for a given month or year to average
- [ ] Bar graphs that show accidents by different metrics (day of the week, etc.)
- [ ] Statistics for Type of Accident (Car to Car, Bike to Car, Pedestrian Involved, etc.)
- [ ] Heat Map
