#import needed libraries

import os
import csv
from statistics import mean

title = "Financial Analysis"
lines = "----------------------------"

#open and read csv file
csv_file = os.path.join("Resources", "budget_data.csv")
# File path for txt document
text_file_output = os.path.join("analysis.txt")

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
    for x in range(len(p_l_total)):
        if x == 0:
            pass
        else:
           average_of_changes_list.append(p_l_total[x] - p_l_total[x - 1])
    average_change = mean(average_of_changes_list)
    
    max_change = max(average_of_changes_list)
    min_change = min(average_of_changes_list)
    
    max_change_date = str(date_list[average_of_changes_list.index(max(average_of_changes_list))])
    
    
    min_change_date = str(date_list[average_of_changes_list.index(min(average_of_changes_list))])
    #print(average_of_changes_list)
    
    #print total of objects in list
    print(title)
    print(lines)
    print("Total Months: " + str(length_of_date_list))
    print("Total Profit/Losses: $" + str(p_l_total_sum))
    print("Average Change: $" + str(float(round(average_change, 2))))
    print("Greatest Increase in Revenue: " + str(max_change_date) + " " + "($" + str(max_change) + ")")
    print("Greatest Decrease in Revenue: " + str(min_change_date) + " " + "($" + str(min_change) + ")")

space = "\n"
# Create a text Document
with open(text_file_output, "w") as txt_file:
    txt_file.write(title)
    txt_file.write(space)
    txt_file.write(lines)
    txt_file.write(space)
    txt_file.write("Total Months: " + str(length_of_date_list))
    txt_file.write(space)
    txt_file.write("Total Profit/Losses: $" + str(p_l_total_sum))
    txt_file.write(space)
    txt_file.write("Average Change: $" + str(float(round(average_change, 2))))
    txt_file.write(space)
    txt_file.write("Greatest Increase in Revenue: " + str(max_change_date) + " " + "($" + str(max_change) + ")")
    txt_file.write(space)
    txt_file.write("Greatest Decrease in Revenue: " + str(min_change_date) + " " + "($" + str(min_change) + ")")