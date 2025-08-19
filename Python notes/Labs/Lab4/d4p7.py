# Write a code to unzip the zipped file downloaded in
import zipfile

with zipfile.ZipFile("output.zip", 'r') as zip_ref:
    zip_ref.extractall("Unzipped detq")
print("File unzipped successfully!")
