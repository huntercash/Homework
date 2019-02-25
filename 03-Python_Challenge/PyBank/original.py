#import needed libraries

import os
import csv
from statistics import mean

title = "Financial Analysis"
lines = "----------------------------"

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

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
        length_of_date_list = len(date_list)
        p_l_list.append(p_l)

    #do math on index 1 to add them all together
    p_l_total = list(map(int, p_l_list))
    p_l_total_sum = sum(p_l_total)
    
    #figure out average changes in profit and losses over entire period
    average_of_changes_list = []
    for ind in range(len(p_l_total)):
        if ind == 0:
            pass
        else:
           average_of_changes_list.append(p_l_total[ind] - p_l_total[ind - 1])
    average_change = mean(average_of_changes_list)
    print(average_of_changes_list)




    #print(average_of_changes_list)
    
    #print total of objects in list
    print(title)
    print(lines)
    print("Total Months: " + str(length_of_date_list))
    print("Total: $" + str(p_l_total_sum))
    print("Average Change: $" + str(float(round(average_change, 2))))