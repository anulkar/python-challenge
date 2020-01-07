# =========================================================================================
# PYTHON HOMEWORK - PYPOLL ELECTION RESULTS
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# =========================================================================================
# This is the main module that analyzes election voting data provided in a csv file.
# The csv dataset is composed of three columns: "Voter ID", "County" and "Candidate"
# Election results are printed to terminal and exported to a text file in the same folder.
# =========================================================================================

# Execute only when another script imports this as a module
if __name__ != "__main__":

    # Import the os module to create file paths across operating systems
    import os

    # Import module for reading csv files
    import csv

    # =======================================================================
    # The analyze_votes function calculates the following election results:
    # 1) Total number of votes cast
    # 2) A complete list of candidates who received votes
    # 3) The winner of the election based on popular vote
    # =======================================================================
    def analyze_votes(csv_file_name):
        # Create the file path for the election_data.csv file
        pypoll_csv_path = os.path.join(os.getcwd(), csv_file_name)

        # Open the csv file for reading
        with open(pypoll_csv_path, newline = '') as pypoll_csv_file:

            print(f"\nAnalyzing the Election Data File: {pypoll_csv_path}")
            print("\nStay tuned for the results...")
            
            # CSV reader specifies delimiter and variable that holds the contents of the election data file
            pypoll_csv_reader = csv.reader(pypoll_csv_file, delimiter = ',')

            # Read the header row first
            next(pypoll_csv_reader)

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

        # Retrieve the unique list of candidates from the dictionary as a set
        candidates = set(pypoll_dict.values())

        # Initialize a dictionary to store the election results
        pypoll_results = {}

        # Iterate through the set of unique candidates
        for candidate in candidates:
            # Compute the sum of votes won by each candidate
            votes_won = sum(x == candidate for x in pypoll_dict.values())
            # Store the candidate name as a key in the dictionary, and votes won as the corresponding value
            pypoll_results[candidate] = votes_won

        # Use an OrderedDict to sort the dictionary based on votes won by candidates from highest to lowest
        from collections import OrderedDict
        pypoll_results_sorted = OrderedDict(sorted(pypoll_results.items(), key=lambda x: x[1], reverse=True))

        # Initialize variable to store the candidate who won the most votes
        winning_candidate = ""
        # Find the winning candidate in the sorted dictionary of poll results based on max votes
        winning_candidate = max(pypoll_results_sorted, key=pypoll_results_sorted.get)

        # Return the sorted pypoll dictionary, total votes and winning candidate so we can print them later
        return(pypoll_results_sorted, total_votes, winning_candidate)

    # =============================================================================================
    # The print_to_terminal function takes the election results and:
    #  1) Determines the percentage of votes each candidate won
    #  2) Prints a summary of all the election results to terminal
    # =============================================================================================
    def print_to_terminal(pypoll_results_sorted, total_votes, winning_candidate):

        # Initialize an empty list to store each "line" of the results
        # List will be used to print the results to terminal and export to a text file
        pypoll_analysis = []

        # Add formatted output/lines and total number of votes to the list
        pypoll_analysis.append("\nELECTION RESULTS")
        pypoll_analysis.append("\n" + "-" * 30)
        pypoll_analysis.append("\nTotal Votes: {:,}".format(total_votes))
        pypoll_analysis.append("\n" + "-" * 30)

        # Calculate percentage of votes won by each candidate and add them to the list for printing
        for candidate,votes_won in pypoll_results_sorted.items():
            percent_votes_won = votes_won / total_votes
            pypoll_analysis.append("\n" + candidate + ": " + "{:.3%}".format(percent_votes_won) + " ({:,})".format(votes_won))

        # Add remaining formatted output/lines and the winning candidate name to the list
        pypoll_analysis.append("\n" + "-" * 30)
        pypoll_analysis.append("\nWINNER: " + winning_candidate)
        pypoll_analysis.append("\n" + "-" * 30 + "\n")

        # Print the contents of the election results list to the terminal
        print(*pypoll_analysis)

        # Return the election results list to the calling function
        return(pypoll_analysis)

    # =======================================================================================
    # The export_to_txtfile function exports the printed election results to a text file
    # =======================================================================================
    def export_to_txtfile(output_txt_file, pypoll_analysis):
        # Create the file path for the output file that we want to export the results to
        output_file_path = os.path.join(os.getcwd(), output_txt_file)

        # Open the output text file for writing
        with open(output_file_path,'w') as pypoll_output_file:

            # Use list comprehension to write the contents of the list to the output file
            pypoll_output_file.writelines(pypoll_contents for pypoll_contents in pypoll_analysis)

        # Close the text file once done writing to it
        pypoll_output_file.close()

        # Let the user know that we are done exporting the file
        print(f"Results exported to text file: {os.getcwd()}/{output_txt_file}\n")
else:
        # Let the user know that they can't run this module by itself
        print("\nThis is the pypoll.py module that executes only when imported and run via another script. Try running \"python main.py\" instead. \n")