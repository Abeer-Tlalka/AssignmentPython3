# 1. Write a Python program to read a text file and count the occurrences of each word.
def count_words(filename):
    ''''
    Function to read a text file and count the occurrences of each word
    :param file_name: Name of the text file
    :return: A dictionary with words as keys and their frequencies as values
    '''
    word_count = {}  # Dictionary to store word counts

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            text = file.read()

            # Convert all words to lowercase and split the text into words
            words = text.lower().split()

            # Count occurrences of each word
            for word in words:
                word = word.strip('.,!?";:')  # Remove punctuation marks
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
        return word_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return {}
    
    
# 2. Create a program to merge the contents of two text files into one.
def merge_files(file1, file2, output_file):
    '''
    Function to merge the contents of two text files into a new file
    :param file1: Name of the first text file
    :param file2: Name of the second text file
    :param output_file: Name of the new file where the merged content will be written
    '''
    try:
        # Open the first and second files in read mode, and the output file in write mode
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
            # Read the content from both files
            content1 = f1.read()
            content2 = f2.read()

            # Write the content of both files to the output file
            output.write(content1)
            output.write("\n")  # Optionally add a newline between the two file contents
            output.write(content2)

        print(f"Contents of '{file1}' and '{file2}' have been merged into '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")



# 3. Write a function to search for a specific word in a file and print its line number.
def search_word(file_name, word):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, 1):
                if word in line:
                    print(f"Line number {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
# 4. Implement a Python script to count the number of lines, words, and characters in a file.
def count_lines_words_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            word_count = len(lines[0].split())
            character_count = sum(len(line) for line in lines)
            line_count = len(lines)
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
            print(f"Number of characters: {character_count}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")










# # Test the function
# file_name = 'src/text.txt'  # Replace with your text file
# word_occurrences = count_words(file_name)
# print("Word Occurrences:", word_occurrences)

#merge files example:
# file1 = 'src/file1.txt'
# file2 = 'src/file2.txt'
# output_file = 'src/merged_output.txt'

# merge_files(file1, file2, output_file)

# file1 = 'src/file1.txt'

# print(search_word(file1, 'some'))
# print(count_lines_words_characters(file1))