#----------------------------------------Begin Project---------------
# Import needed libraries
import os
import csv
from statistics import mean

# File path for CSV
csv_file = os.path.join("Resources", "budget_data.csv")

# File path for txt document
text_file_output = os.path.join("analysis.txt")

# Empty variables to track
months_total = 0
p_l_total = 0
p_l_previous = 0
p_l_changes = []


# Define increase list
revenue_greatest_increase = ["", 0]

# Define decreate list
revenue_greatest_decrease = ["", 0]

# Create Empty List to Save Data to
p_l_changes_list = []


# Open and read csv as Ordered Dictionary instead of list
# list required making too many seperate lists, code became unreadable

with open(csv_file, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
# Create a Loop to do the analysis
    for row in csvreader:
# Define Revenue Index
        revenue_index = int(row["Profit/Losses"])
        #print(revenue_index)
# Define Months Index
        months_index = (row["Date"])
        #print(months_index) 
# Calculate the month count totals (Calculating based on how many rows exist)
        months_total = months_total + 1
# Calculate Revenue Total
        p_l_total = p_l_total + revenue_index
# Calculate Revenue Change
        p_l_changes = revenue_index - p_l_previous
# Add changes to list and empty variables
        p_l_previous = revenue_index
        #print(p_l_previous)
        
#Figure out the greatest change between 
        if (p_l_changes > revenue_greatest_increase[1]):
            revenue_greatest_increase[1] = p_l_changes
            revenue_greatest_increase[0] = months_index

        if (p_l_changes < revenue_greatest_decrease[1]):
            revenue_greatest_decrease[1] = p_l_changes
            revenue_greatest_decrease[0] = months_index
# Use this data to figure out greatest increase/decrease in revenue dictionary
            p_l_changes_list.append(revenue_index)
#Calculate average changes in profit and losses over entire period using a list
#Need help to get this to work
            list_of_revenue = []
            for ind in range(len(p_l_changes_list)):
                if ind == 0:
                    pass
                else:
                    list_of_revenue.append(p_l_total - p_l_total-1)
    p_l_average = mean(list_of_revenue)
    p_l_round = round(p_l_average, 2)

#Define Repeatable Variables
head = "Financial Analysis"
line1 = "-------------------------"
line2 = "Total Months: " + str(months_total)
line3 = "Total Profit/Losses: " + "$" + str(p_l_total)
line4 = "Average Change: " + "$" + str(p_l_round)
line5 = "Greatest Increase: " + str(revenue_greatest_increase[0]) + " ($" +  str(revenue_greatest_increase[1]) + ")"
line6 = "Greatest Decrease: " + str(revenue_greatest_decrease[0]) + " ($" +  str(revenue_greatest_decrease[1]) + ")"
# Print the results
print(head)
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)

space = "\n"
# Create a text Document
with open(text_file_output, "w") as txt_file:
    txt_file.write(head)
    txt_file.write(space)
    txt_file.write(line1)
    txt_file.write(space)
    txt_file.write(line2)
    txt_file.write(space)
    txt_file.write(line3)
    txt_file.write(space)
    txt_file.write(line4)
    txt_file.write(space)
    txt_file.write(line5)
    txt_file.write(space)
    txt_file.write(line6)
