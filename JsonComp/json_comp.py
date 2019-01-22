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
#This function supports 3 levels of nesting
def _getValueFromJsonFile(list, file_data):
    if (len(list) == 1):
        return [file_data[list[0]]]
    if (len(list) == 2):
        return [file_data[list[0]][i][list[1]] for i in range(0, len(file_data[list[0]]))]
    elif (len(list) == 3):
        return [
                 file_data[list[0]][i][list[1]][j][list[2]]
                 for i in range(0, len(file_data[list[0]]))
                 for j in range(0, len(file_data[list[0]][i][list[1]]))
               ]
    else:
        raise Exception("More than 3 nested levels are not supported.")
#End of private function

# Compare the json data elements based on configuration
def compareConfigBased(elemList, lhsFileData, rhsFileData):
    if (elemList == []):
        return False
    return compare_json_data(
                              _getValueFromJsonFile(elemList[0],lhsFileData),
                              _getValueFromJsonFile(elemList[1],rhsFileData)
                            )
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
     for m in range(0,len(list)):
        if (compareConfigBased (list[m], in_data1, in_data2)):
            print ("Good: Values {l} and {r} matched".format(l=list[m][0],r=list[m][1]))
        else:   
            print ("Error: Values {l} and {r} not matched".format(l=list[m][0],r=list[m][1]))
