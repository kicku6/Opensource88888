import csv
import os
import requests
import base64
from PIL import Image
from io import BytesIO
import threading
from fake_useragent import UserAgent

# Function to extract and save base64 content from a URL with a random user agent
def extract_base64_from_url(url):
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            base64_content = base64.b64encode(response.content).decode('utf-8')
            filename = url[-4:] + '.txt'
            with open(filename, 'w') as file:
                file.write(base64_content)
            convert_base64_to_image(base64_content, filename)
        else:
            print(f"Failed to retrieve content from {url}")
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

# Function to convert base64 to image and save
def convert_base64_to_image(base64_content, filename):
    try:
        image_data = base64.b64decode(base64_content)
        img = Image.open(BytesIO(image_data))
        img.save(filename[:-4] + '.png', 'PNG')
        print(f"Converted and saved {filename[:-4]}.png")
    except Exception as e:
        print(f"Error converting {filename} to image: {str(e)}")

# Read URLs from a CSV file
def process_csv_file(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            url = row[0]
            t = threading.Thread(target=extract_base64_from_url, args=(url,))
            t.start()

if name == '__main__':
    csv_file = 'urls.csv'  # Replace with the path to your CSV file
    if os.path.exists(csv_file):
        process_csv_file(csv_file)
    else:
        print("CSV file not found. Please provide a valid CSV file path.")



        """
        You are a professional python programmer.

        I would like you to write a script to extract base64 contents from a list of urls from a csv file.
        Please store the base64 contents from each url in a text file with the last 4 characters of the url link as the name of the text file.
        Do this recursively and simultaneously with the multithreading function.
        Finally with the base64 contents extracted in each text files, recursively convert the base64 contents to image and store as jpg or png format to show as image.
        Name each saved image in the same format as the text files.

        """