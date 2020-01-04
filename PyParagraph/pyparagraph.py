# ==============================================================================
# PYTHON HOMEWORK - PyParagraph
# GT DATA SCIENCE BOOTCAMP
# PROGRAMMED BY: ATUL NULKAR
# Date: JANUARY 2020
# ==============================================================================
# This is the main module that analyzes passages/paragraphs within a text file.
# It produces a simple set of metrics to assess the complexity of the passages.
# ==============================================================================

# Execute only when another script imports this as a module
if __name__ != "__main__":

    # Import the os module to create file paths across operating systems
    import os

    # Import the regular expressions module
    import re

    # ========================================================================================================
    # The analyze_passages function reads a text file and asseses it for each of the following metrics:
    # 1) Approximate word count
    # 2) Approximate sentence count
    # 3) Approximate letter count (per word)
    # 4) Average sentence length (in words)
    # ========================================================================================================
    def analyze_passages(text_file_name):

        # Create file path for the text file to be assessed
        pypara_text_path = os.path.join(os.getcwd(), text_file_name)

        # Open the text file for reading
        with open(pypara_text_path, 'r') as pypara_text_file:

            # Read all the lines from the text file
            pypara_text = pypara_text_file.readlines()

            # List of sentences with newline character stripped out 
            stripped_para = []

            # Parse each line of text
            for each_line in pypara_text:
                 # Strip unnecessaru characters out and save each line to a new list
                stripped_para.append(each_line.strip("\n")) 

        # Close the text file after we are done reading and analyzing it
        pypara_text_file.close()

        words = []
        sentences = []
        word_count = 0
        sentence_count = 0

        for each_line in stripped_para:
            # Split each line into a list of words
            if each_line != '':
                print("\nOriginal Line: " + each_line)
                words = each_line.split()
                # Count the number of words and increment counter each time
                print("\nWords:  " + str(words))  
                word_count += len(words)
                # Split each line into a list of sentences
                sentences = re.split("(?<=[.!?]) +", each_line)
                print("\nSentence List: " + str(sentences))
                # Remove any empty/null strings from sentences
                sentences = list(filter(None, sentences))
                print("\nSentence Cleaned: " + str(sentences))
                # Count the number of sentences and increment counter each time
                sentence_count += len(sentences)
                print("\nSentence Count: " + str(sentence_count))
                
        pypara_metrics = [pypara_text_path, word_count, sentence_count]

        return pypara_metrics

    # ====================================================================
    # The print_metrics function prints the passage's metrics to terminal
    # ====================================================================
    def print_metrics(pypara_metrics, text_file_name):
        
        pypara_analysis = []

        pypara_analysis.append("\nPARAGRAPH ANALYSIS")
        pypara_analysis.append("\n" + "-" * 30)
        pypara_analysis.append("\nText File Analyzed: " + pypara_metrics[0])
        pypara_analysis.append("\nApproximate Word Count: " + str(pypara_metrics[1]))
        pypara_analysis.append("\nApproximate Sentence Count: " + str(pypara_metrics[2]))
        #pypara_analysis.append("\nAverage Letter Count: " + str(pypara_metrics[2]))
        #pypara_analysis.append("\nAverage Sentence Length: " + str(pypara_metrics[3])) 
        pypara_analysis.append("\n" + "-" * 30 + "\n")

        print (*pypara_analysis)
        
else:
        # Let the user know that they can't run this module by itself
        print("\nThis is the pyparagraph.py module that executes only when imported and run via another script. Try running \"python main.py\" instead. \n")