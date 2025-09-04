'''

Script: Download, Unzip and Copy Latest CRLs to Your External Drive.
Author: Charlie Perez
Date: July 2025
Purpose: This script automates the downloading and transferring of CRLs.

'''

'''IMPORT DEPENDANCIES'''

import remy_pasta2
import remy_unpack
import remy_delivery

'''MAIN ENTRY POINT'''

def main():
    # Print a message stating the script has started
    print("Running CRL grab script...")
    # Call the download_crls function from the remy_pasta2 script to begin downloading your CRLs.
    remy_pasta2.download_crls()
    
    
    # Print a message stating the script has started
    print("Running unzip script...")
    # Call the unzip_crls function from the remy_unpack script
    remy_unpack.unzip_crls()
    
    # Print a message stating the script has started
    print("Running copy to external script...")
    # Call the copy_to_external function from the remy_delivery script
    remy_delivery.copy_to_external()

# Check to see if script is being run directly
if __name__ == "__main__":
    #Call the main function
    main()