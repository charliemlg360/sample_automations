# copy_to_external.py
import os
import shutil

def copy_to_external():
    download_dir = r"C:\Users\Carlos.Perez\Downloads\new_crls"
    external_drive = r"D:\new_crls\new_crls"
    os.makedirs(external_drive, exist_ok=True)
    
    for file in os.listdir(download_dir):
        file_path = os.path.join(download_dir, file)
        if os.path.isfile(file_path):
            shutil.copy2(file_path, external_drive)
            print(f"Successfully copied {file} to {external_drive}")
        else:
            print(f"Skipping directory {file}")

if __name__ == "__main__":
    copy_to_external()