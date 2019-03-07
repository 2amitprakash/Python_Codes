import FileCompare.Common.readCompareConfig as rc
import FileCompare.Json.json_file_processor as jfp

#Compare the elements - list or dictionary or anything else
def compare_json_data(source_data_a,source_data_b):
    def compare(data_a,data_b):
        # type: list
        if (isinstance(data_a, list)):
            #print("Comparing lists: {a} and {b}".format(a=data_a, b=data_b))
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
            #print("Comparing dicts: {a} and {b}".format(a=data_a, b=data_b))
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
            #print("Comparing values: {a} and {b}".format(a=data_a, b=data_b))
            return data_a == data_b
    # compare b to a in recursion unless meet the base condition
    return compare(source_data_b,source_data_a)
#End of compare

# Compare the data elements based on configuration and file type
def compareConfigBased(elemList, file1_list,file1_list_count,file2_list,file2_list_count):
    if (elemList == []):
        return False
    value1 = jfp.getValueFromJsonFile(elemList[0],file1_list,file1_list_count)
    value2 = jfp.getValueFromJsonFile(elemList[1],file2_list,file2_list_count)
    #print (value1, value2)
    return compare_json_data(value1,value2)
#End of Function

def run_compare():
    file1 = "a.json"
    file2 = "b.json"
    cfile = "Config.txt"
    #Get first file loaded
    flat_json_1, lCount_1 = jfp.flatten_json(jfp.loadJson(file1))
    #print ("Flattened JSON ----",flat_json_1)
    #print ("List of the counts ----", lCount_1)
    #Get second file loaded
    flat_json_2, lCount_2 = jfp.flatten_json(jfp.loadJson(file2))
    #Get configuration fle loaded
    lst = rc.readConfig(cfile)
    #Compare
    for m in range(0,len(lst)):
        if (compareConfigBased (lst[m],flat_json_1, lCount_1,flat_json_2, lCount_2)):
            print ("Good: Values for {l} and {r} matched".format(l=lst[m][0],r=lst[m][1]))
        else:   
            print ("Error: Values for {l} and {r} not matched".format(l=lst[m][0],r=lst[m][1]))

# Test the Function        
if __name__=="__main__":
    run_compare()