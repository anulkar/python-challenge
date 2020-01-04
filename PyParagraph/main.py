# ===================================================================
# PYTHON HOMEWORK - PyParagraph
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# ===================================================================
# This is the Main Python script to run for the PyParagraph analysis.
# ===================================================================

# Import the pyparagraph module
# Module contains functions to:
# 1) Assess paragraphs within a text file
# 2) Generate simple metrics
import pyparagraph

# Sets the txt file that you want the script to read
input_txt_file = "paragraph_2.txt"

# Call function to process the csv file and convert the employee records
pypara_metrics = pyparagraph.analyze_passages(input_txt_file)

# Call function to print the metrics to terminal
pyparagraph.print_metrics(pypara_metrics, input_txt_file)