# =================================================================
# PYTHON HOMEWORK - PYBANK FINANCIAL ANALYSIS
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# =================================================================
# This is the Main Python script to run for the PyBoss analysis.
# =================================================================

# Import the pyboss module
# Module contains functions to analyze the bank data and print+export the results to file
import pyboss

# Sets the csv file that you want the script to read
input_csv_file = "employee_data.csv"

# Call function to process the csv file and convert the employee records
cleaned_employee_records = pyboss.convert_employee_records(input_csv_file)

# Sets the csv file that you want to write the results to
output_csv_file = "pyboss_output.csv"

# Call function to export the converted employee data to a new csv file
pyboss.export_to_csvfile(output_csv_file, cleaned_employee_records)