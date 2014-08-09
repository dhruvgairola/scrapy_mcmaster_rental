This project is for McMaster University students who are looking to rent rooms via the McMaster offcampus housing website. I personally found that manually going through the ads was a huge drain on my time since I would manually input the address into Google maps to check how far it was from the campus. Also, if a rental search was unsuccessful for that week, you'd probably have to search the listings again, which would keep getting updated, wasting time again. Keywords like "Female house only" meant that males would not be rented a house. Listings on the website can only be sorted according to a few attributes.

Hence, I decided to scrape the McMaster housing website to collect all the relevant information, filter irrelevant information and sort listings according to what's important.

You will need Python 2.7, pip, and a Google Maps API key.

#### Installation steps :
```
1. Install the following packages:
> pip install Scrapy
> pip install service_identity
> pip install pygeocoder
2. (Optional) If you want to obtain distance information from the house to McMaster: 
> Visit the APIs Console at https://code.google.com/apis/console and log in with your Google Account.
> Click the APIs link from the left-hand menu.
> Activate the Geocoding API service.
> Click the Credentials link from the left-hand menu. Your API key is available here.
> Add your Google API key to maps_api_key.txt as the first and only line.
> Toggle "shouldUseGoogleMaps" to True in the scrapy_mac_rent_spider.py file.
```

#### Additional configuration :

To add urls to scrape, append new elements to the "start_urls" list in the scrapy_mac_rent_spider.py file. Go to https://macoffcampus.mcmaster.ca/classifieds/category/student-rentals/ if you want to use McMaster University's filter to initially filter out "Zones". In this repo, I have only considered Zone 1 and set occupancy to September. You can change this of course but remember to add this url as directed above. 

To scrape rentals, run this command from the top level directory.
```
> scrapy crawl macrent -o items.csv
```
This command creates an items.csv file containing all the scraped listings. Running this command multiple times only appends to the items.csv file (doesn't remove what was already in this file). Once you have the csv, you can load it into Excel or OpenOffice to sort on whichever columns you want. If you want to filter/query the dataset, you can load the csv file into Python/R/Matlab/etc. If you want a json file, change the command to :
```
> scrapy crawl macrent -o items.json
```

If you don't want to provide a Google Maps API, toggle "shouldUseGoogleMaps" to False in the scrapy_mac_rent_spider.py file. Google Maps API is used to get the geolocation of houses, used to calculate the distance of the house from McMaster. Note that Google has a 2,500 free requests limit for geocoding queries per day. Mac listings for Zone 1 are usually < 100, which means you should be able to run the program about 25 times per day if you enable "shouldUseGoogleMaps" in the scrapy_mac_rent_spider.py file.

#### Disclaimer :

Please use this program responsibly. Scraping code was tested working as of July 2014, for houses in Zone 1 (not tested with other Zones). Any changes on the website being scraped would necessarily require modifications to the scraping logic.
