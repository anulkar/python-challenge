# ==================================================================================================
# PYTHON HOMEWORK - PYBOSS EMPLOYEE DATA CLEANUP
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# ==================================================================================================
# This is the main module that converts Employee data records in a csv file to the required format.
# The csv dataset is composed of columns: Emp ID, Name, DOB, SSN, State.
# The converted dataset is exported to a new csv file in the same folder.
# ==================================================================================================

# Execute only when another script imports this as a module
if __name__ != "__main__":

    # Import the os module to create file paths across operating systems
    import os

    # Import module for reading csv files
    import csv

    # ========================================================================================================
    # The convert_employee_records function reads the employee data csv file and converts the data as follows:
    # a) The 'Name' column is split into separate 'First Name' and 'Last Name' columns.
    # b) The 'DOB' data is re-written into MM/DD/YYYY format.
    # c) The 'SSN' data is re-written such that the first five numbers are hidden from view.
    # d) The 'State' data is re-written as simple two-letter abbreviations.
    # ========================================================================================================
    def convert_employee_records(csv_file_name):

        # Create the file path for the employee data.csv file
        pyboss_csv_path = os.path.join(os.getcwd(), csv_file_name)

        # Initalize lists to store the converted data fields/columns
        emp_id = []
        emp_firstname = []
        emp_lastname = []
        emp_dob = []
        emp_ssn = []
        emp_state = []

        # Dictionary that is used to find state abbreviations 
        us_state_abbrev = {
                            'Alabama': 'AL',
                            'Alaska': 'AK',
                            'Arizona': 'AZ',
                            'Arkansas': 'AR',
                            'California': 'CA',
                            'Colorado': 'CO',
                            'Connecticut': 'CT',
                            'Delaware': 'DE',
                            'Florida': 'FL',
                            'Georgia': 'GA',
                            'Hawaii': 'HI',
                            'Idaho': 'ID',
                            'Illinois': 'IL',
                            'Indiana': 'IN',
                            'Iowa': 'IA',
                            'Kansas': 'KS',
                            'Kentucky': 'KY',
                            'Louisiana': 'LA',
                            'Maine': 'ME',
                            'Maryland': 'MD',
                            'Massachusetts': 'MA',
                            'Michigan': 'MI',
                            'Minnesota': 'MN',
                            'Mississippi': 'MS',
                            'Missouri': 'MO',
                            'Montana': 'MT',
                            'Nebraska': 'NE',
                            'Nevada': 'NV',
                            'New Hampshire': 'NH',
                            'New Jersey': 'NJ',
                            'New Mexico': 'NM',
                            'New York': 'NY',
                            'North Carolina': 'NC',
                            'North Dakota': 'ND',
                            'Ohio': 'OH',
                            'Oklahoma': 'OK',
                            'Oregon': 'OR',
                            'Pennsylvania': 'PA',
                            'Rhode Island': 'RI',
                            'South Carolina': 'SC',
                            'South Dakota': 'SD',
                            'Tennessee': 'TN',
                            'Texas': 'TX',
                            'Utah': 'UT',
                            'Vermont': 'VT',
                            'Virginia': 'VA',
                            'Washington': 'WA',
                            'West Virginia': 'WV',
                            'Wisconsin': 'WI',
                            'Wyoming': 'WY',
                        }

        # Open the csv file for reading
        with open(pyboss_csv_path, newline = '') as pyboss_csv_file:

            # Let the user know the file that is being analyzed
            print(f"\nAnalyzing the Employee Data File: {pyboss_csv_path}") 

            # CSV reader specifies delimiter and variable that holds the contents of the data file
            pyboss_csv_reader = csv.reader(pyboss_csv_file, delimiter = ',')

            # Read the header row first
            next(pyboss_csv_reader)

            # Import the datetime module to access datetime objects for converting the DOB data
            from datetime import datetime

            # Read each row of csv
            for row in pyboss_csv_reader:

                # Add the employee ID to the list
                emp_id.append(row[0])

                # Split the Name into First and Last Name and add to respective lists
                emp_name = row[1].split()
                emp_firstname.append(emp_name[0])
                emp_lastname.append(emp_name[1])

                # Read existing DOB format in a datetime object
                dob_object = datetime.strptime(row[2], '%Y-%m-%d')
                # Perform conversion to MM/DD/YYYY format using the object and add to the list
                converted_dob = dob_object.strftime('%m/%d/%Y')
                emp_dob.append(converted_dob)

                # Mask the first 5 SSN numbers with asterisks and add to the list
                ssn = row[3]
                emp_ssn.append("***-**-" + ssn[7:])

                # Determine the State abbreviation using the dictionary and add to list
                emp_state.append(us_state_abbrev[row[4]])

        # Close the csv file after we are done reading and analyzing it
        pyboss_csv_file.close()

        # Zip up the converted data fields (i.e. lists) into a new tuple
        cleaned_employee_records = zip(emp_id, emp_firstname, emp_lastname, emp_dob, emp_ssn, emp_state)

        # Return the cleaned records tuple to the calling function so they can be exported to csv
        return cleaned_employee_records

    # =================================================================================
    # The export_to_csvfile function exports the converted employee data to a csvfile
    # =================================================================================
    def export_to_csvfile(output_csv_file, cleaned_employee_records):
        # Create the file path for the output file that we want to export the data to
        output_file_path = os.path.join(os.getcwd(), output_csv_file)

        # Open the output csv file for writing
        with open(output_file_path, "w", newline="") as pyboss_output_file:

            # Create a writer object for the csv file
            writer = csv.writer(pyboss_output_file)

            # Write the header row
            writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

            # Write in the cleaned up zipped rows
            writer.writerows(cleaned_employee_records)

        # Close the csv file once done writing to it
        pyboss_output_file.close()

        # Let the user know that we are done exporting the file
        print(f"\nDone...Converted Employee Data saved to: {os.getcwd()}/{output_csv_file}\n")
else:
        # Let the user know that they can't run this module by itself
        print("\nThis is the pyboss.py module that executes only when imported and run via another script. Try running \"python main.py\" instead. \n")