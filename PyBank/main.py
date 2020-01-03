# =================================================================
# PYTHON HOMEWORK - PYBANK FINANCIAL ANALYSIS
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# =================================================================
# This is the Main Python script to run for the PyBank analysis.
# =================================================================

# Import the pybank module
# Module contains functions to analyze the bank data and print+export the results to file
import pybank

# Sets the csv file that you want the script to read
input_csv_file = "budget_data.csv"

# Call function to analyze the csv file and save returned results to a list
pybank_results = pybank.analyze_finances(input_csv_file)

# Call function to print results to terminal and save the printed analysis to a list
pybank_analysis = pybank.print_to_terminal(pybank_results)

# Sets the text file that you want to write the results to
output_txt_file = "pybank_output.txt"

# Call function to export the analysis to the text file
pybank.export_to_txtfile(output_txt_file, pybank_analysis)