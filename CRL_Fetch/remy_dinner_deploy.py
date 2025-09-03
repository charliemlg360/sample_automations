# main.py
import remy_pasta2
import remy_unpack
import remy_delivery

def main():
    print("Running CRL grab script...")
    remy_pasta2.download_crls()
    
    print("Running unzip script...")
    remy_unpack.unzip_crls()
    
    print("Running copy to external script...")
    remy_delivery.copy_to_external()

if __name__ == "__main__":
    main()