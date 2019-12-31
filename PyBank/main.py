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

pybank_csv_file.close()

avg_pl_change = total_pl_change / (total_months - 1)

max_profit_month = max(pybank_dict, key=pybank_dict.get)
max_profit_increase = max(pybank_dict.values())

min_profit_month = min(pybank_dict, key=pybank_dict.get)
min_profit_increase = min(pybank_dict.values())

pybank_analysis = []

pybank_analysis.append("\nPyBank Financial Analysis\n-----------------------------------------------------------------------\n")
pybank_analysis.append("Total Months Analyzed: " + str(total_months) + "\n")
pybank_analysis.append("Net Total Profit/Losses over this period: ${:,}\n".format(net_pl_amount))
pybank_analysis.append("Average of the changes in Profit/Losses over this period: ${:.2f}\n".format(avg_pl_change))
pybank_analysis.append("Greatest Increase in Profits over this period: " + max_profit_month + " (${:,})\n".format(max_profit_increase))
pybank_analysis.append("Greatest Decrease in Profits over this period: " + min_profit_month + " (${:,})\n".format(min_profit_increase))

print(*pybank_analysis)

#print("\nPyBank Financial Analysis\n-----------------------------------------------------------------------")
#print(f"Total Months Analyzed: {total_months}")
#print(f"Net Total Profit/Losses over the {total_months} months: ${net_pl_amount:,}")
#print(f"Average of the changes in Profit/Losses over the {total_months} months: ${avgPLChange:.2f}")
#print(f"Greatest Increase in Profits over the {total_months} months: {max_profit_increase} (${max(pybank_dict.values()):,})")
#print(f"Greatest Decrease in Profits over the {total_months} months: {min_profit_increase} (${min(pybank_dict.values()):,})\n")

output_file_path = os.path.join(os.getcwd(), 'pybank_output.txt')

with open(output_file_path,'w') as pybank_output_file:
    pybank_output_file.writelines(pybank_contents for pybank_contents in pybank_analysis)

pybank_output_file.close()