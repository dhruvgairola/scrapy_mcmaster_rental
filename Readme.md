This project is for McMaster University students who are looking to rent rooms via the McMaster offcampus housing website. I personally found that manually going through the ads was a huge drain on my time since I would manually input the address into Google maps to check how far it was from the campus. Also, if a rental search was unsuccessful for that week, you'd probably have to search the listings again, which would keep getting updated, wasting time again. Keywords like "Female house only" meant that males would not be rented a house. Listings on the website can only be sorted according to a few attributes.

Hence, I decided to scrape the McMaster housing website to collect all the relevant information, filter irrelevant information and sort listings according to what's important.

You will need Python 2.7, pip, and a Google Maps API key.

#### Installation steps :
```
1. Install the following packages:
> pip install Scrapy
> pip install service_identity
> pip install pygeocoder
2. Visit the APIs Console at https://code.google.com/apis/console and log in with your Google Account.
3. Click the APIs link from the left-hand menu.
4. Activate the Geocoding API service.
5. Click the Credentials link from the left-hand menu. Your API key is available here.
6. Add your Google API key to maps_api_key.txt as the first and only line.
```

#### Additional configuration :

To add urls to scrape, append new elements to the "start_urls" list in the scrapy_mac_rent_spider.py file. To scrape rentals, run this command from the top level directory.
```
> scrapy crawl macrent -o items.json
```
This command creates an items.json file containing all the scraped listings.

If you don't want to provide a Google Maps API, toggle "shouldUseGoogleMaps" to False in the scrapy_mac_rent_spider.py file.

#### Disclaimer :

Please use this program responsibly. Scraping code was tested working as of July 2014. Any changes on the website being scraped would necessarily require modifications to the scraping logic.
