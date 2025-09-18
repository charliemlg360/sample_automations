'''

Script: Extract the DOD CRL Archive
Author: Charlie Perez
Date: July 2025
Purpose: This script extracts the DOD CRL archive and then removes the archive afterwards

'''

''' IMPORT STANDARD LIBRARIES '''
# This lets us work with files and folders
import os
# This lets us work with ZIP files
import zipfile


'''MAIN ENTRY POINT'''
# This function extracts CRL files from a ZIP archive
def unzip_crls():
    # The folder where our ZIP file is located
    download_dir = r"C:\Users\Carlos.Perez\Downloads\new_crls"
    # The full path to our ZIP file
    zip_file = os.path.join(download_dir, 'ALLCRLZIP.zip')
    
    # Check if the ZIP file actually exists
    if os.path.exists(zip_file):
        # Open the ZIP file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Extract everything from the ZIP file to our folder
            zip_ref.extractall(download_dir)
        
        # Tell the user it worked
        print("Successfully unzipped the CRL bundle")
        
        # Delete the ZIP file since we don't need it anymore
        os.remove(zip_file)
        print("Removed the ZIP file")
    else:
        # Tell the user if we couldn't find the ZIP file
        print("No ZIP file found to unzip")

# This code runs when you execute this script directly
if __name__ == "__main__":
    # Start the unzipping process
    unzip_crls()