# Hack a thing 2 -- Erika and Kristie -- Moogle  (movie + google)
## Description
Our website allows you to get a summary of all the important information about a movie using Wikipedia as the source. We used the package Beautiful Soup to help with the webscraping, a Python Flask Backend, and plain HTML/CSS.

## Who did what

### Erika
Followed webscraping tutorial
https://www.youtube.com/watch?v=XQgXKtPSzUI
attempted to use tutorial to webscrape amazon page, but realized the html tags were too complex for amazon with many layers (attempt can be found on webscraping_amazon.py file), so switched to wikipedia.

Worked with Kristie to scrape necessary information from wikipedia pages using Python using skills from tutorial above. Wrote the code to clean up the dictionary. 

### Kristie
Worked with Erika to scrape necessary information from wikipedia pages using Python.
Used the following tutorial (https://pythonhow.com/html-templates-in-flask/) to set up a basic Flask Backend and connect it with HTML/CSS templates. Retrieved assets from Google (credit: http://the-toast.net/2014/11/14/moogle-mom-search-engine/). Parsed the script we made together to dynamically update our backend based on user input.


## What we learned
Some webpages are much easier to webscrape than others, how to build a Flask Backend and connect it with a frontend, more about HTML tags and styling, a little bit about AJAX (tried and it didn't work).

## How does this hack inspire you or relate to your possible project ideas?
Webscraping is a valuable tool if done right since it basically makes any website your dataset. 


## What didn't work

Tried to use AJAX on a plain HTML file instead of building out a backend, but ultimately found it was not only better but also easier to make a Flask backend! Also tried to use BeautifulSoup to scrape Amazon at first but found that Wikipedia's tags and HTML is much more friendly to work with. Our search also only works if the user inputs the movie in the same format as the corresponding wikipedia page's header/url.

## Local setup instructions

-If you don't have virtualenv installed, do it using `pip install virtualenv`
-Then, in the directory which stores virtualenv.py, run `virtualenv ENV`
-To activate once you're in your virtualenv, run `source ENV/bin/activate`
-To run the project locally, run `python app.py`

Also need to have the following installed: 
`pip install flask`
`pip install beautifulsoup4`
`pip install flask_restful`
