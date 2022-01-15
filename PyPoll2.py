# Import CSV and OS modules.
import csv
import os

# Assign a variable for the file to oad and the path.
file_to_load = "Resources/election_results.csv"

# Open the election results and read the file.
election_data = open(file_to_load,"r")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a variable to hold total votes.
total_votes = 0

# Declare a new list called candidate_options.
candidate_options = []

# Declare an empty dictionary to hold candidate votes.
candidate_votes= {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file:
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote vount.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the perecentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,}) \n")
        txt_file.write(candidate_results)

        
        # Determine winning vote count and candidate.
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning percent = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the results to our text file.
    txt_file.write(winning_candidate_summary)