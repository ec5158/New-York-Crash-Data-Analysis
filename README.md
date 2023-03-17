# New-York-Crash-Data-Analysis

## Description
This program takes data about crashes in NYC and visualizes how the number of crashes and area where crashes occurred changed from year to year and month to month. This is a rewrite of an older RIT data mining school project I participated in that researched how COVID-19 changed how and when motor vehicle collisions occurred in the various boroughs of New York City.

The data and CSV files used for this project come from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95).

## Instructions
``` ./data_cleaning.py <filename.csv> [<month>] <year> ``` To start, use this program with the given CSV file from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) to create a new CSV file of only the data falling on the inputted month and year. The CSV file should be from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) for this program to work. The new CSV file will have unspecified and empty data entries masked into numpy's NaN value for usage in future data analysis.

``` ./monthly_stats.py <x-label> <filename1.csv> [<filename2.csv> ...] ``` Creates a bar chart of the number of accidents that occurred in the given CSV file and sorts them by x-label (Vehicles, Crash Time, etc.). This is for comparing data in terms of months. [filename2.csv] is optional and inputting a second CSV file creates a double bar graph of both CSV files to compare accidents by month and year based on given x-label. Adding any other CSV files after the second one will lead to the program comparing data from filename1.csv to the average number of accidents from the rest of the CSV files.

``` ./yearly_stats.py <x-label> <filename1.csv> [<filename2.csv> ...] ``` Creates a bar chart of the number of accidents that occurred in the given CSV file and sorts them by x-label (Months or Days of the Week). This is for comparing data in terms of years. [filename2.csv] is optional and inputting a second CSV file creates a double bar graph of both CSV files to compare accidents by year based on given x-label. Adding any other CSV files after the second one will lead to the program comparing data from filename1.csv to the average number of accidents from the rest of the CSV files.

``` ./accident_line_graphs.py <x-label> <filename1.csv> [<filename2.csv> ...] ``` Creates a line graph of the number of accidents that occurred in the given CSV file and sorts them by x-label (Crash Time, Day of the Week, or Borough). This is for comparing data in terms of years. [filename2.csv] is optional and inputting a second CSV file creates a double line graph of both CSV files to compare accidents by year based on given x-label. Adding any other CSV files after the second one will lead to the program comparing data from filename1.csv to the average number of accidents from the rest of the CSV files. If there is only one CSV file and the inputted x-label is Borough, then a unique multiple line graph is created with every borough represented with their own colored line and the x-label becomes the time span a motor vehicle accident occurred and the y-label becomes the number of accidents in that time span.

``` ./one_hot_coding.py <filename1.csv> ``` Performs one hot encoding on the given CSV file by replacing the columns of boroughs, contributing factor vehicle, and vehicle type code with one hot encoded versions of them.

``` ./heat_map.py <filename1.csv> ``` Creates a heat map of the motor vehicle accidents that occurred in New York City using the given CSV file. This is for looking at data in terms of a single year and/or month. This program displays a map representing New York City Boroughs with a heat map overlay that shows where the highest number of motor vehicle collisions occurred.

## Progress
- [X] Program can read in CSV file
- [X] Program can create CSV with subsection of data from original CSV file
        based on year and/or month
- [X] Program can perform basic data cleaning of data received
- [X] Bar graphs that show accidents by vehicle for a given data set
- [X] Bar graphs that can compare accidents by vehicle between different months
- [X] Bar graphs that show accidents by crash time spans for a given data set
- [X] Bar graphs that can compare accidents by crash time spans between different months
- [X] Bar graphs that show accidents by different metrics (day of the week, etc.)
- [X] Comparing accidents for a given year to average
- [X] Comparing accidents for a given month to average
- [X] Comparing accidents by each hour of the day by borough in a certain year
- [X] Representing data in terms of line charts
- [X] Documentation
- [X] Heat Map of accidents in every borough using Parzen Density Estimation

### Works in Progress:
- [ ] More Testing

