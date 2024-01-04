import requests
from bs4 import BeautifulSoup
import json

pages = 2

for p in range(pages):
  url = f"https://www.ebay.com/b/Video-Game-Consoles/139971/bn_320033?rt=nc&_dmd=2&_pgn={p}"

  #Auth headers
  headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.2; SM-T535) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Safari/537.36'
  }

  # Send a GET request to the URL
  response = requests.get(url, headers=headers)

  # Check if the request was successful (status code 200)
  if response.status_code == 200:
      # Parse the HTML content of the page using BeautifulSoup
     soup = BeautifulSoup(response.text, 'html.parser')

   # Find all the relevant elements on the page (item-image, item-name, item-price)
     items = []
     for item in soup.find_all('li', class_='s-item--large'):
       link = item.find('a', class_='s-item__link').get('href')
       image = item.find('img', class_='s-item__image-img')
       name = item.find('h3', class_='s-item__title')
       price = item.find('span', class_='s-item__price')

       if link and image and name and price:
          item_data = {
            "item_link": link,
            "item_image": image['src'],
            "item_name": name.get_text(strip=True),
            "item_price": price.get_text(strip=True).strip('to').replace('to', ' ')
          }
          items.append(item_data)
       print(items)

    # Output the data to a JSON file
     with open('ebay_items.json', 'w', encoding='utf-8') as json_file:
         json.dump(items, json_file, ensure_ascii=False, indent=2)

     print("Scraping successful. Data saved to ebay_items.json.")
  else:
      print(f"Failed to retrieve the page. Status code: {response.status_code}")
