import Movies
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods=['POST'])
def movie():
    projectpath = request.form['projectFilepath']
    projectpath = projectpath.replace(" ", "_")
    my_url="https://en.wikipedia.org/wiki/"+ projectpath
    # opening up connection and grabbing page
    uClient = uReq(my_url)
    page_html= uClient.read()
    uClient.close()

    # parsing through the page
    page_soup= soup(page_html,"html.parser")

    # getting table elements
    table_body=page_soup.find('tbody')
    rows= table_body.find_all('tr')
    result = []
    for i in range(len(rows)):
        cols=rows[i].find_all('td')
        result.append(cols)

    # creating dictionary to save everything into
    master={}

    #get image infomrmation
    src= result[1][0].find('img')['src'][2:]
    master["image"]=src

    # looping through the text information
    for j in range(2,len(result)):

        key= page_soup.findAll("th",{"style":"white-space:nowrap;padding-right:0.65em;"})[j-2].string
        classname= result[j][0].find_all("div",{"class":"plainlist"})

        if classname == []: # one item
            if not result[j][0].find('a'):
                body=str(result[j][0])[4:-5]

            else:
                body = result[j][0].find('a').string

        else: # list of items
            body = []
            string= result[j][0].find_all('li')
            for i in range(len(string)):
                s = string[i].string
                body.append(s)

        master[key]=body

    print("----------")
    print(master)
    #cleaning up the dictionary, deleting information that we do not want
    to_be_deleted=[]
    for key in master:
        if isinstance(master[key],list) and len(master[key])==1:
            to_be_deleted.append(key)
        if str(master[key])[0] == "[":
            to_be_deleted.append(key)
    for key in to_be_deleted:
        del master[key]

    res_string = "<img src='https://"+ src +"""' alt='Picture'style='  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%; width: 200px;margin-top: 50px;'>"""
    res_string += """<table style='margin-left:auto;
    margin-right:auto; width: 500px;margin-top: 50px;'>"""
    for k,v in master.items():
        res_string += "</tr>"
        res_string += "<td><b>" + str(k) + "<b></td>"
        res_string += "<td>" + str(v) + "</td>"
        res_string += "</tr>"

    res_string += "</table>"
    master = str(master)[1:-1]
    master = master.replace(",", "\n")

    return res_string


if __name__ == '__main__':
     app.run(debug=True)
