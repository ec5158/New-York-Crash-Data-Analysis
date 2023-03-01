# New-York-Crash-Data-Analysis

## Description
This program takes data about crashes in NYC and visualizes how the number of crashes and area where crashes occurred changed due to COVID-19. This is a rewrite of an older RIT data mining school project I participated in.

The data and CSV files used for this project come from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95).

## Instructions
``` ./data_cleaning.py <filename.csv> [<month>] <year> ``` Starts the program with the given CSV file and creates a new CSV file of only the data falling on the inputted month and year. The CSV file should be from the [NYC OpenData Website](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) for this program to work.

``` ./monthly_stats.py <x-label> <filename1.csv> [<filename2.csv>] ``` Creates a bar chart of the number of accidents that occurred in the given CSV file and sorts them by x-label (Vehicles, Crash Time, etc.). This is for comparing data in terms of months. [filename2.csv] is optional and inputting a second CSV file creates a double bar graph of both CSV files to compare accidents by month and year based on given x-label.

``` ./yearly_stats.py <x-label> <filename1.csv> [<filename2.csv> ...] ``` Creates a bar chart of the number of accidents that occurred in the given CSV file and sorts them by x-label (Months or Days of the Week). This is for comparing data in terms of years. [filename2.csv] is optional and inputting a second CSV file creates a double bar graph of both CSV files to compare accidents by month and year based on given x-label. Adding any other CSV files after the second one will lead to the program comparing data from filename1.csv to the average number of accidents of the rest of the CSV files.

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

### Works in Progress:
- [ ] More Testing
- [ ] Documentation
- [ ] Comparing accidents for a given month to average
- [ ] Comparing accidents by each hour of the day by borough in a certain year
- [ ] Representing data in terms of line charts
- [ ] Heat Map of accidents in every borough using Parzen Density Estimation
