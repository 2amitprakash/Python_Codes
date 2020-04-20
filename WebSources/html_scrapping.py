from lxml import html
import requests
import os
import csv

htmlfiles = []
for root, dirs, files in os.walk("/Users/amitprakash/Documents"):
    for file in files:
        if file.endswith(".html"):
            htmlfiles.append(os.path.join(root, file))
print ("File List : ", htmlfiles)
#page = requests.get('https://covid19.healthdata.org/united-states-of-america/virginia')
#tree = html.fromstring(page.content)
#measure = tree.xpath('//*[@id="root"]/div/main/div[3]/div[1]/div[2]/div[1]/div[1]/text()')
#value = tree.xpath('//*[@id="root"]/div/main/div[3]/div[1]/div[2]/div[1]/div[2]/text()')

for htmlfile in htmlfiles:
    with open(htmlfile, "r") as f:
        tree = html.fromstring(f.read())
        lmeasure = tree.xpath('//div[@class="_3xMrzF3nxII5ysvl1_7Ncx _1K95TivjKGl4X5qplZyPFT"]/text()')
        lvalue = tree.xpath('//div[@class="fOHfNYVUtJdcPK7UXSNn4"]/text()')
        state = tree.xpath('//span[@class="ant-select-selection-item"]/text()')

        for _ in lmeasure:
            state.extend(state)

        #Combine the measure and date values
        lall = [lmeasure,lvalue]
        #map the result for measure with corresponding dates
        lcsv = list(map(list, zip(*lall)))
        lrows = [[x] + y for x, y in zip(state, lcsv)]
        
        print ("List of Measures: ", lmeasure)
        print ("List of Values: ", lvalue)
        print ("Combined list: ", lrows)
        print ("State: ", state[0]) 

        with open("US_State_Measures.csv", 'a', newline='') as cf:
            writer = csv.writer(cf)
            writer.writerow(lrows)
