import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = "https://example.com"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the elements you want to extract
    # For example, let's extract all the text within <p> tags
    paragraphs = soup.find_all("p")

    # Save the clean text content to a file 
    # Changes by iqra
    with open("output.txt", "w") as file:  
        for paragraph in paragraphs:
            file.write(paragraph.get_text() + "\n")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
