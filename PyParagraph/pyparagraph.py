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

    # ===================================================================================================
    # The analyze_passages function reads a text file and asseses it for each of the following metrics:
    # 1) Approximate word count
    # 2) Approximate sentence count
    # 3) Approximate letter count (per word)
    # 4) Average sentence length (in words)
    # ===================================================================================================
    def analyze_passages(text_file_name):

        # Create file path for the text file to be assessed
        pypara_text_path = os.path.join(os.getcwd(), text_file_name)

        # Open the text file for reading
        with open(pypara_text_path, 'r') as pypara_text_file:

            # Read all the lines from the text file
            pypara_text = pypara_text_file.readlines()

            # Initalize list of sentences that will have the newline character stripped out 
            stripped_para = []

            # Parse each line of text
            for each_line in pypara_text:
                 # Strip newline character from each line of text and save to list
                stripped_para.append(each_line.strip("\n")) 

        # Close the text file after we are done reading and analyzing it
        pypara_text_file.close()

        # Initialize lists to store all words, sentences and words within each sentence 
        words = []
        sentences = []
        words_in_sentence = []

        # Initialize counters for the passage analysis metrics 
        word_count = 0
        sentence_count = 0
        letter_count = 0
        avg_letter_count = 0
        words_per_sentence = 0
        avg_sentence_length = 0

        # Parse each line of text that had the newline stripped out
        for each_line in stripped_para:
            # Split each line into a list of words
            if each_line != '':
                words = each_line.split()
                # Count the number of words and increment counter each time
                word_count += len(words)
                # Iterate through each word in the words list
                for word in words:
                    # Calculate the letter count based on length of each word
                    letter_count += len(word)
                # Split each line into a list of sentences using a regular expression
                sentences = re.split("(?<=[.!?]) +", each_line)
                # Remove any empty/null strings from sentences
                sentences = list(filter(None, sentences))
                # Count the number of sentences and increment counter each time
                sentence_count += len(sentences)
                # Iterate through each sentence
                for sentence in sentences:
                    # Split each sentence into a list of words
                    words_in_sentence = sentence.split()
                    # Calculate words per sentence
                    words_per_sentence += len(words_in_sentence)

        # Calculate average letter count
        avg_letter_count = letter_count / word_count
        # Calculate average length of sentence
        avg_sentence_length = words_per_sentence / sentence_count

        # Store all the calculated metrics into a list for printing later
        pypara_metrics = [pypara_text_path, word_count, sentence_count, avg_letter_count, avg_sentence_length]

        # Return list of metrics to calling function
        return pypara_metrics

    # ====================================================================
    # The print_metrics function prints the passage's metrics to terminal
    # ====================================================================
    def print_metrics(pypara_metrics, text_file_name):
        
        # Initialize empty list
        pypara_analysis = []

        # Add all of the metrics that were analyzed to the list for printing with formatted output
        pypara_analysis.append("\nPARAGRAPH ANALYSIS")
        pypara_analysis.append("\n" + "-" * 30)
        pypara_analysis.append("\nText File Analyzed: " + pypara_metrics[0])
        pypara_analysis.append("\nApproximate Word Count: " + str(pypara_metrics[1]))
        pypara_analysis.append("\nApproximate Sentence Count: " + str(pypara_metrics[2]))
        pypara_analysis.append("\nAverage Letter Count: " + str(round(pypara_metrics[3], 1)))
        pypara_analysis.append("\nAverage Sentence Length: " + str(round(pypara_metrics[4], 1))) 
        pypara_analysis.append("\n" + "-" * 30 + "\n")

        # Print list to terminal
        print (*pypara_analysis)
        
else:
        # Let the user know that they can't run this module by itself
        print("\nThis is the pyparagraph.py module that executes only when imported and run via another script. Try running \"python main.py\" instead. \n")