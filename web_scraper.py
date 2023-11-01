import requests
from bs4 import BeautifulSoup
url = "https://www.bing.com/"
response = requests.get("https://www.bing.com/")
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    # Print the clean text to the console
    print(text)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

with open("scraped_text.txt", "w", encoding="utf-8") as file:
    file.write(text)
    print("Scraped text saved to 'scraped_text.txt'")