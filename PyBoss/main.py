# =================================================================
# PYTHON HOMEWORK - PYBOSS EMPLOYEE DATA CLEANUP
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# =================================================================
# This is the Main Python script to run for the PyBoss analysis.
# =================================================================

# Import the pyboss module
# Module contains functions to:
# 1) Convert the employee data and
# 2) Export the cleaned data to csv file
import pyboss

# Sets the csv file that you want the script to read
input_csv_file = "employee_data.csv"

# Call function to process the csv file and convert the employee records
cleaned_employee_records = pyboss.convert_employee_records(input_csv_file)

# Sets the csv file that you want to write the clean records to
output_csv_file = "pyboss_output.csv"

# Call function to export the cleaned up employee data to a new csv file
pyboss.export_to_csvfile(output_csv_file, cleaned_employee_records)