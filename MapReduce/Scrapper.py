import urllib2
from bs4 import BeautifulSoup
url = "https://www.nytimes.com/2018/03/19/technology/facebook-data-sharing.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, ‘html.parser’)
