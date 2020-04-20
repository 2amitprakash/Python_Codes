# importing the libraries
from bs4 import BeautifulSoup
import requests

url="/Users/amitprakash/Documents/covid-19_va.html"

# Make a GET request to fetch the raw HTML content
#html_content = requests.get(url).text
# Parse the html content
#soup = BeautifulSoup(html_content, "lxml")

# Parse the file content
soup = BeautifulSoup(open(url), "lxml")
print(soup.prettify()) # print the parsed data of html
