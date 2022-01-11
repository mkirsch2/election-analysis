# import csv module and os (add our dependencies)
import csv
import os

# assign a variable to load a file from a path
file_to_load = os.path.join("election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize total vote counter
total_votes = 0

# declare a new list to hold candidate names
candidate_options = []

# declare an empty dictionary
candidate_votes = {}

# open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)
    
    # print each row in the csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]

        # if the candidate name does not match any existing candidate, add the candidate to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to the candidate's vote count
        candidate_votes[candidate_name] +=1


print(candidate_votes)







