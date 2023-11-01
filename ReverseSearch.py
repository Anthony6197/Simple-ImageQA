from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests

def imgSearch(img_url):
    # reverse img search
    # img = "https://i.imgur.com/5bGzZi7.jpg"

    params = {
        "engine": "google_reverse_image",
        "image_url": img_url,
        "api_key": "e6e58fe1c5b8dc37a294e03f6947b05eab8093aee7001be2729ce26839b40797"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    inline_images = results["inline_images"]
    sources = [image["source"] for image in inline_images]

    # web scraping
    soups = "Everything in <title> is information about this image: \n"

    for source in sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        soups += str(soup.title) + "\n"

    return soups

# write webscrape results
# with open("soups.txt", "w") as f:
#     f.write(soups)

# # debugging
# # write sources
# with open("sources.txt", "w") as f:
#     f.write(json.dumps(sources))

# # write inline_images
# with open("images.txt", "w") as f:
#     f.write(json.dumps(inline_images))

