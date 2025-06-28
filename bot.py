import requests
import tweepy
from bs4 import BeautifulSoup

# Twitter credentials (Tweepy v2 client)
consumer_key = 'sK7YeAis3LbNSK2wRzqMFEXCK'
consumer_secret = 'kTLn8HSHwMBdAO6PFArcJDRrDHgzxMK1fJ1RgPtsIuiJq1t5TL'
access_token = '1938981766104072192-5aIFTs7EdXNEYMPMFVXSiDeRjVR366'
access_token_secret = 'CE7KbykD8W9msVe8Brp16gIyKqCeuOrstfMLTqhgKNvET'

# Initialize Tweepy Client (v2)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def download_image(filename='face.jpg'):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }
    page_url = 'https://this-person-does-not-exist.com/en'
    response = requests.get(page_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tag = soup.find('img')
    if img_tag and 'src' in img_tag.attrs:
        image_url = img_tag['src']
        if image_url.startswith('/'):
            image_url = 'https://this-person-does-not-exist.com' + image_url

        img_response = requests.get(image_url, headers=headers)
        img_response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(img_response.content)
        return filename
    else:
        raise Exception("Image URL not found on page")

def post_image(image_path):
    media = client.media_upload(image_path)
    client.create_tweet(media_ids=[media.media_id])

def main():
    image_file = download_image()
    post_image(image_file)

if __name__ == '__main__':
    main()


