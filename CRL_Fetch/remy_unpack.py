# Import the os module, which provides a way to interact with the operating system
import os

# Import the zipfile module, which provides a way to work with ZIP files
import zipfile

# Define a function called unzip_crls, which will be used to unzip the CRLs
def unzip_crls():
    # Define a variable called download_dir, which will be used to store the downloaded CRLs
    download_dir = r"C:\Users\Carlos.Perez\Downloads\new_crls"

    # Define a variable called zip_file, which will be used to store the path to the ZIP file
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

# Check if the script is being run directly (not being imported as a module)
if __name__ == "__main__":
    # Call the unzip_crls function to start the unzipping process
    unzip_crls()