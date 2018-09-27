import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def file_data(file):
    path = ROOT_DIR + "/files"
    ls = os.listdir(path)
    
    for f in ls:
        if f == file:
            data = open(path+"/"+f, 'r')
            data = data.read()

            return data     

def file_exists(file):
    path = ROOT_DIR + "/files"
    ls = os.listdir(path)

    for f in ls:
        if f == file:
            return True
    
    return False