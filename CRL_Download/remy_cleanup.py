'''

Script: Local Directory CRL Removal
Author: Charlie Perez
Date: July 2025
Purpose: This script removes old downloaded CRLS from both your local drives (non-tfr systems).

'''

''' IMPORT STANDARD LIBRARIES '''
# This lets us work with files and folders
import os


'''DEFINE VARIABLES'''

# Define a function called remove_crls, which will be used to remove the CRL files.
def remove_crls():
    # Define the directories to remove CRL files from.
    directories = [
        r"C:\crls\new_crls",
        r"D:\new_crls"
]

    # Put the file extension we want in a variable (.crl)
    file_extension = ".crl"


'''MAIN ENTRY POINT'''

    # This will remove CRL files from each directory with a loop that will go through every item in the directories list.
    for directory in directories:
        # This will loop through every single file and folder in each directory. 
        for file in os.listdir(directory):
            # This if statement will check to see if the filename ends with the extention we're looking for.
            if file.endswith(file_extension):
                # If this finds a .crl file it will create a full directory path to that file.
                file_path = os.path.join(directory, file)
                # For error handling
                try:
                    # Command used to remove the file
                    os.remove(file_path)
                    # Print a success message with an f-string to embed variables
                    print(f"Removed {file} from {directory}")
                    # If the try fails (wrong permissions set for example) run the except black instead of crashing. 
                except Exception as e:
                    # Print the specific error message with an f-string
                    print(f"Error removing {file} from {directory}: {str(e)}")

# This will only run if you execute the file directly.
if __name__ == "__main__":
    # Start the crl removal process.
    remove_crls()