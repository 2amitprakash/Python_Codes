from tokenize import tokenize

#read config file and follow the grammer
#var1.var2 means var2 is nested in a list var1
def readconfig(filename):
    with open(filename) as f:
            for line in f:
                        
        return load(f)

