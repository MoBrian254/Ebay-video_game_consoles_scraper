Description:

The provided Python script is a web scraper using BeautifulSoup and requests libraries to extract information from eBay's "Video Game Consoles" page. 
It specifically targets item-image, item-name, and item-price for each video game console listed on the page. 
The extracted data is then saved to a JSON file named ebay_items.json.

Guidelines for Usage:

Install Dependencies:

Install the required libraries using the command.

pip install beautifulsoup4 requests

Check Output:

The script will attempt to scrape the eBay page and create a JSON file (ebay_items.json) in the same directory.
If successful, the console will display a message indicating that the scraping was successful, and the data is saved.

Customization:

Modify the script as needed based on changes to the eBay page structure.

Error Handling:

The script checks for a successful HTTP response (status code 200) before proceeding with scraping.
If the request is unsuccessful, an error message will be displayed along with the status code.

Output File:

The script outputs a JSON file (ebay_items.json) containing information about item-images, item-names, and item-prices for video game consoles.
