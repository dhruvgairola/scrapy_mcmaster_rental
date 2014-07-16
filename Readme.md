This project is for McMaster students who are looking to rent rooms via the McMaster offcampus housing website. I personally found that manually going through the ads was a huge drain on my time since I would manually input the address into Google maps to check how far it was from the campus. Also, if a rental search was unsuccessful for that week, you'd proabably have to search the listings again, which would keep getting updated, wasting time again. Keywords like "Female house only" meant that males would not be rented a house.

Hence, I decided to scrape the McMaster housing website to collect all the relevant information and sort it according to my own criteria (you can only sort on a few useless criteria on the McMaster website.)

You will need Python 2.7 for this project and an Google Maps API key.
Installation steps :
```
pip install Scrapy
pip install service_identity
pip install pygeocoder
```

Add your Google API key to maps_api_key.txt as the first and only line.

Visit the APIs Console at https://code.google.com/apis/console and log in with your Google Account.
Click the APIs link from the left-hand menu.
Activate the Geocoding API service.
Click the Credentials link from the left-hand menu. Your API key is available here.
