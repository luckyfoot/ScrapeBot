# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

class CraigBot:

    def __init__(self):
        self.city = ""
        self.maxDistance = 1
        self.hasPics = True
        self.maxPrice = 1
        self.minPrice = 0
        self.query = ""
        self.zip = 0

    def get_query(self):
        self.query = str(input('What to search for?'))

    def get_city(self):
        self.city = str(input('What city? : '))

    def get_zip(self):
        self.zip = int(input('What Zip code? :'))

    def get_maxDistance(self):
        self.maxDistance = int(input('Max distance(miles)? :'))

    def get_maxPrice(self):
        self.maxPrice = int(input('What is the max Price? :'))

    def get_minPrice(self):
        self.minPrice = int(input('What is the min Price? :'))


def search_page():
            try:
                mid_address = ".craigslist.org/search/rva?query="
                has_pic = "hasPic=1"
                cr = "&"
                sort = "sort=rel"
                search_dist = "search_distance"
                address = "https://"
                post = "postal="
                min_price = "min_price"
                max_price = "max_price"

                address += query_param.city
                address += mid_address
                address += query_param.query
                address += cr
                address += sort
                address += cr
                address += has_pic
                address += cr
                address += search_dist
                address += query_param.maxDistance
                address += cr
                address += post
                address += query_param.zip
                address += cr
                address += min_price
                address += query_param.minPrice
                address += cr
                address += max_price
                address += query_param.maxPrice

                print(address)

                html = urlopen(address)
                parsed_listings = BeautifulSoup(html, "html.parser")
                results = parsed_listings.findAll("a",
                {"class": "result-title"})
            except:
                print('Unable to connect to Craigslist.')
                print('check your connection and try again later')

            return results


def output(results):

    pass


print('Welcome to CraigBot')

craig = CraigBot()

craig.get_query()
craig.get_maxPrice()
craig.get_minPrice()
craig.get_maxDistance()
craig.get_city()
craig.get_zip()

posts = search_page()