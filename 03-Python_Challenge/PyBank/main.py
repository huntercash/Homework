### PyBank
#
#![Revenue](Images/revenue-per-lead.jpg)
#
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#
#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#
#  * The total number of months included in the dataset
#
#  * The net total amount of "Profit/Losses" over the entire period
#
#  * The average of the changes in "Profit/Losses" over the entire period
#
#  * The greatest increase in profits (date and amount) over the entire period
#
#  * The greatest decrease in losses (date and amount) over the entire period
#
#* As an example, your analysis should look similar to the one below:
#
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```
#
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#----------------------------------------Begin Project---------------------------------
#import needed libraries
#from pathlib import Path, PureWindowsPath #universal file finder, the os module does not work well.. 
import os
import csv #to import csv files

#filename = PureWindowsPath("Resources\\budget_data.csv")
budget_csv = os.path.join = ("..", "Resources", "budget_data.csv")

#open the csvfile
with open(budget_csv, newline="") as csvfile:
    #let the csv reader know the variable name and delimiter, and make it a dictionary
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        dates = (row['Date'])
        month_count = sum(map(len, dates.values()))
        print(month_count)