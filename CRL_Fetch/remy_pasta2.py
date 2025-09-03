# Import the os module, which provides a way to interact with the operating system
import os

# Import the requests module, which provides a way to send HTTP requests
import requests

# Import the crl_urls module, which contains a list of CRL URLs to download
from crl_urls import crl_urls

# Import the urlparse and unquote functions from the urllib.parse module
from urllib.parse import urlparse, unquote

# Define a function called download_crls, which will be used to download the CRLs
def download_crls():
    # Define a variable called download_dir, which will be used to store the downloaded CRLs
    download_dir = r"C:\Users\Carlos.Perez\Downloads\new_crls"

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

                    # Check if the file name is empty
                    if not file_name:
                        # If the file name is empty, use a default file name
                        file_name = 'crl_bundle.zip'

                    # Use the unquote function to decode the file name and replace any URL-encoded characters
                    file_name = unquote(file_name)

                # Replace any invalid characters in the file name
                invalid_chars = '<>:"/\\|?*'

                # Iterate over each invalid character
                for char in invalid_chars:
                    # Replace the invalid character with an empty string
                    file_name = file_name.replace(char, '')

                # Create the full path to the file
                save_path = os.path.join(download_dir, file_name)

                # Open the file in binary write mode
                with open(save_path, 'wb') as f:
                    # Iterate over each chunk of the response content
                    for chunk in response.iter_content(chunk_size=8192):
                        # Write the chunk to the file
                        f.write(chunk)

                # Print a success message
                print(f"Successfully downloaded {file_name} to {save_path}")
            else:
                # Print an error message if the response status code is not 200
                print(f"Failed to download {url}. Status code: {response.status_code}")
        except Exception as e:
            # Print an error message if an exception occurs
            print(f"Error downloading {url}: {str(e)}")

# Check if the script is being run directly (not being imported as a module)
if __name__ == "__main__":
    # Call the download_crls function to start the download process
    download_crls()