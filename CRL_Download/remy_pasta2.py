'''

Script: Download CRLS + DOD Bundle Into Selected Directory
Author: Charlie Perez
Date: July 2025
Purpose: This script downloads the (non-tfr systems).

'''

''' IMPORT STANDARD LIBRARIES '''
# Import the os module, which provides a way to interact with the operating system
import os

# Import the requests module, which provides a way to send HTTP requests
import requests

# Import your crl_urls list, which contains a list of CRL URLs to download
from crl_urls import crl_urls

# Import the urlparse and unquote functions from the urllib.parse module
from urllib.parse import urlparse, unquote


'''MAIN ENTRY POINT'''

# Define a function called download_crls, which will be used to download the CRLs
def download_crls():
    # Define a variable called download_dir, which will be used to store the downloaded CRLs
    download_dir = r"C:\crls\new_crls"

    # Use the os.makedirs function to create the download directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)

    # Iterate over each URL in the crl_urls list
    for url in crl_urls:
        try:
            # Use the requests.get function to send a GET request to the URL and get the response
            response = requests.get(url, stream=True)

            # Check if the response status code is 200, which indicates a successful request
            if response.status_code == 200:
                # Get the Content-Disposition header from the response, which contains the file name
                content_disposition = response.headers.get('Content-Disposition')

                # Check if the Content-Disposition header is set
                if content_disposition:
                    # Split the Content-Disposition header to get the file name
                    file_name = content_disposition.split('filename=')[1].strip('"')

                    # Use the unquote function to decode the file name and replace any URL-encoded characters
                    file_name = unquote(file_name)
                else:
                    # If the Content-Disposition header is not set, use the URL path to get the file name
                    parsed_url = urlparse(url)

                    # Get the path component of the URL
                    file_name = os.path.basename(parsed_url.path)

                    # If the filename is empty use the following default name
                    if not file_name:                       
                        file_name = 'crl_bundle.zip'

                    # Convert any URL-encoded characters into spaces
                    file_name = unquote(file_name)

                # Remove characters not allowed in Windows filenames and replace them
                invalid_chars = '<>:"/\\|?*'
                for char in invalid_chars:
                    file_name = file_name.replace(char, '')

                # Create the complete directory path where the file will be saved
                save_path = os.path.join(download_dir, file_name)

                # Save the downloaded file
                with open(save_path, 'wb') as f:
                    # Download in chunks to handle large files
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Let the user know the operation was a success!
                print(f"Successfully downloaded {file_name} to {save_path}")
            else:
                # Let the user know the operation failed :(
                print(f"Failed to download {url}. Status code: {response.status_code}")
        except Exception as e:
            # Show an error message if anything goes wrong
            print(f"Error downloading {url}: {str(e)}")

# This will only run if you execute the file directly
if __name__ == "__main__":
    # Call the main download_crls function to begin your downloads
    download_crls()