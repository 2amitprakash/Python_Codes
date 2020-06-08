# importing the libraries
from bs4 import BeautifulSoup
import requests

url="https://wolterskluwer.com/products-services/support/offices/united-states.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Parse the file content
#soup = BeautifulSoup(open(url), "lxml")
#print(soup.prettify()) # print the parsed data of html

rows = soup.find_all("td")
type(rows)
lLocs = BeautifulSoup(str(rows[2]), "lxml").get_text()
lAdd = lLocs.replace('\n',':').split(':')
lAdd1 = [lAdd for lAdd in lAdd if not lAdd.startswith(' ')]
lAdd2 = [lAdd for lAdd in lAdd if lAdd.startswith(' ')]
print("State: ", lAdd1)
print("Address: ", lAdd2)
#for link in lLocs:
#    print("Record : ",link)
