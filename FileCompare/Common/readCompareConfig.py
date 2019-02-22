#read config file and follow the grammer
#var1.var2 means var2 is nested in a list var1
def readConfig(filename):
        configlist = [] # the main list with all confg elements
        with open(filename) as f:
            for line in f:
                if not (line.startswith("#")):
                    list = line.strip('\n').split('=')
                    # a two element list for each element in config list
                    configlist.append([list[0].split('.'), list[1].split('.')])
        return configlist
#End of Function        
#Test the function
if __name__=="__main__":
        config = "config.txt"
        print (readConfig(config))