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