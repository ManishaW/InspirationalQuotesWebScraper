# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.dailyinspirationalquotes.in/'

page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class': 'td-excerpt'})

#strip() is used to remove starting and trailing
name = name_box.text.strip() 
print name.replace("Read more", "").strip()
