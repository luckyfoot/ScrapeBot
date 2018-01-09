from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

craigslist = "https://seattle.craigslist.org"
count = 0
actualLink = []
address = []
title = []

html = urlopen("https://seattle.craigslist.org/search/rva?query=trailer&hasPic=1&min_price=2000&max_price=10000")
parsed_listings = BeautifulSoup(html, "html.parser")
postings = parsed_listings.findAll("a", {"class" : "result-title"})

for post in postings:
    for t in post:
        title.append(t)
    if 'href' in post.attrs:
        address.append(post.attrs['href'])

for link in address:
    actualLink.append(link )


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








