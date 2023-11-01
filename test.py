from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests

params = {
        "engine": "google_reverse_image",
        "image_url": "https://twitter.com/sumikowrestles/status/1509644630693855233/photo/1",
        "api_key": "e6e58fe1c5b8dc37a294e03f6947b05eab8093aee7001be2729ce26839b40797"
    }

search = GoogleSearch(params)
results = search.get_dict()
print(results)
# inline_images = results["inline_images"]

# def get_imgur_direct_image_url(imgur_page_url):
#     response = requests.get(imgur_page_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     image_element = soup.find('img', {'class': 'post-image-placeholder'})
#     if image_element:
#         image_url = image_element['src']
#         if image_url.startswith('//'):
#             image_url = f'https:{image_url}'
#         return image_url
#     return None

# imgur_page_url = "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQi4a8NzG1ocCbgUUZxxDLocQwDQvhod4gHC3aRRg3juK0LDsZHECn7AwMJq8WUmPFLai9IJhY5YWNLRys"
# direct_image_url = get_imgur_direct_image_url(imgur_page_url)

# if direct_image_url:
#     print(f"Direct image URL: {direct_image_url}")
# else:
#     print("Unable to find the direct image URL.")