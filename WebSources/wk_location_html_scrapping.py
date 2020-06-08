from lxml import html
import requests
import os
import csv

#Deleting the csv file if it exists
csvfile = "WK_Locations.csv"
try:
    os.remove(csvfile)
except OSError:
    pass

#website scrape code
page = requests.get('https://wolterskluwer.com/products-services/support/offices/united-states.html')
tree = html.fromstring(page.content)
#measure = tree.xpath('//*[@id="root"]/div/main/div[3]/div[1]/div[2]/div[1]/div[1]/text()')
#value = tree.xpath('//*[@id="root"]/div/main/div[3]/div[1]/div[2]/div[1]/div[2]/text()')


lstate = tree.xpath('/html/body/main/article/div/div/div/div/table/tbody/tr[2]/td[1]/h2[1]/a[@id]/text()')

print ("States: ", lstate)

with open(csvfile, 'a', newline='') as cf:
    writer = csv.writer(cf)
    #writer.writerows(lrows)
