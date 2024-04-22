import requests
from bs4 import BeautifulSoup
import os
import time

def download_comic(base_url, save_dir, start_page, end_page):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Iterate over each comic page
    for page_number in range(start_page, end_page + 1):
        # Construct the URL for the current comic page
        comic_url = f"{base_url}/{page_number}"

        # Download the HTML content of the comic page
        response = requests.get(comic_url)
        soup = BeautifulSoup(response.content, 'lxml')

        # Find the image element containing the comic image
        image_element = soup.find('img', class_='lazyload')

        # Get the image URL from the image element
        if image_element is not None:
            image_url = image_element['data-src']

            # Download the image and save it to the save directory
            image_filename = os.path.join(save_dir, f"{page_number}.jpg")
            image_response = requests.get(image_url)
            with open(image_filename, 'wb') as f:
                f.write(image_response.content)

            # Print a message to indicate progress
            print(f"Downloaded image for comic {page_number}")

        # Add a delay between downloading images to avoid overloading the website
        time.sleep(1)

if __name__ == "__main__":
    # Set the base URL of the comic website
    base_url = "https://www.ffmh123.com/update(https://www.ffmh123.com/book/3137)"

    # Set the save directory for the images
    save_dir = "/Users/heoo0124/Desktop/AA/YIREN/comics"

    # Set the start and end page numbers to scrape
    start_page = 1
    end_page = 688

    # Download the images from the specified pages
    download_comic(base_url, save_dir, start_page, end_page)
