import json
import copy
from readJsonCompConfig import readConfig

def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
            A list of elements having a type list and count of children
    """
    out = {}
    lCount = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
            lCount[name[:-1]] = i # create the list count    
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out, lCount

#load the JSON file
def loadJson(filename):
    with open(filename) as f:
        return json.load(f)
#End of function

#Compare the elements - list or dictionary or anything else
def compare_json_data(source_data_a,source_data_b):
    def compare(data_a,data_b):
        # type: list
        if (isinstance(data_a, list)):
            # is [data_b] a list and of same length as [data_a]?
            if (
                not (isinstance(data_b, list)) or
                (len(data_a) != len(data_b))
            ):
                return False
            else:
                # Sort the lists
                #data_a.sort()
                #data_b.sort()
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
            print("Comparing value", data_a, data_b)
            return data_a == data_b
    # compare b to a in recursion unless meet the base condition
    return compare(source_data_b,source_data_a)
#End of compare

#This function extracts value from JSON file for a given hierarchy in config file
def _getValueFromJsonFile(lst, lhs):
    #Check if a constant value to return then not read in JSON file
    if ( not (lst == []) and len(lst) == 3):
        if (lst[0] == "R"): #To handle comparison to constant/real values
            print ("Found R and value ", lst[2])
            if (lst[1] == "None"):
                return [None]
            elif (lst[1] == "Int"):
                return [int(lst[2])]
            elif (lst[1] == "Real"):
                return [float(lst[2])]
            elif (lst[1] == "True"):
                return [True]
            elif (lst[1] == "False"):
                return [False]
            else:
                return [lst[2]]
    #If not constant then
    if (lhs):
        file_data = in_data1
        list_lCount = lCount_1
        flat_json = flat_json_1
    else:
        file_data = in_data2
        list_lCount = lCount_2
        flat_json = flat_json_2
    #If length == 1 then return directly
    if (len(lst) == 1):
        return [file_data[lst[0]]]
    else:
        vlist=[]
        for e_count in range(0,len(lst)):
            elem = lst[e_count]
            if (vlist == []):
                vlist = [elem]
            else:
                vlist = [s + elem for s in vlist]
            #Get the count list for each list type
            l_count = [list_lCount[v] if v in list(list_lCount) else 0 for v in vlist]
            # add the elements accordingly to build the list of keys
            nvlist = []
            for ct in range(0,len(l_count)):
                cnt = l_count[ct]
                if (cnt == 0): # a dict
                    #print ("dict:", elem)
                    nvlist.append(vlist[ct] + ".")
                else: # a list
                    #print ("list:", elem)
                    for i in range(0, cnt):
                        nvlist.append(vlist[ct] + "." + str(i) + ".")
            vlist = copy.deepcopy(nvlist)
        return [flat_json[key.strip(".")] for key in vlist]
#End of private function

# Compare the json data elements based on configuration
def compareConfigBased(elemList):
    if (elemList == []):
        return False
    value1 = _getValueFromJsonFile(elemList[0],True)
    value2 = _getValueFromJsonFile(elemList[1],False)
    #print (value1, value2)
    return compare_json_data(value1,value2)
#End of Function

# Execute the Function        
if __name__=="__main__":
     #Get first file loaded
     file = 'C:\\MyWork\\Abacus\\Utility\\Test\\inputclaim.json' 
     #file = 'a.json'
     in_data1 = loadJson(file)
     flat_json_1, lCount_1 = flatten_json(in_data1)
     #print ("Flattened JSON ----",flat_json_1)
     #print ("List of the counts ----", lCount_1)
     #print (lCount_1["carrot"])
     #Get second file loaded
     file = 'C:\\MyWork\\Abacus\\Utility\\Test\\entities_claim.json' 
     #file = 'b.json'
     in_data2 = loadJson(file)
     flat_json_2, lCount_2 = flatten_json(in_data2)
     #Get configuration fle loaded
     lst = readConfig("C:\\MyWork\\Abacus\\Utility\\Test\\config.txt")
     #lst = readConfig("Config.txt")
     #Compare
     for m in range(0,len(lst)):
        if (compareConfigBased (lst[m])):
            print ("Good: Values for {l} and {r} matched".format(l=lst[m][0],r=lst[m][1]))
        else:   
            print ("Error: Values for {l} and {r} not matched".format(l=lst[m][0],r=lst[m][1]))
