import scrapy
from scrapy import Request
from scrapy_mac_rent.items import ScrapyMacRentItem
from pygeocoder import Geocoder
from math import sin, cos, sqrt, atan2, radians

class ScrapyMacRentSpider(scrapy.Spider):
    name = "macrent"
    shouldUseGoogleMaps = True
    api_key = ""
    allowed_domains = ["macoffcampus.mcmaster.ca"]
    start_urls = [
        "https://macoffcampus.mcmaster.ca/classifieds/category/student-rentals/?s&price_from&price_to&zone=1&spaces_from&spaces_to&occupancy_select=10&bedrooms_from&bedrooms_to&internet=0&furnished=0",
        "https://macoffcampus.mcmaster.ca/classifieds/category/student-rentals/page/2/?s&price_from&price_to&zone=1&spaces_from&spaces_to&occupancy_select=10&bedrooms_from&bedrooms_to&internet=0&furnished=0"
        "https://macoffcampus.mcmaster.ca/classifieds/category/student-rentals/page/3/?s&price_from&price_to&zone=1&spaces_from&spaces_to&occupancy_select=10&bedrooms_from&bedrooms_to&internet=0&furnished=0"
        "https://macoffcampus.mcmaster.ca/classifieds/category/student-rentals/page/4/?s&price_from&price_to&zone=1&spaces_from&spaces_to&occupancy_select=10&bedrooms_from&bedrooms_to&internet=0&furnished=0"
    ]

    def __init__(self):
        print("Initializing...")
        if shouldUseGoogleMaps:
            with open ("maps_api_key.txt", "r") as api_file:
                api_key = api_file.read()
                
            gmaps = Geocoder(api_key=api_key)
    
    def haversine(self, latitude1, longitude1, latitude2, longitude2):
        R = 6373.0
        lat1 = radians(latitude1)
        lat2 = radians(latitude2)
        lon1 = radians(longitude1)
        lon2 = radians(longitude2)
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2 
        c = 2 * atan2( sqrt(a), sqrt(1-a) ) 
        d = R * c
        return d

    def dirn(self, latitude1, longitude1, latitude2, longitude2):
        if(latitude2 - latitude1 > 0 and longitude2 - longitude1 > 0):
            return "NE"
        elif(latitude2 - latitude1 < 0 and longitude2 - longitude1 < 0):
            return "SW"
        elif(latitude2 - latitude1 > 0 and longitude2 - longitude1 < 0):
            return "NW"
        elif(latitude2 - latitude1 < 0 and longitude2 - longitude1 > 0):
            return "SE"
        else:
            return "~"

    def parse(self, response):
        for sel in response.xpath('//div[@class="address"]'):
            item = ScrapyMacRentItem()
            item['address'] = sel.xpath('a/text()')[0].extract().strip()
            item['zone'] = sel.xpath('a/text()')[1].extract().strip()
            item['url'] = sel.xpath('a/@href')[0].extract().strip()

            if shouldUseGoogleMaps:
                coords = self.gmaps.geocode(item['address'] + ", Hamilton, ON L8S")[0].coordinates
                item['latitude'] = coords[0]
                item['longitude'] = coords[1]
                item['dist'] = self.haversine(43.25792970000001, -79.9181011, coords[0], coords[1])
                item['dirn'] = self.dirn(43.2583633, -79.91991700000001, coords[0], coords[1])
            
            yield Request(item['url'], meta={'item': item}, callback=self.parse_listing) 

    def parse_listing(self, response):
        item = response.request.meta['item']
        for sel in response.xpath('//div[@class="entry-content post"]'):
            item['lease'] = sel.xpath('//div[contains(strong, "Lease")]/text()').extract()[1].strip()
            item['rent_amt'] = sel.xpath('//div[contains(strong, "per month")]/text()').extract()[0].strip()
            item['contact_name'] = sel.xpath('//div[contains(strong, "Name")]/text()').extract()[1].strip()
            item['description'] = sel.xpath('//div[@class="ocrc_ad_description"]/text()').extract()
            
            female_keyword = False
            for desc in item['description']:
                if("female" in desc.lower()):
                    female_keyword = True
            
            item['female_keyword'] = female_keyword

            pri_ph = sel.xpath('//div[contains(strong, "Primary Phone")]/text()').extract()
            sec_ph = sel.xpath('//div[contains(strong, "Secondary Phone")]/text()').extract()
            
            if(len(pri_ph) > 1):
                item['contact_ph'] = pri_ph[1].strip()

            if(len(sec_ph) > 1):
                item['contact_sec_ph'] = sec_ph[1].strip()

            item['num_bedrooms'] = sel.xpath('//div[contains(strong, "Number of Bedrooms in Apt/House")]/text()').extract()[1].strip()
            item['num_bedrooms_for_rent'] = sel.xpath('//div[contains(strong, "Number of Bedrooms for Rent")]/text()').extract()[1].strip()
            item['utils'] = sel.xpath('//div[contains(strong, "Utilities Costs Included in Rent")]/text()').extract()[1].strip()
            item['internet'] = sel.xpath('//div[contains(strong, "Internet")]/text()').extract()[1].strip()

        img_list = []

        for sel in response.xpath('//div[@id="ocrc-entry-images"]'):
            img = sel.xpath('a/@href').extract()
            if(len(img) > 1):
                img_list.append(img[0].strip())

        item['images'] = img_list

        print(item)