

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://en.wikipedia.org/wiki/Hannah_Montana:_The_Movie'

# opening up connection and grabbing page 
uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()

# parsing through the page 
page_soup= soup(page_html,"html.parser")


table_body=page_soup.find('tbody')
rows= table_body.find_all('tr')
result = []
for i in range(len(rows)):
	cols=rows[i].find_all('td')
	result.append(cols)

master={}

# print(len(page_soup.findAll("th",{"style":"white-space:nowrap;padding-right:0.65em;"})))
# print(len(result))
print("________________")
print(result)
for j in range(2,len(result)):

	containers= page_soup.findAll("th",{"style":"white-space:nowrap;padding-right:0.65em;"})[j-2].string
	classname= result[j][0].find_all("div",{"class":"plainlist"})

	# print(classname)
	if classname == []:
		if not result[j][0].find('a'):

			body=str(result[j][0])[4:-5]

		else:
			body = result[j][0].find('a').string # one item
		# print(string)

	else:
		body = [] # list
		string= result[j][0].find_all('li')
		for i in range(len(string)):
			s = string[i].string
			body.append(s)

	master[containers]=body

print(master)

## Dictionary file 

