# =============================================================================
# PYTHON HOMEWORK - PYBANK FINANCIAL ANALYSIS
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# =============================================================================
# This is the Main Python script to run for the PyBank analysis.
# It analyzes financial data provided in the "budget_data.csv" file.
# Note that the csv file and the python script should be in the same folder.
# The csv dataset is composed of two columns: "Date" and "Profit/Losses"
# The script calculates the following stats:
    # Total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
# ==============================================================================

# Import the os module to create file paths across operating systems
import os

# Import module for reading csv files
import csv

# Create the file path for the budget_data.csv file
pybank_csv_path = os.path.join(os.getcwd(), 'budget_data.csv')

# Open the csv file for reading
with open(pybank_csv_path, newline = '') as pybank_csv_file:

    # CSV reader specifies delimiter and variable that holds the contents of the budget data file
    pybank_csv_reader = csv.reader(pybank_csv_file, delimiter = ',')

    # Read and save the header row first
    pybank_csv_header = next(pybank_csv_reader)

    # Initialize variable to store the total number of months in the dataset
    total_months = 0

    # Initialize variable to store the net total amount of Profit/Losses
    net_pl_amount = 0

    # Initialize variables to store the current and previous month's Profit/Losses
    curr_month_pl = 0
    prev_month_pl = 0

    # Initialize variable to store the monthly change in Profit/Losses (curr minus prev)
    monthly_pl_change = 0

    # Initialize variable to store the total change in Profit/Losses
    total_pl_change = 0

    # Initialize dictionary to store the Date and the corresponding change in Profit/Losses
    # Dictionary will be used to compute the greatest increase/decrease in Profit/Losses
    pybank_dict = {}

    # Read each row of budget data after the header to compute the necessary financial stats
    for budget_data in pybank_csv_reader:
        # Increment total_months variable by 1 for each row in the file 
        # Each row represents one month in the dataset
        total_months += 1

        # Store the current month's profit/loss value
        curr_month_pl = int(budget_data[1])

        # Add the net total amount of profit/loss based on current month's value
        # This maintains the cumulative total amount
        net_pl_amount += curr_month_pl

        # This condition checks if we are reading the first month's data in the csv 
        # If it's the first month then there is nothing to compute/compare against
        # For subsequent months the block computes and stores all the necessary stats            
        if total_months != 1:
            # Compute monthly change in profit/loss as the current month's value minus previous month's value
            monthly_pl_change = curr_month_pl - prev_month_pl
            
            # Capture the cumulative total change in profit/loss based on the monthly change value 
            total_pl_change += monthly_pl_change

            # Store the Date as a key in the dictionary, and the Monthly change as the corresponding value 
            pybank_dict[budget_data[0]] = monthly_pl_change

        # Set the current month's profit/loss value to the previous
        # This allows us to compute the monthly change value in the subsequent iteration
        prev_month_pl = curr_month_pl

# Close the csv file after we are done reading and analyzing it
pybank_csv_file.close()

# Compute the average change in profit/loss
avg_pl_change = total_pl_change / (total_months - 1)

# Compute the greatest increase in profits from the dictionary (month and amount) 
max_profit_month = max(pybank_dict, key=pybank_dict.get)
max_profit_increase = max(pybank_dict.values())

# Compute the greatest decrease in profits from the dictionary (month and amount) 
min_profit_month = min(pybank_dict, key=pybank_dict.get)
min_profit_increase = min(pybank_dict.values())

# Initialize an empty list to store each "line" or "output" of the financial analysis results
# List will be used to print the results to terminal and export to a text file
pybank_analysis = []

# Add all of the analysis results to the list in the form of formatted output/lines
pybank_analysis.append("\nPYBANK FINANCIAL ANALYSIS")
pybank_analysis.append("\n" + "-" * 60)
pybank_analysis.append("\nTotal Months Analyzed: " + str(total_months))
pybank_analysis.append("\nNet Total Profit/Losses: ${:,}".format(net_pl_amount))
pybank_analysis.append("\nAverage of the changes in Profit/Losses: ${:.2f}".format(avg_pl_change))
pybank_analysis.append("\nGreatest Increase in Profits: " + max_profit_month + " (${:,})".format(max_profit_increase))
pybank_analysis.append("\nGreatest Decrease in Profits: " + min_profit_month + " (${:,})".format(min_profit_increase))
pybank_analysis.append("\n" + "-" * 60 + "\n")

# Print the contents of the list to the terminal
print(*pybank_analysis)

# Create the file path for the output file that we want to export the results to
output_file_path = os.path.join(os.getcwd(), 'pybank_output.txt')

# Open the output text file for writing
with open(output_file_path,'w') as pybank_output_file:

    # Use list comprehension to write the contents of the list to the output file
    pybank_output_file.writelines(pybank_contents for pybank_contents in pybank_analysis)

# Close the text file once done writing to it
pybank_output_file.close()