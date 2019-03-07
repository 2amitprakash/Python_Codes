#Process JSON files for following functions:
#   1. store the elements in a list
#   2. extract value from list based on key defined in configuration file
import sys
import json
import copy

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
    with open(filename, "r") as f:
        return json.load(f)
#End of function

#This function extracts value from JSON file for a given hierarchy in config file
def getValueFromJsonFile(lst, flat_json, list_lCount):
    #Check if a constant value to return then not read in JSON file
    if ( not (lst == []) and len(lst) == 3):
        if (lst[0] == "R"): #To handle comparison to constant/real values
            #print ("Found R and value ", lst[2])
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
    #Start processing the comparison
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

# Test the Function        
if __name__=="__main__":
    file1 = "a.json"
    file2 = "b.json"
    #Get first file loaded
    flat_json_1, lCount_1 = flatten_json(loadJson(file1))
    print ("Flattened JSON ----\n",flat_json_1)
    #print ("List of the counts ----", lCount_1)
    #Get second file loaded
    flat_json_2, lCount_2 = flatten_json(loadJson(file2))
    print ("Flattened JSON ----\n",flat_json_2)
    #Get value
    clist = ["pear","fourth","second","coding"]
    print ("\nValue of pear.fourth.second.coding in first file: ", getValueFromJsonFile(clist, flat_json_1, lCount_1))
