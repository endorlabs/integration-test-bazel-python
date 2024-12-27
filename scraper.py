import aiohttp
import requests
from bs4 import BeautifulSoup
from utils.asyncRunner import runAsync

async def scrape_website(url, depth=1):
    try:
        # Send a GET request to the website
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.text()

        # Parse the HTML content of the page
        soup = BeautifulSoup(content, 'lxml')

        # Extract and print the title of the page
        title = soup.title.string if soup.title else 'No title found'
        print(f"Page Title: {title}")

        # Example: Extract all links on the page
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print("Links found on the page:")
        for link in links:
            print(link)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url_to_scrape = input("Enter the URL to scrape: ")
    depth = int(input("Enter the depth for scraping: "))
    runAsync(scrape_website, url_to_scrape)