import json
from pprint import pprint
from tokenize import tokenize

#load the JSON file
def loadJson(filename):
    with open(filename) as f:
        return json.load(f)

if __name__=="__main__":
        file = 'a.json'
        input_data = loadJson(file)
        pprint (input_data)
        var1="carrot"
        list = input_data[var1]
        print ("Value is: {v}, and length is {l}".format(v=input_data[var1][0]["fourth"],l=len(list)))
