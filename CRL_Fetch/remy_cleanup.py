# Import the os module, which provides a way to interact with the operating system
import os

# Define a function called remove_crls, which will be used to remove the CRL files
def remove_crls():
    # Define the directories to remove CRL files from
    directories = [
        r"C:\Users\Carlos.Perez\Downloads\new_crls",
         r"D:\new_crls\new_crls"
    ]

    # Define the file extension to look for (CRL files have a .crl extension)
    file_extension = ".crl"

    # Remove CRL files from each directory
    for directory in directories:
        for file in os.listdir(directory):
            if file.endswith(file_extension):
                file_path = os.path.join(directory, file)
                try:
                    os.remove(file_path)
                    print(f"Removed {file} from {directory}")
                except Exception as e:
                    print(f"Error removing {file} from {directory}: {str(e)}")

# Check if the script is being run directly (not being imported as a module)
if __name__ == "__main__":
    # Call the remove_crls function to start the removal process
    remove_crls()