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
#  * As an example, your analysis should look similar to the one below:
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

import os
import csv



#open and read csv file
csv_file = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csv_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    #split the headers
    headers=csv_header.split(',')
    #print('headers split up:', headers)

    date_index=headers.index('Date')
    #print('Date is in index:', date_index)

    p_l_index=headers.index('Profit/Losses\r\n')
    #print('Profit and Losses is in index:', p_l_index)
    date_list = []
    p_l_list = []
#  * The total number of months included in the dataset
    #create loop that appends date index into list
    for row in csvreader:
        date = row[0]
        p_l = row[1]
    #append them to the new list
        date_list.append(date)
        p_l_list.append(p_l)
    #print total of objects in list
    print(len(date_list))

