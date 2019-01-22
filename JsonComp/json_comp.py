import json
from pprint import pprint
from readJsonCompConfig import readConfig

#load the JSON file
def loadJson(filename):
    with open(filename) as f:
        return json.load(f)
#End of function

#Compare the elements - list or dictionary or anything else
def compare_json_data(source_data_a,source_data_b):
    def compare(data_a,data_b):
        # type: list
        if (type(data_a) is list):
            # is [data_b] a list and of same length as [data_a]?
            if (
                (type(data_b) != list) or
                (len(data_a) != len(data_b))
            ):
                return False
            else:
                # Sort the lists
                data_a.sort()
                data_b.sort()
                # iterate over list items
                for list_index,list_item in enumerate(data_a):
                    # compare [data_a] list item against [data_b] at index
                    if (not compare(list_item,data_b[list_index])):
                        return False
                # list identical
                return True
        # type: dictionary
        elif (type(data_a) is dict):
            # is [data_b] a dictionary?
            if (type(data_b) != dict):
                return False
            # iterate over dictionary keys
            for dict_key,dict_value in data_a.items():
                # key exists in [data_b] dictionary, and same value?
                if (
                    (dict_key not in data_b) or
                    (not compare(dict_value,data_b[dict_key]))
                ):
                    return False
            # dictionary identical
            return True
        # simple value - compare both value and type for equality
        else:
            return data_a == data_b
    # compare a to b in recursion unless meet the base condition
    return compare(source_data_a,source_data_b)
#End of compare

# Compare the 2 list based on configuration
def compareConfigBased(lhsList, rhsList, lhsFile, rhsFile):
    if ((len(lhsList) == 1) and (len(rhsList) == 1)):
        return compare_json_data(lhsFile[lhsList[0]],rhsFile[rhsList[0]])
    for l in range(len(lhsList)-1):
        for r in range(len(rhsList)-1):
            return False            

#End of Function

# Test the Function        
if __name__=="__main__":
     #Get first file loaded
     file = 'a.json'
     in_data1 = loadJson(file)
     #pprint (input_data)
     #Get second file loaded
     file = 'b.json'
     in_data2 = loadJson(file)
     #Get configuration fle loaded
     list = readConfig("Config.txt")
     #Compare
     for m in range(len(list)-1):
             elemList = list[m]
             lhsList = elemList[0]
             rhsList = elemList[1]
             if (compareConfigBased (lhsList, rhsList, in_data1, in_data2)):
                print ("Good: Values {l} and {r} matched".format(l=lhsList,r=rhsList))
             else:   
                print ("Error: Values {l} and {r} not matched".format(l=lhsList,r=rhsList))
     #hardcoded example -- can be removed once working code established
     var1="carrot"
     list = in_data1[var1]
     print ("Value is: {v}, and length is {l}".format(v=in_data1[var1][0]["fourth"],l=len(list)))
