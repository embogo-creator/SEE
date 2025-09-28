import os
import requests
from urllib.parse import urlparse

def fetch_image():
    print("Ubuntu-Inspired Image Fetcher 🖼️")
    print("The Wisdom of Ubuntu: 'I am because we are'\n")

    # Prompt user for an image URL
    url = input("Enter the URL of an image: ").strip()

    # Directory to save images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad HTTP status

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no valid extension, assign default name
        valid_extensions = (".jpg", ".jpeg", ".png", ".gif")
        if not filename.lower().endswith(valid_extensions):
            filename = "downloaded_image.jpg"

        # Full save path
        filepath = os.path.join(save_dir, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"✅ Image saved successfully as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("⚠️ Invalid URL. Please provide a correct image link.")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Could not reach the server.")
    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️ HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
