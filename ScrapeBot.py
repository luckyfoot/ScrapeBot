from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def get_page():
    try:
        """
        beg_address= "https://"
        mid_address= ".craigslist.org/search/rva?query="
        post_w_pic= "&hasPic=1"
        address= ""

        city=input('Search city?: ')
        first_search_param=input('What Are we looking for?: ')
        max_price = int(input('Max price?:'))
        min_price = int(input('Min price?: '))

        address= beg_adress + city + mid_address + first_search_param + post_w_pic + "&" + max_price + "&" + min_price

        print(address)
        """
        
        html = urlopen("https://seattle.craigslist.org/search/rva?query=trailer&hasPic=1&min_price=2000&max_price=10000")
        parsed_listings = BeautifulSoup(html, "html.parser")
        clean_posts = parsed_listings.findAll("a", {"class" : "result-title"})
    except:
        print('Unable to connect to Craigslist. check your connection and try again later')

    return clean_posts

def wr_page(postings):
    count = 0
    
    for post in postings:
        for t in post:
            title.append(t)
        if 'href' in post.attrs:
            address.append(post.attrs['href'])

    for link in address:
        count += 1
        actualLink.append(link )
    try:
        scrapePage = open("trailerScrape.html", "w")
        scrapePage.write("<html>")
        scrapePage.write("<h1 style = \"font-weight:bold; font-size:200%\"> These are the top Craiglist postings for Trailers with a min. price of 2K</h1><br />")

        for link in actualLink:
            scrapePage.write("<a href= ")
            scrapePage.write(link)
            scrapePage.write(">")
            scrapePage.write(title[count])
            scrapePage.write("</a><br />")
            count = count +1   
        scrapePage.write("</html>")
        scrapePage.close()

    except:
        print("Uh-oh something went wrong, unable to open the write file")
        return

craigslist = "https://seattle.craigslist.org"
actualLink = []
address = []
title = []


srch_rslts = get_page()
wr_page(srch_rslts)


print('I finished')


		
