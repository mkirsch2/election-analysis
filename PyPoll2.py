# Import CSV and OS modules
import csv
import os

# Assign a variable for the file to oad and the path.
file_to_load = "Resources/election_results.csv"

# Open the election results and read the file.
election_data = open(file_to_load,"r")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file:
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
