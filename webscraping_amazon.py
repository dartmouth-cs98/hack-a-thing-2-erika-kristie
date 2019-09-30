# Webscraping for amazon URL 
# DOES NOT WORK 

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.amazon.com/s?k=alexa&ref=nb_sb_noss_2'

# opening up connection and grabbing page 
uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()

# parsing through the page 
page_soup= soup(page_html,"html.parser")


# gets each product 
containers= page_soup.findAll("div",{"class":"sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"})

print(len(containers))


#remove amazon header
containers= containers[1:]
container=containers[1]
container.a.span.text