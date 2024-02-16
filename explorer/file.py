import os


def get_upper_level(path):
    tmp = apart(path, "/")  # apart to list
    del tmp[len(tmp) - 1]  # delect last path
    if len(tmp) != 0:
        return together(tmp, "/")  # convert list to path string
    else:
        return False
     
    
    
    
def isFolder(path):
    if os.path.isdir(path):
        return True 
    elif os.path.isfile(path):
        return False 

# apart string its path

def apart(string, char):
    if string[len(string) - 1] != char:
        string += char
    tmp = ""
    res = []
    for i in string:
        if i == char:
            res.append(tmp)
            tmp = ""
        else:
            tmp += i
    return res


def together(list, char):
    res = ""
    for i in list:
        i += char
        res += i
    return res

    
      
    
    