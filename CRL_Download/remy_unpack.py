'''

Script: Unzip the CRL File
Author: Charlie Perez
Date: July 2025
Purpose: This script unzips the contents of your CRL zip file into a target directory and then removes the zip file itself.

'''

''' IMPORT STANDARD LIBRARIES '''
import os
import zipfile


'''MAIN ENTRY POINT'''
# Define the main function
def unzip_crls():
    # Define a variable called download_dir, where your CRL files are
    download_dir = r"C:\Users\carlitos\Downloads\new_crls"

    # Define a variable called zip_file, which stores the path to the ZIP file
    zip_file = os.path.join(download_dir, 'ALLCRLZIP.zip')

    # Check if the ZIP file exists
    if os.path.exists(zip_file):
        # Use the zipfile.ZipFile function to open the ZIP file in read mode
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Use the extractall method to extract the contents of the ZIP file to the download directory
            zip_ref.extractall(download_dir)

        # Print a success message
        print("Successfully unzipped the CRL bundle")

        # Use the os.remove function to remove the ZIP file
        os.remove(zip_file)

        # Print a message indicating that the ZIP file has been removed
        print("Removed the ZIP file")
    else:
        # Print an error message if the ZIP file does not exist
        print("No ZIP file found to unzip")

# Check to see if script is being executed directly
if __name__ == "__main__":
    # Calls the unzip_crls function
    unzip_crls()