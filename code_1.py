import requests
import os

# Prompt the user to enter the URL of the image they want to download
image_url = input("Enter the URL of the image you want to download: ")

# Send a GET request to the URL to download the image
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the filename from the URL (after the last '/')
    filename = image_url.split("/")[-1]

    # Get the file extension from the filename
    file_extension = os.path.splitext(filename)[-1].lower()

    # Open a file in binary mode and write the image content to it
    with open(filename, "wb") as f:
        f.write(response.content)

    print("Image saved to", filename)
else:
    print("Error:", response.status_code)
