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

# Loop 3 times to assess the three text files we have already prepared
for file_num in range(3):

    # Sets the txt file that you want the script to read
    input_txt_file = "paragraph_" + str(file_num + 1) + ".txt"
    # Call function to analyze the passage in the text file and save the metrics to a list
    pypara_metrics = pyparagraph.analyze_passages(input_txt_file)
    # Call function to print the list of metrics to terminal
    pyparagraph.print_metrics(pypara_metrics, input_txt_file)