# Dependencies
import os
import csv
import operator

# File path for CSV
csv_file = os.path.join("Resources", "election_data.csv")

# File path for txt document
text_file_output = os.path.join("ElectionResults.txt")


#define things i need to count based on instructions
votes = 0
total_candidates = 0
#Define new lists to move data into
candidate_options = []
can_votes = {}

#open csvfile as dictionary
with open(csv_file, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

#Loop through all of the rows
    for row in csvreader:
#Define the indexs as Voter ID, County, Candidate
        voterid_index = row["Voter ID"]
        county_index = row["County"]
        can_index = row["Candidate"]
        #print(voterid_index)
        #print(county_index)
        #print(can_index)
        #ctrl+c these..
#Define what votes are
        votes = votes + 1
#Define count of how many candidates there are
        total_candidates = can_index
#Find all of the candidates and add them to the candidate options list
        if can_index not in candidate_options:
            candidate_options.append(can_index)
#Find the corresponding votes for candidates and add them to candidate votes dictionary
            can_votes[can_index] = 1
        else:
            can_votes[can_index] = can_votes[can_index] + 1

#---------------------------Start Printing Statements-----------------------------------------
#Print headers +  total votes
print("Election Results")
print("-------------------------")
print("Total Votes " + str(votes))
print("-------------------------")

#Create a loop to display all of the election results per candidate
for candidate in can_votes:
    string_percentage = format(round(((can_votes[candidate]/votes)*100)),'.3f')
    string_total_votes = can_votes[candidate]
    candidate_results = (candidate + " " + str(string_percentage) + "%" + " (" + str(string_total_votes) + ")")
    print(candidate_results)

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# added import operator ^        
# Determine winner in the candidate votes dictionary
election_winner = max(can_votes.items(), key=operator.itemgetter(1))[0]
#print(election_winner)
# Print Winner results
print("-------------------------")
print("Winner: " + str(election_winner))
print("-------------------------")

space = "\n"
# Output to Text File.. 
with open(text_file_output, "w") as txt_file:

    txt_file.write("Election Results")
    txt_file.write(space)
    txt_file.write("-------------------------")
    txt_file.write(space)
    txt_file.write("Total Votes " + str(votes))
    txt_file.write(space)
    txt_file.write("-------------------------")
    txt_file.write(space)
    for candidate in can_votes:
        string_percentage = format(round(((can_votes[candidate]/votes)*100)),'.3f')
        string_total_votes = can_votes[candidate]
        candidate_results = (candidate + " " + str(string_percentage) + "%" + " (" + str(string_total_votes) + ")")
        txt_file.write(candidate_results)
        txt_file.write(space)
    txt_file.write("-------------------------")
    txt_file.write(space)
    txt_file.write("Winner: " + str(election_winner))
    txt_file.write(space)
    txt_file.write("-------------------------")