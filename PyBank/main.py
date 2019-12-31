# Main Python script to run for the PyBank analysis.

# ==============================================================================
# PYTHON HOMEWORK - PYBANK
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# ==============================================================================

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:
  # Financial Analysis
  # ----------------------------
  # Total Months: 86
  # Total: $38382578
  # Average  Change: $-2315.12
  # Greatest Increase in Profits: Feb-2012 ($1926159)
  # Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Import the os module to create file paths across operating systems
import os

# Import module for reading csv files
import csv

# Create the file path for the budget_data.csv file
pybank_csv_path = os.path.join(os.getcwd(), 'budget_data.csv')

with open(pybank_csv_path, newline = '') as pybank_csv_file:

    # CSV reader specifies delimiter and variable that holds the contents of the budget data file
    pybank_csv_reader = csv.reader(pybank_csv_file, delimiter = ',')

    # Read the header row first
    pybank_csv_header = next(pybank_csv_reader)

    # Initialize variable to store the total number of months in the dataset
    total_months = 0

    net_pl_amount = 0

    curr_month_pl = 0

    prev_month_pl = 0

    monthly_pl_change = 0

    total_pl_change = 0

    pybank_dict = {}

    # Read each row of budget data after the header
    for budget_data in pybank_csv_reader:
        # Increment total_months variable by 1 for each row in the file 
        # Each row represents one month in the dataset
        total_months += 1
        curr_month_pl = int(budget_data[1])
        net_pl_amount += curr_month_pl
        if total_months == 1:
            prev_month_pl = curr_month_pl
        else:
            monthly_pl_change = curr_month_pl - prev_month_pl
            total_pl_change += monthly_pl_change
            prev_month_pl = curr_month_pl
            pybank_dict[budget_data[0]] = monthly_pl_change

avgPLChange = total_pl_change / (total_months - 1)

max_profit_increase = max(pybank_dict, key=pybank_dict.get)
min_profit_increase = min(pybank_dict, key=pybank_dict.get)

print("\nPyBank Financial Analysis\n-----------------------------------------------------------------------")
print(f"Total Months Analyzed: {total_months}")
print(f"Net Total Profit/Losses over the {total_months} months: ${net_pl_amount:,}")
print(f"Average of the changes in Profit/Losses over the {total_months} months: ${avgPLChange:.2f}")
print(f"Greatest Increase in Profits over the {total_months} months: {max_profit_increase} (${max(pybank_dict.values()):,})")
print(f"Greatest Decrease in Profits over the {total_months} months: {min_profit_increase} (${min(pybank_dict.values()):,})\n")