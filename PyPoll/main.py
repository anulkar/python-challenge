# ===================================================================================
# PYTHON HOMEWORK - PYPOLL ELECTION RESULTS
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# ===================================================================================
# This is the Main Python script to run for the PyPoll analysis.
# It analyzes voting data provided in the "election_data.csv" file.
# Note that the csv file and the python script should be in the same folder.
# The csv dataset is composed of three columns: "Voter ID", "County" and "Candidate"
# The script calculates the following election results:
    # Total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
# ===================================================================================

# Import the os module to create file paths across operating systems
import os

# Import module for reading csv files
import csv

# Create the file path for the election_data.csv file
pypoll_csv_path = os.path.join(os.getcwd(), 'election_data.csv')

# Open the csv file for reading
with open(pypoll_csv_path, newline = '') as pypoll_csv_file:

    # CSV reader specifies delimiter and variable that holds the contents of the budget data file
    pypoll_csv_reader = csv.reader(pypoll_csv_file, delimiter = ',')

    # Read and save the header row first
    pypoll_csv_header = next(pypoll_csv_reader)

    # Initialize variable to store the total number of votes in the dataset
    total_votes = 0

    # Initialize dictionary to store the Voter ID and Candidate Name
    # Dictionary will be used to calculate the election results
    pypoll_dict = {}

    # Read each row of election data after the header to obtain the necessary election results
    for voting_data in pypoll_csv_reader:
        # Increment total_votes variable by 1 for each row in the file 
        # Each row represents one vote in the dataset
        total_votes += 1

        # Store the Voter ID as a key in the dictionary, and the Candidate name as the corresponding value 
        pypoll_dict[voting_data[0]] = voting_data[2]

# Close the csv file after we are done reading and analyzing it
pypoll_csv_file.close()

candidates = set(pypoll_dict.values())

pypoll_results = {}

pypoll_analysis = []

pypoll_analysis.append("\nELECTION RESULTS")
pypoll_analysis.append("\n" + "-" * 30)
pypoll_analysis.append("\nTotal Votes: {:,}".format(total_votes))
pypoll_analysis.append("\n" + "-" * 30)

for candidate in candidates:
    votes_won = sum(x == candidate for x in pypoll_dict.values())
    pypoll_results[candidate] = votes_won

from collections import OrderedDict
pypoll_results_sorted = OrderedDict(sorted(pypoll_results.items(), key=lambda x: x[1], reverse=True))

for candidate,votes_won in pypoll_results_sorted.items():
    percent_votes_won = votes_won / total_votes
    pypoll_analysis.append("\n" + candidate + ": " + "{:.3%}".format(percent_votes_won) + " ({:,})".format(votes_won))

pypoll_analysis.append("\n" + "-" * 30)

# Compute the greatest increase in profits from the dictionary (month and amount) 
winning_candidate = max(pypoll_results_sorted, key=pypoll_results_sorted.get)

pypoll_analysis.append("\nWINNER: " + winning_candidate)
pypoll_analysis.append("\n" + "-" * 30 + "\n")

# Print the contents of the list to the terminal
print(*pypoll_analysis)

# Create the file path for the output file that we want to export the results to
output_file_path = os.path.join(os.getcwd(), 'pypoll_output.txt')

# Open the output text file for writing
with open(output_file_path,'w') as pypoll_output_file:

    # Use list comprehension to write the contents of the list to the output file
    pypoll_output_file.writelines(pypoll_contents for pypoll_contents in pypoll_analysis)

# Close the text file once done writing to it
pypoll_output_file.close()