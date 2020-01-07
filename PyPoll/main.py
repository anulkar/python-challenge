# ===============================================================
# PYTHON HOMEWORK - PYPOLL ELECTION RESULTS
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# ===============================================================
# This is the Main Python script to run for the PyPoll analysis.
# ===============================================================

# Import the pypoll module
# Module contains functions to analyze the election data and print+export the voting results to file
import pypoll

# Sets the csv file that you want the script to read
input_csv_file = "election_data.csv"

# Call function to analyze the csv file and save election results to variables
pypoll_results_sorted, total_votes, winning_candidate = pypoll.analyze_votes(input_csv_file)

# Call function to print results to terminal and save the printed analysis to a list
pypoll_analysis = pypoll.print_to_terminal(pypoll_results_sorted, total_votes, winning_candidate)

# Sets the text file that you want to write the results to
output_txt_file = "pypoll_output.txt"

# Call function to export the printed analysis from the list to the text file
pypoll.export_to_txtfile(output_txt_file, pypoll_analysis)